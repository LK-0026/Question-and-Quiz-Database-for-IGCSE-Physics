import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.http_endpoint('/image/:row_id')
def get_image(row_id, **p):
  row = app_tables.questions.get_by_id(row_id)
  return row['image']