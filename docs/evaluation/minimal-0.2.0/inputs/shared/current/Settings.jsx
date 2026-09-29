import { Button } from './Button';

export function Settings({ openHelp }) {
  return <Button onClick={openHelp}><svg aria-hidden="true"><path d="M1 1h4v4H1z" /></svg></Button>;
}
