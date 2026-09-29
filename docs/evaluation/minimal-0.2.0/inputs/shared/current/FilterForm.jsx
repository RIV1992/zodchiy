import { Button } from './Button';

export function FilterForm({ apply, reset }) {
  return <form onSubmit={apply}>
    <label>Название <input name="search" /></label>
    <Button type="button" onClick={reset}>Сбросить</Button>
    <Button type="submit">Применить</Button>
  </form>;
}
