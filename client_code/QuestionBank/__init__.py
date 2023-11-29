from ._anvil_designer import QuestionBankTemplate
from anvil import *

class QuestionBank(QuestionBankTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
