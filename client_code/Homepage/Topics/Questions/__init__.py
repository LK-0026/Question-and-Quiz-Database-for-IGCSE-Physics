from ._anvil_designer import QuestionsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Questions(QuestionsTemplate):
  def __init__(self, topic,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.title.text = topic

    # Any code you write here will run before the form opens.
  def back_button_click(self, **event_args):
    open_form('Homepage.Topics')