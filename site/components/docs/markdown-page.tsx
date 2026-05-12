import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import { markdownLinkToRoute, type DocPage } from "@/lib/docs";

export function MarkdownPage({ doc }: { doc: DocPage }) {
  return (
    <article className="markdown">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ href = "", children }) => {
            const nextHref = markdownLinkToRoute(href, doc.sourcePath);
            const external = /^https?:\/\//.test(nextHref);
            return (
              <a href={nextHref} target={external ? "_blank" : undefined} rel={external ? "noreferrer" : undefined}>
                {children}
              </a>
            );
          }
        }}
      >
        {doc.content}
      </ReactMarkdown>
    </article>
  );
}
