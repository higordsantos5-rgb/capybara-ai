import Link from "next/link";

import type { DocSection } from "@/lib/docs";

export function SectionPage({ section }: { section: DocSection }) {
  return (
    <article className="markdown section-page">
      <p className="section-kicker">Documentation section</p>
      <h1>{section.title}</h1>
      <p>{section.excerpt}</p>
      <div className="section-index" aria-label={`${section.title} pages`}>
        {section.items.map((item) => (
          <Link className="section-index-item" href={item.route} key={item.route}>
            <span>{item.title}</span>
            <small>{item.type === "section" ? "Section" : item.slug.join("/")}</small>
            <p>{item.excerpt}</p>
          </Link>
        ))}
      </div>
    </article>
  );
}
