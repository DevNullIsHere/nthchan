#!/usr/bin/env python
# coding: utf8

### �������� s2ch.
### ������ ���������� ���������.

## �������
import SocketServer
import time
import struct
import Queue
import thread
from random import randint as rnd
nodeid = struct.pack("I", rnd(0, 2**32-1))

from s2ch.core import *
