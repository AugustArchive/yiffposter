FROM alpine:latest

LABEL MAINTAINER="August <august@augu.dev>"
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add --update --no-cache python3-dev

RUN apk add --no-cache bluez-dev \
	bzip2-dev \
	coreutils \
	dpkg-dev dpkg \
	expat-dev \
	findutils \
	gcc \
	gdbm-dev \
	libc-dev \
	libffi-dev \
	libnsl-dev \
	libtirpc-dev \
	linux-headers \
	make \
	ncurses-dev \
	openssl-dev \
	pax-utils \
	readline-dev \
	sqlite-dev \
	tcl-dev \
	tk \
	tk-dev \
	util-linux-dev \
	xz-dev \
	zlib-dev

WORKDIR /opt/autoyiffer
COPY . .
RUN pip --version
RUN pip install -U -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
