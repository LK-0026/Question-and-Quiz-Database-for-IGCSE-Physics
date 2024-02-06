from ._anvil_designer import Nuclear_physicsTemplate
from anvil import *
import anvil.server

class Nuclear_physics(Nuclear_physicsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def back_button_click(self, **event_args):
    open_form('Homepage.Topics')
