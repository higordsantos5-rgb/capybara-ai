"""Shared primitive types for Capybara AI."""

from enum import StrEnum


class Capability(StrEnum):
    """Capabilities that must be explicitly declared by model cards."""

    TEXT = "text"
    MARKDOWN = "markdown"
    CODE = "code"
    IMAGE = "image"
    PDF = "pdf"
    AUDIO = "audio"
    VIDEO = "video"
    FILE = "file"
    MCP_COMPATIBLE = "mcp_compatible"
    STREAMING = "streaming"
    STRUCTURED_OUTPUT = "structured_output"


class ContextType(StrEnum):
    """Supported context item types in V1."""

    TEXT = "text"
    MARKDOWN = "markdown"
    CODE = "code"
    IMAGE = "image"
    PDF = "pdf"
    AUDIO = "audio"
    VIDEO = "video"
    FILE = "file"
    MCP_RESOURCE = "mcp_resource"
    DERIVED = "derived"


class AdapterStatus(StrEnum):
    """Declared maturity for a provider adapter."""

    REAL = "real"
    EXPERIMENTAL = "experimental"
    CONTRACT = "contract"
    MOCK = "mock"


class ProviderName(StrEnum):
    """Providers known to the V1 architecture."""

    FAKE = "fake"
    OPENAI = "openai"
    GEMINI = "gemini"
    ANTHROPIC = "anthropic"
    XAI = "xai"
    DEEPSEEK = "deepseek"
    META = "meta"


SENSITIVE_KEYS = frozenset(
    {
        "api_key",
        "apikey",
        "authorization",
        "credential",
        "credentials",
        "secret",
        "token",
        "access_token",
        "refresh_token",
        "password",
        "headers",
    }
)
