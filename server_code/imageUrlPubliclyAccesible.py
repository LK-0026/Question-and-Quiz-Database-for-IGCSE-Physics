import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.http_endpoint('/get_image')
def getImage(rowID):
  questionImage = app_tables.questions.get_by_id(rowID)['image']
  return questionImage
