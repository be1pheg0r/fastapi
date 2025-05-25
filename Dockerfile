FROM python:3.10.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* requirements.txt* ./

RUN pip install --upgrade pip && \
    if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:backend_app", "--host", "0.0.0.0", "--port", "8000"]
