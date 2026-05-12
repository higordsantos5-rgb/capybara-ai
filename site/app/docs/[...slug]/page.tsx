import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { DocsLayout } from "@/components/docs/docs-layout";
import { MarkdownPage } from "@/components/docs/markdown-page";
import { getAllDocSlugs, getDocBySlug, getDocsTree } from "@/lib/docs";

type PageProps = {
  params: Promise<{
    slug: string[];
  }>;
};

export async function generateStaticParams() {
  const slugs = await getAllDocSlugs();
  return slugs.filter((slug) => slug.length > 0).map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const doc = await getDocBySlug(slug);
  if (!doc) {
    return {};
  }

  return {
    title: doc.title,
    description: doc.excerpt
  };
}

export default async function DocPage({ params }: PageProps) {
  const { slug } = await params;
  const [doc, tree] = await Promise.all([getDocBySlug(slug), getDocsTree()]);

  if (!doc) {
    notFound();
  }

  return (
    <DocsLayout tree={tree} currentPath={doc.route}>
      <MarkdownPage doc={doc} />
    </DocsLayout>
  );
}
