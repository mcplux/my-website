# My website

A custom Content Manager System built with **Django** and **Wagtail** to power my personal website

## 🧱 Tech Stack

- 🐍 [Python](https://www.python.org/)
- 💚 [Django](https://www.djangoproject.com/)
- 🐦‍ [Wagtail](https://wagtail.org/)
- 🎨 [TailwindCSS](https://tailwindcss.com/)
- 🐋 [Docker](https://docs.docker.com/)

## 🏗️ Key Features

- Create & update project pages.
- Structure this projects in different pages.
- Maintain full control over content.

## 🖥️ Development Setup

1. **Clone Repository**
   ```bash
   git clone git@github.com:mcplux/my-website.git
   cd my-website
   ```
2. **Start required services (database & adminer)**
   ```bash
   docker compose up db adminer -d
   ```
   This will start:
   - `db`: PostgreSQL database.
   - `adminer`: Database UI Web.
3. **Build the web container**
   ```bash
   docker compose build web
   ```
4. **Apply database migrations**
   ```bash
   docker compose run --rm web python manage.py migrate
   ```
5. **(Optional, but recommended) Create a superuser**
   ```bash
   docker compose run --rm web python manage.py createsuperuser
   ```
   And follow instruction, then you will have access to Django admin panel.
6. **Run development server in watch mode**
   ```bash
   docker compose up web --watch
   ```
   Now the application should be running and have useful links (default):
   - **Web application**: http://localhost:8000/
   - **Admin panel**: http://localhost:8000/admin/
   - **Adminer**: http://localhost:8080
7. **You can work in you machine**
   ```bash
   uv sync
   ```

## ❤️ Author

Made for Juan Pablo Martinez (@mcplux)
