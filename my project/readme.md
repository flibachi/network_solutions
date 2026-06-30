# Шаблон Full Stack FastAPI

## Технологический стек и возможности

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) для бэкенд-API на Python.
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) для взаимодействия с SQL-базами данных через ORM на Python.
  - 🔍 [Pydantic](https://docs.pydantic.dev), используемый FastAPI, для валидации данных и управления настройками.
  - 💾 [PostgreSQL](https://www.postgresql.org) в качестве SQL-базы данных.
- 🚀 [React](https://react.dev) для фронтенда.
  - 💃 С использованием TypeScript, хуков, [Vite](https://vitejs.dev) и других компонентов современного фронтенд-стека.
  - 🎨 [Tailwind CSS](https://tailwindcss.com) и [shadcn/ui](https://ui.shadcn.com) для компонентов интерфейса.
  - 🤖 Автоматически генерируемый клиент для фронтенда.
  - 🧪 [Playwright](https://playwright.dev) для сквозного (End-to-End) тестирования.
  - 🦇 Поддержка тёмной темы.
- 🐋 [Docker Compose](https://www.docker.com) для разработки и промышленной эксплуатации.
- 🔒 Надёжное хеширование паролей по умолчанию.
- 🔑 Аутентификация на основе JWT (JSON Web Token).
- 📫 Восстановление пароля через электронную почту.
- 📬 [Mailcatcher](https://mailcatcher.me) для локального тестирования электронной почты в процессе разработки.
- ✅ Тесты с [Pytest](https://pytest.org).
- 📞 [Traefik](https://traefik.io) в качестве обратного прокси-сервера / балансировщика нагрузки.
- 🚢 Инструкции по развёртыванию с использованием Docker Compose, включая настройку прокси Traefik на фронтенде для автоматической обработки HTTPS-сертификатов.
- 🏭 CI (непрерывная интеграция) и CD (непрерывное развёртывание) на основе GitHub Actions.

### Панель управления — Вход

[![Документация API](img/login.png)](https://github.com/fastapi/full-stack-fastapi-template)

### Панель управления — Администратор

[![Документация API](img/dashboard.png)](https://github.com/fastapi/full-stack-fastapi-template)

### Панель управления — Элементы

[![Документация API](img/dashboard-items.png)](https://github.com/fastapi/full-stack-fastapi-template)

### Панель управления — Тёмная тема

[![Документация API](img/dashboard-dark.png)](https://github.com/fastapi/full-stack-fastapi-template)

### Интерактивная документация API

[![Документация API](img/docs.png)](https://github.com/fastapi/full-stack-fastapi-template)

## Как использовать

Вы можете **просто сделать форк или клон** этого репозитория и использовать его как есть.

✨ Всё работает из коробки. ✨

### Как использовать частный репозиторий

Если вы хотите использовать частный репозиторий, GitHub не позволит вам просто сделать форк, так как это не позволяет изменить видимость форков.

Но вы можете сделать следующее:

- Создайте новый репозиторий GitHub, например `my-full-stack`.
- Клонируйте этот репозиторий вручную, указав имя проекта, который вы хотите использовать, например `my-full-stack`:

```bash
git clone git@github.com:fastapi/full-stack-fastapi-template.git my-full-stack
```

- Перейдите в новый каталог:

```bash
cd my-full-stack
```

- Установите новый источник (origin) для вашего репозитория, скопировав его из интерфейса GitHub, например:

```bash
git remote set-url origin git@github.com:octocat/my-full-stack.git
```

- Добавьте этот репозиторий как ещё один «удалённый» (remote), чтобы в дальнейшем получать обновления:

```bash
git remote add upstream git@github.com:fastapi/full-stack-fastapi-template.git
```

- Отправьте код в ваш новый репозиторий:

```bash
git push -u origin master
```

### Обновление из исходного шаблона

После клонирования репозитория и внесения изменений вы можете захотеть получить последние изменения из этого исходного шаблона.

- Убедитесь, что вы добавили исходный репозиторий как удалённый (remote), это можно проверить с помощью:

```bash
git remote -v

origin    git@github.com:octocat/my-full-stack.git (fetch)
origin    git@github.com:octocat/my-full-stack.git (push)
upstream    git@github.com:fastapi/full-stack-fastapi-template.git (fetch)
upstream    git@github.com:fastapi/full-stack-fastapi-template.git (push)
```

- Загрузите последние изменения без слияния:

```bash
git pull --no-commit upstream master
```

Это загрузит последние изменения из этого шаблона без их фиксации, чтобы вы могли проверить, всё ли в порядке, перед фиксацией.

- Если возникли конфликты, разрешите их в вашем редакторе.

- После завершения зафиксируйте изменения:

```bash
git merge --continue
```

### Настройка

Затем вы можете обновить конфигурации в файлах `.env` для настройки ваших параметров.

Перед развёртыванием обязательно измените как минимум следующие значения:

- `SECRET_KEY`
- `FIRST_SUPERUSER_PASSWORD`
- `POSTGRES_PASSWORD`

Вы можете (и должны) передавать их как переменные окружения из секретов.

Прочитайте документацию [deployment.md](./deployment.md) для более подробной информации.

### Генерация секретных ключей

Некоторые переменные окружения в файле `.env` имеют значение по умолчанию `changethis`.

Вам необходимо заменить их на секретный ключ. Для генерации секретных ключей вы можете выполнить следующую команду:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Скопируйте содержимое и используйте его в качестве пароля или секретного ключа. Выполните команду ещё раз, чтобы сгенерировать другой надёжный ключ.

## Альтернативный способ использования — с Copier

Этот репозиторий также поддерживает генерацию нового проекта с помощью [Copier](https://copier.readthedocs.io).

Будут скопированы все файлы, заданы вопросы для настройки, а файлы `.env` обновлены в соответствии с вашими ответами.

### Установка Copier

Вы можете установить Copier с помощью:

```bash
pip install copier
```

Или, если у вас есть [`pipx`](https://pipx.pypa.io/), выполните:

```bash
pipx install copier
```

**Примечание:** Если у вас есть `pipx`, установка copier не обязательна — вы можете запустить его напрямую.

### Генерация проекта с Copier

Определите имя каталога для вашего нового проекта, которое вы будете использовать ниже. Например, `my-awesome-project`.

Перейдите в каталог, который будет родительским для вашего проекта, и выполните команду с именем вашего проекта:

```bash
copier copy https://github.com/fastapi/full-stack-fastapi-template my-awesome-project --trust
```

Если у вас есть `pipx` и вы не устанавливали `copier`, вы можете запустить его напрямую:

```bash
pipx run copier copy https://github.com/fastapi/full-stack-fastapi-template my-awesome-project --trust
```

**Примечание:** Опция `--trust` необходима для выполнения [скрипта после создания](https://github.com/fastapi/full-stack-fastapi-template/blob/master/.copier/update_dotenv.py), который обновляет ваши файлы `.env`.

### Входные переменные

Copier запросит у вас некоторые данные, желательно подготовить их заранее.

Но не волнуйтесь, вы можете обновить любые из них позже в файлах `.env`.

Входные переменные с их значениями по умолчанию (некоторые автоматически сгенерированы):

- `project_name`: (по умолчанию: `"FastAPI Project"`) Название проекта, отображаемое пользователям API (в .env).
- `stack_name`: (по умолчанию: `"fastapi-project"`) Имя стека, используемое для меток Docker Compose и имени проекта (без пробелов, без точек) (в .env).
- `secret_key`: (по умолчанию: `"changethis"`) Секретный ключ проекта, используемый для безопасности, хранится в .env. Вы можете сгенерировать его с помощью метода, описанного выше.
- `first_superuser`: (по умолчанию: `"admin@example.com"`) Электронная почта первого суперпользователя (в .env).
- `first_superuser_password`: (по умолчанию: `"changethis"`) Пароль первого суперпользователя (в .env).
- `smtp_host`: (по умолчанию: "") Хост SMTP-сервера для отправки электронных писем. Можно настроить позже в .env.
- `smtp_user`: (по умолчанию: "") Пользователь SMTP-сервера для отправки электронных писем. Можно настроить позже в .env.
- `smtp_password`: (по умолчанию: "") Пароль SMTP-сервера для отправки электронных писем. Можно настроить позже в .env.
- `emails_from_email`: (по умолчанию: `"info@example.com"`) Адрес электронной почты, с которого отправляются письма. Можно настроить позже в .env.
- `postgres_password`: (по умолчанию: `"changethis"`) Пароль для базы данных PostgreSQL, хранится в .env. Можно сгенерировать с помощью метода, описанного выше.
- `sentry_dsn`: (по умолчанию: "") DSN для Sentry, если вы используете эту систему. Можно настроить позже в .env.

## Разработка бэкенда

Документация по бэкенду: [backend/README.md](./backend/README.md).

## Разработка фронтенда

Документация по фронтенду: [frontend/README.md](./frontend/README.md).

## Развёртывание

Документация по развёртыванию: [deployment.md](./deployment.md).

## Разработка

Общая документация по разработке: [development.md](./development.md).

Она включает использование Docker Compose, пользовательских локальных доменов, конфигурации `.env` и т. д.

## Примечания к выпускам

См. файл [release-notes.md](./release-notes.md).

## Лицензия

Шаблон Full Stack FastAPI распространяется на условиях лицензии MIT.