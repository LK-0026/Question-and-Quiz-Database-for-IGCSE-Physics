import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pytesseract
from PIL import Image

@anvil.server.callable
def imageToText(uploaded):  
    image = Image.open(uploaded)