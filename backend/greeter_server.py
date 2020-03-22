from concurrent import futures
import logging
import csv

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

import time

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):        
        with open('tweets.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                time.sleep(2)            
                yield helloworld_pb2.HelloReply(message=str(row))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

# python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto
