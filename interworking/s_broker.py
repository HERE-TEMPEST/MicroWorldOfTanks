import socket
import threading
from typing import Dict, List

from .queue import DuplexQueue
from logger import LoggerService
from protocols import Request, Response

class Connection:
  def __init__(self, id, newSocket, clientAddr):
    self.socket: socket.socket = newSocket
    self.addr = clientAddr
    self.id = id

class ISMessageBroker:
  def __init__(self, hostname, port, queue: DuplexQueue):
    self.hostname = hostname
    self.port = port
    self.__status_connected = True
    self.__connections: Dict[int, Connection] = {}
    self.__listener_connections: threading.Thread = None
    self.__listener_messages: threading.Thread = None
    self.__sender_messages: threading.Thread = None
    self.__tcpSocket: socket.socket = None
    self.__queue: DuplexQueue = queue

  def status(self):
    return self.__status_connected

  def __recvMessages(self):
    while self.status():
      try:
        for connection_id in self.__connections:
          try:
            request = self.__connections[connection_id].socket.recv(1024)
            if len(request) > 0:
              #LoggerService.info("SOCKET", f"received message from {str(self.__connections[connection_id].addr)}")
              self.__queue.push_in_wait(Request(connection_id, request))
            else:
              ##LoggerService.warr("SOCKET", f"client {str(self.__connections[connection_id].addr)} disconnected")
              self.__connections[connection_id].socket.close()
              del self.__connections[connection_id]
          except socket.timeout:
            pass
          except ConnectionResetError:
            self.__connections[connection_id].socket.close()
            del self.__connections[connection_id]
            ##LoggerService.warr("SOCKET", f"client {str(self.__connections[connection_id].addr)} disconnected")
      except RuntimeError:
        pass

  def __sendMessages(self):
    while self.status():
      try:
        message: Response = self.__queue.shift_out()
        if message is not None:
          if message.id == 999:
            for player in self.__connections:
              self.__connections[player].socket.send(message.body)
          else:
            self.__connections[message.id].socket.send(message.body)
      except BaseException:
        pass
  

  def start(self):
    self.__tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__tcpSocket.bind((self.hostname, self.port))
    self.__tcpSocket.settimeout(0.03)
    self.__tcpSocket.listen()
    LoggerService.info("SOCKET", f"Socket is listening on {self.hostname}")

    self.__listener_connections = threading.Thread(target=self.__acceptConn)
    self.__listener_messages = threading.Thread(target=self.__recvMessages)
    self.__sender_messages = threading.Thread(target=self.__sendMessages)
    
    self.__listener_connections.start()
    self.__listener_messages.start()
    self.__sender_messages.start()


  def __join(self):
    self.__listener_connections.join()
    self.__sender_messages.join()
    self.__listener_messages.join()


  def close(self):
    try:
      #LoggerService.info("SOCKET", f"Socket is closed")
      self.__status_connected = False
      #self.__tcpSocket.shutdown(socket.SHUT_RDWR)
      self.__tcpSocket.detach()
      self.__tcpSocket.close()
    except EOFError:
      self.__join()

  def __acceptConn(self):
    while self.status():
      try:
        newSocket, clientAddr = self.__tcpSocket.accept()
        if newSocket:
          newSocket.settimeout(0.01)
          newClient = Connection(id=len(self.__connections)+1, newSocket=newSocket, clientAddr=clientAddr)
          self.__connections[newClient.id] = newClient
          ##LoggerService.info(f"SOCKET", f" new user {clientAddr} has been connected.")
          ##LoggerService.info(f"SOCKET", f" active connections {len(self.__connections)}")
      except BaseException:
        pass

  def emit(self, command):
    if command == "exit":
      self.close()
