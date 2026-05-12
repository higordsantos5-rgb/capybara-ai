import Link from "next/link";

import type { DocTree, DocTreeItem } from "@/lib/docs";

type DocsSidebarProps = {
  currentPath: string;
  tree: DocTree;
};

const groupLabels: Record<string, string> = {
  "getting-started": "Getting Started",
  guides: "Guides",
  reference: "Reference",
  internal: "Internal / Audit"
};

export function DocsSidebar({ tree, currentPath }: DocsSidebarProps) {
  const grouped = groupTree(tree.items);

  return (
    <nav className="docs-sidebar" aria-label="Documentation navigation">
      {grouped.map((group) => (
        <section key={group.label}>
          <h2>{group.label}</h2>
          <ul>
            {group.items.map((item) => (
              <SidebarItem key={item.route} item={item} currentPath={currentPath} />
            ))}
          </ul>
        </section>
      ))}
    </nav>
  );
}

function SidebarItem({ item, currentPath }: { item: DocTreeItem; currentPath: string }) {
  const active = item.route === currentPath;

  return (
    <li>
      <Link aria-current={active ? "page" : undefined} href={item.route}>
        {item.title}
      </Link>
      {item.children.length > 0 ? (
        <ul>
          {item.children.map((child) => (
            <SidebarItem key={child.route} item={child} currentPath={currentPath} />
          ))}
        </ul>
      ) : null}
    </li>
  );
}

function groupTree(items: DocTreeItem[]) {
  const topLevel = items.filter((item) => item.route !== "/docs");
  const groups = ["getting-started", "guides", "reference", "internal"].map((slug) => ({
    label: groupLabels[slug],
    items: topLevel.filter((item) => item.slug[0] === slug)
  }));

  const overview = items.find((item) => item.route === "/docs");
  const other = topLevel.filter((item) => !groupLabels[item.slug[0]]);

  return [
    ...(overview ? [{ label: "Overview", items: [overview] }] : []),
    ...groups.filter((group) => group.items.length > 0),
    ...(other.length > 0 ? [{ label: "More", items: other }] : [])
  ];
}
