import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
#import pytesseract

@anvil.server.callable
def imageToText(uploaded):  
  configOCR = r'--oem 3 --psm 6'
  textOCR = pytesseract.image_to_string(uplaaded, config=configOCR)
  return textOCR