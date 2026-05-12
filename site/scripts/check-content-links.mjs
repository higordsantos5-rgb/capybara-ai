import { promises as fs } from "node:fs";
import path from "node:path";

const projectRoot = path.resolve(process.cwd(), "..");
const docsRoot = path.join(projectRoot, "docs");
const markdownFiles = [path.join(projectRoot, "README.md"), ...(await listMarkdownFiles(docsRoot))];
const linkPattern = /\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)/g;
const broken = [];

for (const file of markdownFiles) {
  const content = await fs.readFile(file, "utf8");
  for (const match of content.matchAll(linkPattern)) {
    const rawHref = match[1];
    if (/^https?:\/\//.test(rawHref)) {
      continue;
    }

    const [target] = rawHref.split("#");
    const resolved = path.resolve(path.dirname(file), target);
    try {
      await fs.access(resolved);
    } catch {
      broken.push(`${path.relative(projectRoot, file)} -> ${rawHref}`);
    }
  }
}

if (broken.length > 0) {
  console.error("Broken markdown links:");
  for (const item of broken) {
    console.error(`- ${item}`);
  }
  process.exit(1);
}

async function listMarkdownFiles(directory) {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const files = await Promise.all(
    entries.map(async (entry) => {
      const fullPath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        return listMarkdownFiles(fullPath);
      }
      return entry.isFile() && entry.name.endsWith(".md") ? [fullPath] : [];
    })
  );
  return files.flat();
}
