from ._anvil_designer import Motion_Forces_and_EnergyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Motion_Forces_and_Energy(Motion_Forces_and_EnergyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def back_button_click(self, **event_args):
    open_form('Homepage.Topics')