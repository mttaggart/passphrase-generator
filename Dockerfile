FROM ubuntu:latest
MAINTAINER Michael Taggart "mtaggart@taggart-tech.com"

EXPOSE 5000

RUN apt update && apt install -y python3-pip python3-dev python3-setuptools

COPY ./requirements.txt /passphrase-generator/requirements.txt

WORKDIR /passphrase-generator

RUN pip3 install -r requirements.txt

COPY . /passphrase-generator

ENTRYPOINT ["python3"]

CMD ["app.py"]
