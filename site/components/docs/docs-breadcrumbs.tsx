import Link from "next/link";

export function DocsBreadcrumbs({ path }: { path: string }) {
  const parts = path.replace(/^\/docs\/?/, "").split("/").filter(Boolean);

  return (
    <nav className="breadcrumbs" aria-label="Breadcrumbs">
      <Link href="/">Home</Link>
      <span>/</span>
      <Link href="/docs">Docs</Link>
      {parts.map((part, index) => {
        const href = `/docs/${parts.slice(0, index + 1).join("/")}`;
        const label = titleize(part);
        const last = index === parts.length - 1;
        return (
          <span key={href} className="breadcrumb-tail">
            <span>/</span>
            {last ? <span>{label}</span> : <Link href={href}>{label}</Link>}
          </span>
        );
      })}
    </nav>
  );
}

function titleize(value: string) {
  return value
    .split("-")
    .map((word) => word.slice(0, 1).toUpperCase() + word.slice(1))
    .join(" ");
}
