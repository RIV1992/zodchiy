export function Button({ children, onClick }) {
  return <button className="action action--compact" onClick={onClick}>{children}</button>;
}
