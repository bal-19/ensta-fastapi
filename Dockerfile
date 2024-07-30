FROM python:3.10.14-bookworm

WORKDIR /app

COPY . /app

RUN python -m venv venv

RUN . venv/bin/activate && pip install -r requirements.txt

EXPOSE 1903

CMD [ "/app/venv/bin/python", "main.py" ]