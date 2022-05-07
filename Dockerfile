FROM --platform=linux/amd64 python:3

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

CMD ["python", "./bot.py"]