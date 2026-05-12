import { promises as fs } from "node:fs";
import path from "node:path";

export type DocPage = {
  type: "page";
  content: string;
  excerpt: string;
  route: string;
  slug: string[];
  sourcePath: string;
  title: string;
};

export type DocSection = {
  type: "section";
  excerpt: string;
  items: DocSectionItem[];
  route: string;
  slug: string[];
  title: string;
};

export type DocSectionItem = {
  excerpt: string;
  route: string;
  slug: string[];
  title: string;
  type: "page" | "section";
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
    type: "page",
    content,
    excerpt,
    route: slug.length === 0 ? "/docs" : `/docs/${slug.join("/")}`,
    slug,
    sourcePath,
    title
  };
}

export async function getDocSectionBySlug(slug: string[]): Promise<DocSection | null> {
  const entries = await getAllDocEntries();
  return entries.find((entry): entry is DocSection => entry.type === "section" && sameSlug(entry.slug, slug)) ?? null;
}

export async function getDocEntryBySlug(slug: string[]) {
  return (await getDocBySlug(slug)) ?? (await getDocSectionBySlug(slug));
}

export async function getAllDocSlugs() {
  const entries = await getAllDocEntries();
  return entries.map((entry) => entry.slug);
}

async function getAllDocEntries(): Promise<Array<DocPage | DocSection>> {
  const files = await listMarkdownFiles(docsRoot);
  const fileSlugs = files.map(markdownFileToSlug);
  const directorySlugs = await listDirectorySlugs(docsRoot);
  const pages = (await Promise.all(dedupeSlugs(fileSlugs).map((slug) => getDocBySlug(slug)))).filter(
    (entry): entry is DocPage => Boolean(entry)
  );
  const pageKeys = new Set(pages.map((page) => page.slug.join("/")));
  const sectionSlugs = directorySlugs.filter((slug) => slug.length > 0 && !pageKeys.has(slug.join("/")));
  const sections: DocSection[] = sectionSlugs.map((slug) => ({
    type: "section",
    excerpt: `Browse every Capybara AI documentation page under ${titleFromSlug(slug.at(-1) ?? "section")}.`,
    items: [],
    route: `/docs/${slug.join("/")}`,
    slug,
    title: titleFromSlug(slug.at(-1) ?? "Documentation")
  }));
  const entries: Array<DocPage | DocSection> = [...pages, ...sections].sort((left, right) =>
    left.slug.join("/").localeCompare(right.slug.join("/"))
  );

  for (const section of sections) {
    section.items = entries
      .filter((entry) => isDescendant(entry.slug, section.slug))
      .map((entry) => ({
        excerpt: entry.excerpt,
        route: entry.route,
        slug: entry.slug,
        title: entry.title,
        type: entry.type
      }));
  }

  return entries;
}

export async function getDocsTree(): Promise<DocTree> {
  const entries = await getAllDocEntries();
  const byKey = new Map(
    entries.map((entry) => [
      entry.slug.join("/"),
      {
        children: [] as DocTreeItem[],
        route: entry.route,
        slug: entry.slug,
        title: entry.title
      }
    ])
  );

  const roots: DocTreeItem[] = [];

  for (const item of byKey.values()) {
    const parentKey = item.slug.slice(0, -1).join("/");
    const parent = item.slug.length > 0 ? byKey.get(parentKey) : null;
    if (parent) {
      parent.children.push(item);
    } else {
      roots.push(item);
    }
  }

  const sortItems = (items: DocTreeItem[]) => {
    items.sort((left, right) => left.slug.length - right.slug.length || left.title.localeCompare(right.title));
    items.forEach((item) => sortItems(item.children));
  };
  sortItems(roots);

  return { items: roots };
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

async function listDirectorySlugs(directory: string): Promise<string[][]> {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(
    entries.map(async (entry) => {
      if (!entry.isDirectory()) {
        return [];
      }
      const fullPath = path.join(directory, entry.name);
      return [directoryToSlug(fullPath), ...(await listDirectorySlugs(fullPath))];
    })
  );
  return nested.flat();
}

function markdownFileToSlug(file: string) {
  const relative = path.relative(docsRoot, file).replaceAll(path.sep, "/");
  if (relative === "index.md") {
    return [];
  }
  return relative.replace(/(^|\/)index\.md$/, "$1").replace(/\.md$/, "").replace(/\/$/, "").split("/").filter(Boolean);
}

function directoryToSlug(directory: string) {
  return path.relative(docsRoot, directory).replaceAll(path.sep, "/").split("/").filter(Boolean);
}

function dedupeSlugs(slugs: string[][]) {
  const seen = new Set<string>();
  return slugs.filter((slug) => {
    const key = slug.join("/");
    if (seen.has(key)) {
      return false;
    }
    seen.add(key);
    return true;
  });
}

function isDescendant(slug: string[], ancestor: string[]) {
  return slug.length > ancestor.length && ancestor.every((part, index) => slug[index] === part);
}

function sameSlug(left: string[], right: string[]) {
  return left.length === right.length && left.every((part, index) => part === right[index]);
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
