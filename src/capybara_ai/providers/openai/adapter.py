"""OpenAI adapter isolated from the provider-agnostic core."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.context.items import ContextItem
from capybara_ai.core.errors import (
    MissingCredentialError,
    ProviderExecutionError,
    ProviderUnavailableError,
)
from capybara_ai.core.execution import ExecutionRequest
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import AdapterStatus, ContextType, ProviderName
from capybara_ai.providers.base import ProviderResponse


@dataclass(slots=True)
class OpenAIProviderAdapter:
    """Real OpenAI adapter using the optional OpenAI SDK."""

    provider: str = ProviderName.OPENAI.value
    status: AdapterStatus = AdapterStatus.REAL
    requires_credentials: bool = True
    limitations: tuple[str, ...] = (
        "Requires capybara-ai[openai].",
        "Requires a consumer-provided API key.",
        "Only supports context types mapped by this adapter.",
    )

    def is_available(self) -> bool:
        try:
            import openai  # type: ignore[import-not-found]  # noqa: F401
        except ImportError:
            return False
        return True

    def execute(
        self,
        request: ExecutionRequest,
        card: ModelCard,
        credential: str | None,
        metadata: ExecutionMetadata,
    ) -> ProviderResponse:
        if not credential:
            raise MissingCredentialError(
                "OpenAI provider requires a consumer-provided API key.",
                details={"provider": self.provider},
            )
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise ProviderUnavailableError(
                "OpenAI SDK is not installed. Install capybara-ai[openai].",
                details={"provider": self.provider},
            ) from exc

        client = OpenAI(api_key=credential)
        payload: dict[str, Any] = {
            "model": card.model_id,
            "input": self._input_for_request(request),
        }
        if request.stream:
            payload["stream"] = True
        if request.structured_schema is not None:
            payload["text"] = {
                "format": {
                    "type": "json_schema",
                    "name": "capybara_ai_schema",
                    "schema": request.structured_schema,
                }
            }
        try:
            response = client.responses.create(**payload)
        except Exception as exc:  # noqa: BLE001
            raise ProviderExecutionError(
                "OpenAI provider call failed.",
                details={"provider": self.provider, "model": card.model_id},
            ) from exc
        metadata.validations.append("openai_responses_api_called")
        output = getattr(response, "output_text", None)
        if output is None:
            output = str(response)
        return ProviderResponse(
            output=output, raw_metadata={"provider_response_type": type(response).__name__}
        )

    def _input_for_request(self, request: ExecutionRequest) -> list[dict[str, Any]]:
        content: list[dict[str, Any]] = [{"type": "input_text", "text": request.prompt}]
        for item in request.context:
            if not isinstance(item, ContextItem):
                continue
            if item.type in {ContextType.TEXT, ContextType.MARKDOWN, ContextType.CODE}:
                content.append({"type": "input_text", "text": str(item.content)})
            elif item.type is ContextType.IMAGE:
                content.append({"type": "input_image", "image_url": str(item.content)})
        return [{"role": "user", "content": content}]
