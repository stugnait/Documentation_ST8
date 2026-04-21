# ☁️ Infrastructure Specification Document (ISD)

## Стек розгортання
- **Runtime**: Docker / Kubernetes.
- **Балансувальник**: Nginx.
- **Бази даних**:
    - **PostgreSQL**: Основне сховище.
    - **Redis**: Кеш для миттєвої перевірки квитків.
- **Черги**: RabbitMQ.

## Масштабування
Налаштований **HPA (Horizontal Pod Autoscaler)**. Якщо на вході натовп і CPU бота > 70% — система автоматично піднімає нові контейнери.