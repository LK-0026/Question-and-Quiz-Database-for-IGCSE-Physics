from ._anvil_designer import Motion_Forces_EnergyTemplate
from anvil import *
import anvil.server

class Motion_Forces_Energy(Motion_Forces_EnergyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
