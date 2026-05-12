type CodeBlockProps = {
  code: string;
  compact?: boolean;
  language: string;
};

export function CodeBlock({ code, compact = false, language }: CodeBlockProps) {
  return (
    <div className={compact ? "code-block code-block-compact" : "code-block"}>
      <div className="code-block-top">
        <span>{language}</span>
      </div>
      <pre>
        <code>{code}</code>
      </pre>
    </div>
  );
}
