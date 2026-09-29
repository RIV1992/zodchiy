// Один оператор имеет одинаковые права из каталога и из истории.
// title и id поступают из общего хранилища. route — текущий URL.
export const sidebar = [
  { label: 'Главная', href: '/' },
  { label: 'Приборы', href: '/help/equipment' },
  { label: 'История', href: '/history' },
];

export function catalogLink(item, route) {
  return `/items/${item.id}?returnTo=${encodeURIComponent(route)}`;
}

export function historyLink(item) {
  return `/history/items/${item.id}`;
}

export const routes = {
  '/': { title: 'Обзор', links: ['/history'] },
  '/help/equipment': { title: 'О приборах', body: 'Здесь описаны правила проката.', links: [] },
  '/catalog': { title: 'Приборы', query: ['search', 'page'], cardLink: catalogLink },
  '/items/:id': { entity: 'equipment', view: 'detail', actions: ['reserve'], back: '/catalog' },
  '/history': { title: 'История', cardLink: historyLink },
  '/history/items/:id': { entity: 'equipment', view: 'summary', actions: [], back: '/history' },
};

export function reserve(itemId) {
  return { itemId, status: 'reserved' };
}
