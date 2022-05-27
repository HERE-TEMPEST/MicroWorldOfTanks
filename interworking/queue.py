import multiprocessing

class DuplexQueue:

  def __init__(self):
    self.__input_queue = multiprocessing.Queue()
    self.__output_queue = multiprocessing.Queue()

      # work with input
  def shift_in_wait(self):
    return self.__input_queue.get(block=True)

  def shift_in(self):
    try:
      return self.__input_queue.get(block=False)
    except BaseException:
      return None

  def push_in_wait(self, value):
    self.__input_queue.put(obj=value, block=True)

  def push_in(self, value):
    try:
      self.__input_queue.put(obj=value, block=False)
    except BaseException:
      pass

    
      # work with output
  def shift_out_wait(self):
    return self.__output_queue.get(block=True)

  def shift_out(self):
    try:
      return self.__output_queue.get(block=True, timeout=0.5)
    except BaseException:
      return None

  def push_out_wait(self, value):
    self.__output_queue.put(obj=value, block=True)

  def push_out(self, value):
    try:
      self.__output_queue.put(obj=value, block=False)
    except BaseException:
      pass


  def close(self):
    self.__input_queue.close()
    self.__output_queue.close()

  def __del__(self):
    self.__input_queue.close()
    self.__output_queue.close()