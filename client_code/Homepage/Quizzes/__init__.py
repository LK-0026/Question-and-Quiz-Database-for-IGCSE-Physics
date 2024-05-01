from ._anvil_designer import QuizzesTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
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
    #Stores all the quizzes that matches with the search 
    rowsFound = []

    #Does a Linear search for the quizzes based on the input
    for row in app_tables.quizzes.search():
      if self.text_box_searchQuiz.text.lower() in row['quizName'].lower():
        rowsFound.append(row)

    #Displays the all the quizzes based on the search
    self.repeating_panel_quizzesList.items = rowsFound
    
    #Displays a text depending or not if quizzes are found with the search 
    if len(rowsFound) == 0:
      self.label_noResults.visible = True
    else:
      self.label_noResults.visible = False
    

  #Goes to the form to enter the name of a new quiz
  def button_newQuiz_click(self, **event_args):
    open_form('Homepage.Quizzes.EnterQuizName')