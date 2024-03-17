from ._anvil_designer import EnterQuizNameTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from Questions import Questions

class EnterQuizName(EnterQuizNameTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  #Opens the previous form when button is clicked
  def back_button_click(self, **event_args):
    open_form('Homepage.Quizzes')

  #Opens the tab which contains all the question from the specific topics
  #A parameter which contains the selected topic from the dropdown box is passed into the next form
  def enter_click(self, **event_args):
    open_form('Homepage.Quizzes.EnterQuizName.MakingQuiz', quizName = self.text_box_quizName)

