from ._anvil_designer import TopicsTemplate
from anvil import *
import anvil.server

class Topics(TopicsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    option = None

    # Any code you write here will run before the form opens.
    self.topics = ["Motion, Forces and Energy", "Thermal physics", "Waves", "Electricity and magnetism","Nuclear physics","Space physics"]
    self.topics_list.items = self.topics
  def back_button_click(self, **event_args):
    open_form('Homepage')

  def topics_list_change(self, **event_args):
    """This method is called when an item is selected"""
    option = self.topics_list.selected_value

  def enter_click(self, **event_args):
    option = self.topics_list.selected_value
    if option == "Motion, Forces and Energy":
      open_form('Homepage.Topics.Motion_Forces_and_Energy')
    elif option == "Thermal physics":
      open_form('Homepage.Topics.Thermal_physics')
    elif option == "Waves":
      open_form('Homepage.Topics.Waves')
    elif option == "Electricity and magnetism":
      open_form('Homepage.Topics.Electricity_and_Magnetism')
    elif option == "Nuclear physics":
      open_form('Homepage.Topics.Nuclear_physics')
    elif option == "Space physics":
      open_form('Homepage.Topics.Space_physics')



  
