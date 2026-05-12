import Link from "next/link";

export function SiteHeader() {
  return (
    <header className="site-header">
      <Link className="brand" href="/" aria-label="Capybara AI home">
        <span className="brand-mark" aria-hidden="true" />
        <span>Capybara AI</span>
      </Link>
      <nav aria-label="Main navigation">
        <Link href="/docs">Docs</Link>
        <Link href="/docs/installation">Installation</Link>
        <a href="https://pypi.org/project/capybara-ai/">PyPI status</a>
      </nav>
    </header>
  );
}
