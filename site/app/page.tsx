import Link from "next/link";

import { CodeBlock } from "@/components/ui/code-block";
import { FeatureIcon } from "@/components/ui/feature-icon";
import { getReadmeOverview } from "@/lib/docs";

const features = [
  ["Capability Registry", "Declared model abilities are the source of truth."],
  ["Provider Routing", "Only enabled, configured, eligible models can run."],
  ["Multimodal Validation", "Image, PDF, audio, and video context is blocked unless supported or explicitly pipelined."],
  ["MCP Tool Permissions", "External tools require configuration, allowlists, scopes, and traceable permissions."],
  ["Structured Errors", "Failures stay explicit and inspectable instead of becoming vague text."],
  ["Provider Adapters", "Adapters declare honest maturity: mock, real, experimental, or contract."]
];

const principles = [
  "Explicit over implicit.",
  "Validate before execution.",
  "Capabilities are declared, never guessed.",
  "External tools are denied by default."
];

export default async function HomePage() {
  const overview = await getReadmeOverview();

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-art" aria-hidden="true">
          <div className="sun" />
          <div className="river" />
          <div className="leaf leaf-a" />
          <div className="leaf leaf-b" />
          <div className="capybara-mark">
            <span className="capybara-ear capybara-ear-left" />
            <span className="capybara-ear capybara-ear-right" />
            <span className="capybara-eye" />
            <span className="capybara-nose" />
          </div>
          <div className="terminal-float">
            <span>required: text, mcp_tools</span>
            <span>selected: fake/test</span>
            <span>fallback: denied</span>
          </div>
        </div>
        <div className="hero-copy">
          <h1>Capybara AI</h1>
          <p className="tagline">
            Predictable Python agents with explicit capabilities, safe provider routing,
            multimodal validation, and MCP tool permissions.
          </p>
          <div className="hero-actions">
            <Link className="button button-primary" href="/docs/getting-started/quickstart">
              Quickstart
            </Link>
            <Link className="button button-secondary" href="/docs">
              Docs
            </Link>
          </div>
          <CodeBlock code="pip install capybara-ai" language="bash" compact />
        </div>
      </section>

      <section className="feature-band" aria-labelledby="features-heading">
        <div className="section-heading">
          <h2 id="features-heading">Framework Boundaries You Can See</h2>
          <p>{overview.problem}</p>
        </div>
        <div className="feature-grid">
          {features.map(([title, text], index) => (
            <article className="feature-card" key={title}>
              <FeatureIcon index={index} />
              <h3>{title}</h3>
              <p>{text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="split-section">
        <div>
          <h2>Why Capybara AI?</h2>
          <p>{overview.why}</p>
          <p>
            Providers must be configured, models must be enabled, capabilities must be
            declared, and MCP tools are denied unless allowlisted.
          </p>
        </div>
        <div className="code-panel">
          <CodeBlock
            language="python"
            code={`from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(AgentConfig(name="assistant"))
result = agent.run(
    "Explain capability routing in one sentence.",
    fake_runner(),
)

print(result.output)
print(result.metadata.to_dict())`}
          />
        </div>
      </section>

      <section className="principles-band" aria-labelledby="principles-heading">
        <div>
          <h2 id="principles-heading">Design Principles</h2>
          <p>
            The V1 keeps the core small, provider-agnostic, and strict about what can
            run. The friendly surface is intentional; the runtime contract is firm.
          </p>
        </div>
        <ol>
          {principles.map((principle) => (
            <li key={principle}>{principle}</li>
          ))}
        </ol>
      </section>

      <section className="status-section">
        <div>
          <h2>Project Status</h2>
          <p>
            V1 is implemented and locally validated. The public package release is being
            prepared; the intended install command is already stable.
          </p>
        </div>
        <dl>
          <div>
            <dt>License</dt>
            <dd>MIT</dd>
          </div>
          <div>
            <dt>Package</dt>
            <dd>
              <a href="https://pypi.org/project/capybara-ai/">PyPI release pending: capybara-ai</a>
            </dd>
          </div>
          <div>
            <dt>Docs Source</dt>
            <dd>README.md and docs/**/*.md</dd>
          </div>
        </dl>
      </section>
    </div>
  );
}
