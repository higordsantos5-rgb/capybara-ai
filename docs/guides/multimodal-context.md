# Multimodal Context

Capybara AI treats multimodal input as part of routing, not as an afterthought.
Context items contribute capabilities to the request before a provider is called.

Supported context item types include:

- text;
- markdown;
- code;
- image;
- PDF;
- audio;
- video;
- generic file;
- MCP resource;
- derived context from an explicit pipeline.

```python
from capybara_ai.context import ContextItem
from capybara_ai.core.types import ContextType

context = [
    ContextItem(type=ContextType.IMAGE, data=b"...", source="upload"),
]
```

An image context item requires a model with the `image` capability. A PDF context
item requires native `pdf` support or a configured pipeline that produces
traceable derived context.

Pipelines are useful when your application wants to transform context before
routing. The transformation remains visible in metadata, and the derived context
does not pretend to be native model support.
