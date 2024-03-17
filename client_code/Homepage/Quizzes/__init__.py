from ._anvil_designer import QuizzesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Quizzes(QuizzesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_quizzesList.items = app_tables.quizzes.search()

  #Goes back to the previous form
  def back_button_click(self, **event_args):
    open_form('Homepage')

  #Searches for quizzes 
  def text_box_searchQuiz_pressed_enter(self, **event_args):
    rowsFound = []
    for row in app_tables.quizzes.search():
      if self.text_box_searchQuiz.text.lower() in row['quizName'].lower():
        rowsFound.append(row)
    
    if len(rowsFound) == 0:
      self.label_noResults.visible = True
    else:
      self.label_noResults.visible = False
    self.repeating_panel_quizzesList.items = rowsFound
        
