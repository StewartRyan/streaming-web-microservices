FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install grpcio
RUN pip install grpcio-tools

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "grpc_server.py" ]
