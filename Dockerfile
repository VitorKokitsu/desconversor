FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN groupadd user && useradd user -m -g user

USER user

WORKDIR /app

COPY src pyproject.toml uv.lock /app/

RUN uv sync --locked --no-dev

ENTRYPOINT ["uv", "run", "--no-sync", "main.py"]
