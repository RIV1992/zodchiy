export function Button({ children, disabled = false, type = 'button', onClick }) {
  return <button className="action" disabled={disabled} type={type} onClick={onClick}>{children}</button>;
}
