FROM python:3.10-alpine

RUN pip install uv

COPY . .

RUN uv sync --locked

RUN source .venv/bin/activate

CMD ["uv", "run", "python", "lichess.py"]