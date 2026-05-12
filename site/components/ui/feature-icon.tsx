const paths = [
  "M5 6h14M7 12h10M9 18h6",
  "M4 12h6l3-6 3 12 3-6h1",
  "M12 4c3 3 5 6 5 9a5 5 0 0 1-10 0c0-3 2-6 5-9Z",
  "M7 11V8a5 5 0 0 1 10 0v3M6 11h12v9H6z",
  "M6 5h12v14H6zM9 9h6M9 13h6M9 17h3",
  "M5 8l7-4 7 4v8l-7 4-7-4zM12 4v16"
];

export function FeatureIcon({ index }: { index: number }) {
  return (
    <span className="feature-icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" role="img">
        <path d={paths[index % paths.length]} />
      </svg>
    </span>
  );
}
