import { Button } from './Button';

export function Reservation({ pending, createReservation }) {
  return <Button disabled={pending} onClick={createReservation}>Забронировать</Button>;
}
