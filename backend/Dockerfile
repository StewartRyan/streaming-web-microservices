FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install grpcio
RUN pip install grpcio-tools

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "greeter_server.py" ]

# python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. helloworld.proto
