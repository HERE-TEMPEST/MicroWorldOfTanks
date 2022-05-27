from typing import List
import xml.sax
from xml.dom import minidom

from rating.filesystem.reader import RatingDTO 


class XmlRatingWriter:
  class XmlWriter:
      def __init__(self):
          pass
        
      def update_sourse(self, data: List[RatingDTO], path):
        root = minidom.Document()
        xml = root.createElement('ratings') 
        root.appendChild(xml)
        for i in data:
          rating_child = root.createElement('rating')
          rating_child.setAttribute('name', i.name)
          xml.appendChild(rating_child)

          score_child = root.createElement('score')
          rating_child.appendChild(score_child)
          date_text = root.createTextNode(str(i.score))
          score_child.appendChild(date_text)

        xml_str = root.toprettyxml(indent ="\t") 

        try:
          f = open(path, "w", encoding='utf-8')
        except FileNotFoundError:
          print(f"file {path} is created")
        
        f = open(path, "w", encoding='utf-8')
        f.write(xml_str)

  def __init__(self):
    self.writer = XmlRatingWriter.XmlWriter()

  def update_source(self, source, data):
    self.writer.update_sourse(data, source)