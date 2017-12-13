""" To do By Brandon - Let me know when you are finished!
HINT: You should do the Matrix File first, because you need that file to do this file"""

import socket
import time
import Matrix

def print_state(state):
  print(state)
  
def mysend(s, msg):
    s.connect(('127.0.0.1',8000))
    Matrix
    s.send(msg.encode('utf-8'))
  
def myrecv(s):
    data=s.recv(1024)
    return data
  
def text_proc(text, user):
