class Request:
  def __init__(self, id, body: bytes):
    self.id = id
    self.body = body


class Response:
  def __init__(self, id, body: bytes):
    self.id = id
    self.body = body