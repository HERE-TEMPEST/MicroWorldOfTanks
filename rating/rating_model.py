from datetime import datetime
from typing import List

from .filesystem.reader import RatingDTO

class RatingModel:
  def __init__(self, filehandler):
    self.filehandler = filehandler
    self.storage: List[RatingDTO] = []

  def save_file(self, source):
    try:
      self.filehandler.update_source(source, self.storage)
      return True
    except FileNotFoundError:
      return False

  def open_file(self, source):
    try:
      self.filehandler.update_resource(source)
      data: List[RatingDTO] = self.filehandler.read_from_source()
      self.storage = data
      self.storage.sort(reverse= True, key = lambda a: a.score)
      return True
    except BaseException:
      return False

  def get_ratings(self) -> List[RatingDTO]:
    return self.storage

  def append(self, name: str, score: int) -> bool:
    if name == "":
      return False
    else:
      if not self.update(name, score):
        self.storage.append(RatingDTO(name, score))
    self.storage.sort(reverse= True, key = lambda a: a.score)
    return True

  def update(self, name: str, score: int) -> bool:
    for rating in self.storage:
      if rating.name == name:
        rating.score = score
        return True
    return False
  
  def get_max(self):
    if len(self.storage) == 0:
      return -1
    return self.storage[0].score