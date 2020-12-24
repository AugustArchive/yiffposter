FROM python:3.6-alpine

LABEL MAINTAINER="August <august@augu.dev>"
COPY . .
RUN pip --version
RUN pip install -U -r requirements.txt

CMD ["python", "run.py"]
