from ._anvil_designer import HomepageTemplate
from anvil import *

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
  def button_question_click(self, **event_args):
    open_form('QuestionBank',y_parameter="an_argument")
