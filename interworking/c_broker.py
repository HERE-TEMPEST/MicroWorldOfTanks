import socket
import threading

from .queue import DuplexQueue
from logger import LoggerService

class ICMessageBroker:
  def __init__(self, hostname, port, queue: DuplexQueue):
    self.hostname = hostname #"192.168.43.39"
    self.port = port
    self.__status_connected = True
    self.__listener_messages: threading.Thread = None
    self.__sender_messages: threading.Thread = None
    self.__tcpSocket: socket.socket = None
    self.__queue: DuplexQueue = queue

  def get_status(self):
    return self.__status_connected

  def __recvMessages(self):
    while self.__status_connected:
      try:
        recvData = self.__tcpSocket.recv(1024)
        if len(recvData) == 0:
          ##LoggerService.warr("SOCKET", "server is closed")
          self.close()
          break
        self.__queue.push_in_wait(recvData)
        #LoggerService.info("SOCKET", "received message from server")
      except ConnectionResetError:
        self.close()       
      except socket.timeout:
        pass
      except BaseException:
        pass

  def __sendMessages(self):
    while self.__status_connected:
      try:
        message = self.__queue.shift_out()
        if message is not None and len(message) != 0:
          self.__tcpSocket.send(message)
      except BaseException:
        pass

  def start(self):
    try:
      self.__tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.__tcpSocket.settimeout(1)
      self.__tcpSocket.connect((self.hostname, self.port))
      #LoggerService.info("SOCKET", f"Socket is listening on {self.hostname}")
      
      self.__listener_messages = threading.Thread(target=self.__recvMessages)
      self.__sender_messages = threading.Thread(target=self.__sendMessages)
      
      self.__listener_messages.start()
      self.__sender_messages.start()
    except BaseException:
      raise f"Address not found"


  def join(self):
    self.__sender_messages.join()
    self.__listener_messages.join()


  def close(self):
    try:
      self.__status_connected = False
      #self.__tcpSocket.shutdown(socket.SHUT_RDWR)
      self.__tcpSocket.detach()
      self.__tcpSocket.close()
      self.join() 
    except EOFError:
      self.join()

  def emit(self, command):
    if command == "exit":
      self.close()