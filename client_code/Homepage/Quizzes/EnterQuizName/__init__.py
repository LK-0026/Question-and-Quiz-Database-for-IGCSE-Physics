from ._anvil_designer import EnterQuizNameTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class EnterQuizName(EnterQuizNameTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  #Opens the tab which contains all the question in the database to be added into a quizzes
  #A parameter which contains the quiz name from the text box is passed into the next form
  def enter_click(self, **event_args):
    #Gives na alert if the user does't provide any data in the textbox
    if self.text_box_quizName.text == "":
      alert("You have to give a name for this quiz.")
    else:
      open_form('Homepage.Quizzes.EnterQuizName.MakingQuiz', quizName = self.text_box_quizName.text)

  #Opens the previous form when button is clicked
  def back_button_click(self, **event_args):
    open_form('Homepage.Quizzes')
