from concurrent import futures
import logging
import csv

import grpc

import tweets_pb2
import tweets_pb2_grpc

import time

class MessageSender(tweets_pb2_grpc.MessageSenderServicer):
    def SendMessage(self, request, context):        
        with open('tweets.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                time.sleep(2)            
                yield tweets_pb2.RequestMessage(message=str(row))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tweets_pb2_grpc.add_MessageSenderServicer_to_server(MessageSender(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
