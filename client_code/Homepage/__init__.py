from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  #Opens the Question Bank section of the program
  def button_question_click(self, **event_args):
    open_form('Homepage.Topics')

  #Opens the Quiz Bank section of the program
  def button_quiz_click(self, **event_args):
    open_form('Homepage.Quizzes')
