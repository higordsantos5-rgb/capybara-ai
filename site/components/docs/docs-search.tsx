"use client";

import Link from "next/link";
import { useMemo, useState } from "react";

import type { DocTree } from "@/lib/docs";

export function DocsSearch({ tree }: { tree: DocTree }) {
  const [query, setQuery] = useState("");
  const items = useMemo(() => flatten(tree), [tree]);
  const results = query.trim()
    ? items.filter((item) => item.title.toLowerCase().includes(query.trim().toLowerCase())).slice(0, 6)
    : [];

  return (
    <div className="docs-search">
      <label htmlFor="docs-search">Search docs</label>
      <input
        id="docs-search"
        type="search"
        placeholder="Search pages"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      {results.length > 0 ? (
        <ul>
          {results.map((item) => (
            <li key={item.route}>
              <Link href={item.route}>{item.title}</Link>
            </li>
          ))}
        </ul>
      ) : null}
    </div>
  );
}

function flatten(tree: DocTree) {
  const output: Array<{ route: string; title: string }> = [];
  const visit = (items: DocTree["items"]) => {
    for (const item of items) {
      output.push({ route: item.route, title: item.title });
      visit(item.children);
    }
  };
  visit(tree.items);
  return output;
}
