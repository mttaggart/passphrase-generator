FROM python:alpine
MAINTAINER Michael Taggart "mtaggart@taggart-tech.com"

EXPOSE 5000

COPY ./requirements.txt /passphrase-generator/requirements.txt

WORKDIR /passphrase-generator

RUN pip3 install -r requirements.txt

COPY . /passphrase-generator

ENTRYPOINT ["python"]

CMD ["app.py"]
