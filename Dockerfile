# Python runtime based on Debian 12
FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1\
    DJANGO_SETTINGS_MODULE=config.settings.dev

# Install required packages for Python, uv, Django and Wagtail
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install tailwindcss and uv
RUN curl -LsSfo /usr/bin/tailwindcss \
    https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
    && chmod +x /usr/bin/tailwindcss
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to the path
ENV PATH="/root/.local/bin:$PATH"

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Install requirements project
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY . .

# Add virtual environment to path so you can use python
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["honcho", "start"]
