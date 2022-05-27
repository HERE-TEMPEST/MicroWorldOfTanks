from .rating_model import RatingModel
from .file_handler import FileHandler
from .filesystem import XmlRatingWriter, XmlRatingReader

reader = XmlRatingReader()
writer = XmlRatingWriter()
filehandler = FileHandler(reader, writer)
modelRatings = RatingModel(filehandler)
modelRatings.open_file("./ratings.xml")


