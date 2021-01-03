FROM python:3.6-alpine

LABEL MAINTAINER="August <august@augu.dev>"
COPY . .

RUN apk add gcc
RUN pip --version
RUN pip install -U -r requirements.txt

CMD ["python", "run.py"]
