import type { ReactNode } from "react";

import { DocsBreadcrumbs } from "@/components/docs/docs-breadcrumbs";
import { DocsSidebar } from "@/components/docs/docs-sidebar";
import { DocsSearch } from "@/components/docs/docs-search";
import type { DocTree } from "@/lib/docs";

type DocsLayoutProps = {
  children: ReactNode;
  currentPath: string;
  tree: DocTree;
};

export function DocsLayout({ children, currentPath, tree }: DocsLayoutProps) {
  return (
    <div className="docs-shell">
      <aside className="docs-sidebar-wrap">
        <DocsSearch tree={tree} />
        <DocsSidebar tree={tree} currentPath={currentPath} />
      </aside>
      <div className="docs-content">
        <DocsBreadcrumbs path={currentPath} />
        {children}
      </div>
    </div>
  );
}
