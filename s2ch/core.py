#!/usr/bin/env python
# coding: utf8

import socket


class BaseCodec:
    def encode(data):
        return data
    
    def decode(data):
        return data

class Node:
    def __init__(self, addr, mport, aport):
        self.addr = addr
        self.mport = mport
        self.aport = aport
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(0)
        self.codec = BaseCodec()
    
    def send(self, data):
        self.sock.send_to(self.codec.encode(data) (self.addr, self.mport))


class s2chNetClient:
    def __init__(self):
        self.neighbours = []
    
    def send_to(self, data, nodeid):
        for neighbour in self.neighbours:
            if neighbour.nodeid == nodeid:
                neighbour.send(data)
                break
    
    def broadcast(self, data):
        for neighbour in self.neighbours:
            neighbour.send_to(data)


class s2chNetServerHandler(SocketServer.BaseRequestHandler):
    def push_request(self, data, socket, addr):        
        reqnumber, reqtype = struct.unpack("II", data[:8])
        reqraw = data[8:]
        req = {"id": reqnumber, "type": reqtype, "data": reqraw, "remote": addr}
        requests.put(req)

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        self.push_request(data, socket, self.client_address)
        

class Request:
    def set(self, id, type, data):
        self.id = id
        self.type = type
        self.data = data
    
    def set_from_raw(self, rawdata):
        pass
    
    def get_raw(self):
        pass

class Responce:
    def set(self, id, data):
        self.id = id
        self.data = data
    
    def set_from_raw(self, rawdata):
        pass
    
    def get_raw(self):
        pass

class RequestSeries:
    def __init__():
        self.requests = []
    
    def add_request(self, request):
        self.requests.append(request)
    
    def get_raw(self):
        pass
    
    def set_from_raw(self, rawdata):
        pass
    
    def generate_responce_series(self, callback):
        pass

class ResponceSeries:
    def __init__():
        self.responces = []
    
    def add_responce(self, responce):
        self.responces.append(responce)
    
    def get_raw(self):
        pass
    
    def set_from_raw(self, rawdata):
        pass
    
class ReqStorage:
    def __init__(self):
        self.requests = {}
        self.monitors = {}
    
    def add_request(self, request):
        pass
    
    def add_responce(self, responce):
        pass
    
    def watch(self, rid, callback):
        pass