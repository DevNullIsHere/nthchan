#!/usr/bin/python
# coding: cp1251

### Прототип 

## Импорты
import SocketServer
import time
import struct
import Queue
import thread

## Глобальные, лол, переменные
requests = Queue.Queue(512)

#
class s2chServerHandler(SocketServer.BaseRequestHandler):
    def push_request(self, data, socket, addr):
        reqnumber, reqtype = struct.unpack("II", data[:8])
        reqraw = data[8:]
        req = {"id": reqnumber, "type": reqtype, "data": reqraw, "remote": addr}
        requests.put(req)

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        self.push_request(data, socket, self.client_address)

def start_server():
    HOST, PORT = "localhost", 9999
    server = SocketServer.UDPServer((HOST, PORT), s2chServerHandler)
    server.serve_forever()

thread.start_new_thread(start_server)
