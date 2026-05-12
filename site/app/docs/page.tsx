import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { DocsLayout } from "@/components/docs/docs-layout";
import { MarkdownPage } from "@/components/docs/markdown-page";
import { getDocBySlug, getDocsTree } from "@/lib/docs";

export const metadata: Metadata = {
  title: "Documentation",
  description: "Browse the Capybara AI documentation."
};

export default async function DocsIndexPage() {
  const [doc, tree] = await Promise.all([getDocBySlug([]), getDocsTree()]);

  if (!doc) {
    notFound();
  }

  return (
    <DocsLayout tree={tree} currentPath="/docs">
      <MarkdownPage doc={doc} />
    </DocsLayout>
  );
}
