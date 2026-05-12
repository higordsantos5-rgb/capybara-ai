import { promises as fs } from "node:fs";
import path from "node:path";

export type DocPage = {
  content: string;
  excerpt: string;
  route: string;
  slug: string[];
  sourcePath: string;
  title: string;
};

export type DocTreeItem = {
  children: DocTreeItem[];
  route: string;
  slug: string[];
  title: string;
};

export type DocTree = {
  items: DocTreeItem[];
};

const projectRoot = path.resolve(process.cwd(), "..");
const docsRoot = path.join(projectRoot, "docs");
const readmePath = path.join(projectRoot, "README.md");

export async function getReadmeOverview() {
  const readme = await fs.readFile(readmePath, "utf8");
  return {
    problem: extractParagraphAfter(readme, "Why Capybara AI?"),
    why:
      "Direct SDK integrations are quick at first, but they often grow hidden assumptions around model authorization, multimodal input, fallback, secrets, and external tools."
  };
}

export async function getDocBySlug(slug: string[]): Promise<DocPage | null> {
  const sourcePath = slug.length === 0 ? path.join(docsRoot, "index.md") : path.join(docsRoot, ...slug) + ".md";

  if (!(await exists(sourcePath))) {
    return null;
  }

  const content = await fs.readFile(sourcePath, "utf8");
  const title = extractTitle(content) ?? titleFromSlug(slug.at(-1) ?? "Documentation");
  const excerpt = extractExcerpt(content);

  return {
    content,
    excerpt,
    route: slug.length === 0 ? "/docs" : `/docs/${slug.join("/")}`,
    slug,
    sourcePath,
    title
  };
}

export async function getAllDocSlugs() {
  const files = await listMarkdownFiles(docsRoot);
  return files
    .map((file) => {
      const relative = path.relative(docsRoot, file).replaceAll(path.sep, "/");
      if (relative === "index.md") {
        return [];
      }
      return relative.replace(/\.md$/, "").split("/");
    })
    .sort((left, right) => left.join("/").localeCompare(right.join("/")));
}

export async function getDocsTree(): Promise<DocTree> {
  const slugs = await getAllDocSlugs();
  const pages = (await Promise.all(slugs.map((slug) => getDocBySlug(slug)))).filter((doc): doc is DocPage => Boolean(doc));

  const items = pages.map((page) => ({
    children: [] as DocTreeItem[],
    route: page.route,
    slug: page.slug,
    title: page.title
  }));

  return { items };
}

export function markdownLinkToRoute(href: string, sourcePath: string) {
  if (!href || /^(https?:|mailto:|#)/.test(href)) {
    return href;
  }

  const [target, anchor] = href.split("#");
  if (!target.endsWith(".md")) {
    return href;
  }

  const absolute = path.resolve(path.dirname(sourcePath), target);
  const relativeToDocs = path.relative(docsRoot, absolute).replaceAll(path.sep, "/");
  const clean = relativeToDocs.replace(/(^|\/)index\.md$/, "$1").replace(/\.md$/, "").replace(/\/$/, "");
  const route = clean ? `/docs/${clean}` : "/docs";
  return anchor ? `${route}#${anchor}` : route;
}

async function listMarkdownFiles(directory: string): Promise<string[]> {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(
    entries.map(async (entry) => {
      const fullPath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        return listMarkdownFiles(fullPath);
      }
      return entry.isFile() && entry.name.endsWith(".md") ? [fullPath] : [];
    })
  );
  return nested.flat();
}

async function exists(filePath: string) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

function extractTitle(content: string) {
  return content.match(/^#\s+(.+)$/m)?.[1]?.trim();
}

function extractExcerpt(content: string) {
  return (
    content
      .replace(/^#\s+.+$/m, "")
      .split(/\n{2,}/)
      .map((part) => part.replace(/\s+/g, " ").trim())
      .find((part) => part.length > 40) ??
    "Capybara AI documentation page."
  );
}

function extractParagraphAfter(content: string, heading: string) {
  const [, after = ""] = content.split(`## ${heading}`);
  return extractExcerpt(after);
}

function titleFromSlug(slug: string) {
  return slug
    .split("-")
    .map((word) => word.slice(0, 1).toUpperCase() + word.slice(1))
    .join(" ");
}
