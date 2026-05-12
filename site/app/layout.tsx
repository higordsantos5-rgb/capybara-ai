import type { Metadata } from "next";
import Link from "next/link";
import type { ReactNode } from "react";

import { SiteHeader } from "@/components/layout/site-header";
import "@/styles/globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://capybara-ai.vercel.app"),
  title: {
    default: "Capybara AI Documentation",
    template: "%s | Capybara AI"
  },
  description:
    "Capybara AI is a Python microframework for predictable AI agents with explicit model capabilities, safe provider routing, multimodal validation, and MCP tool permissions.",
  openGraph: {
    title: "Capybara AI",
    description:
      "Predictable AI agents with explicit model capabilities, safe provider routing, multimodal validation, and MCP tool permissions.",
    type: "website"
  }
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <a className="skip-link" href="#main">
          Skip to content
        </a>
        <SiteHeader />
        <main id="main">{children}</main>
        <footer className="site-footer">
          <div>
            <strong>Capybara AI</strong>
            <span>MIT licensed Python microframework.</span>
          </div>
          <nav aria-label="Footer">
            <Link href="/docs">Docs</Link>
            <Link href="/docs/installation">Installation</Link>
            <a href="https://pypi.org/project/capybara-ai/">PyPI status</a>
          </nav>
        </footer>
      </body>
    </html>
  );
}
