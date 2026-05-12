# Multimodal Context

Capybara AI treats multimodal input as a capability boundary.

Supported context item types include text, markdown, code, image, PDF, audio,
video, generic file, MCP resource, and derived context.

If a request contains an image, the selected model must declare `image`. If a
request contains a PDF, the selected model must declare `pdf`, or your project
must configure an explicit pipeline that produces derived context.

Pipelines are traceable transformations. They do not become native model support.

