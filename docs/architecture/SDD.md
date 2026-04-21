# 🏗 Software Design Document (SDD)

## Архітектура
Обрано **мікросервісний підхід**, щоб бот і аналітика жили окремо і не заважали один одному.

### Компоненти:
1. **API Gateway**: Роутинг запитів.
2. **Bot Worker**: Обробка вебхуків Telegram (найшвидша частина).
3. **Analytics Engine**: Агрегація даних (асинхронно через RabbitMQ).

## Специфікація API
| Метод | Ендпоінт | Опис |
| :--- | :--- | :--- |
| `POST` | `/api/v1/tickets/generate` | Створити квиток |
| `POST` | `/api/v1/bot/webhook` | Дані від Telegram |
| `GET` | `/api/v1/analytics/live` | Стата для дашборду |