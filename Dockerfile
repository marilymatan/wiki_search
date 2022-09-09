FROM python:3.7-slim-buster

ENV key_wiki_pages="Category:Disambiguation pages"
ENV language="en"

EXPOSE 5000
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "src/main.py"]
