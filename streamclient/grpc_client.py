from __future__ import print_function
import logging
import redis
import grpc

import tweets_pb2
import tweets_pb2_grpc
conn = redis.Redis('redis-service')

def run():
    with grpc.insecure_channel('grpc-server:50051') as channel:
        stub = tweets_pb2_grpc.MessageSenderStub(channel)
        total_length = 0        
        for response in stub.SendMessage(tweets_pb2.ResponseMessage()):
            response_array = eval(response.message)         
            total_length += len(response.message)
            conn.hmset(response_array[1], {"tweet" : str(response_array), "data": total_length})        
            print("real-time character count: " + str(total_length))
            print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
