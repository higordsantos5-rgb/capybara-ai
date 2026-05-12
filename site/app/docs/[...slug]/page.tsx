import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { DocsLayout } from "@/components/docs/docs-layout";
import { MarkdownPage } from "@/components/docs/markdown-page";
import { SectionPage } from "@/components/docs/section-page";
import { getAllDocSlugs, getDocEntryBySlug, getDocsTree } from "@/lib/docs";

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
  const entry = await getDocEntryBySlug(slug);
  if (!entry) {
    return {};
  }

  return {
    title: entry.title,
    description: entry.excerpt
  };
}

export default async function DocPage({ params }: PageProps) {
  const { slug } = await params;
  const [entry, tree] = await Promise.all([getDocEntryBySlug(slug), getDocsTree()]);

  if (!entry) {
    notFound();
  }

  return (
    <DocsLayout tree={tree} currentPath={entry.route}>
      {entry.type === "page" ? <MarkdownPage doc={entry} /> : <SectionPage section={entry} />}
    </DocsLayout>
  );
}
