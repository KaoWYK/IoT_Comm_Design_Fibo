import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import threading
from MQTT.subscriber import listen, getHistory

import grpc
from concurrent import futures
import log_pb2
import log_pb2_grpc

sub = threading.Thread(target = listen)

class LogServicer(log_pb2_grpc.LogServicer):

    def __init__(self):
        pass

    def Show(self, request, context):
        response = log_pb2.LogResponse()
        response.history.extend(getHistory())

        return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="0.0.0.0", type=str)
    parser.add_argument("--port", default=8800, type=int)
    args = vars(parser.parse_args())

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = LogServicer()
    log_pb2_grpc.add_LogServicer_to_server(servicer, server)

    sub.start()
    print( "Server Sub Started..." )

    try:
        server.add_insecure_port(f"{args['ip']}:{args['port']}")
        server.start()
        print(f"Run gRPC Server for Order-Logging at {args['ip']}:{args['port']}")
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass
