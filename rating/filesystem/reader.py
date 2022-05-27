from typing import List
import xml.sax
from datetime import datetime

class RatingDTO:
  def __init__(self, name, score):
    self.name = name
    self.score = score


class XmlRatingReader:
    class Parser(xml.sax.ContentHandler):
      def __init__(self):
        self.tag = ""
        self.data = {
          "name": "",
          "score": 0,
        }
        self.ratings = list()

      # Call when an element starts
      def startElement(self, tag, attributes):
        self.tag = tag
        if tag == 'rating':
          name = attributes['name']
          self.data.update({ 'name':  name })


      # Call when an elements ends
      def endElement(self, tag):
        if self.tag == "score":
          self.ratings.append(RatingDTO(self.data["name"], self.data["score"]))
        self.tag = ""

   #   Call when a character is read
      def characters(self, content):
        if self.tag == 'score':
          self.data["score"] = int(content)

      def get_ratings(self):
        return self.ratings
    
    def __init__(self):
      self.parser = xml.sax.make_parser()
      self.parser.setFeature(xml.sax.handler.feature_namespaces,0)
      self.classParser = XmlRatingReader.Parser()
      self.parser.setContentHandler(self.classParser)
      self.list = []

    def read_from_source(self, source) -> List[RatingDTO]:
      self.classParser.ratings = list()
      self.parser.setFeature(xml.sax.handler.feature_namespaces,0)
      self.parser.parse(source)
      return self.classParser.get_ratings()