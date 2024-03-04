from ._anvil_designer import AddingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Adding(AddingTemplate):
  def __init__(self, topicChosen,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.topicChosen = topicChosen
    # Any code you write here will run before the form opens.

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Homepage.Topics.Questions', topicChosen = self.topicChosen)
