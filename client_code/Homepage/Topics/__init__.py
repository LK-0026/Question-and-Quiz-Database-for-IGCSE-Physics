from ._anvil_designer import TopicsTemplate
from anvil import *

class Topics(TopicsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def back_button_click(self, **event_args):
    open_form('Homepage')
