from ._anvil_designer import TopicsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from Questions import Questions

class Topics(TopicsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    #List which contains all the topics in the Question Bank
    self.topics = ["Motion, forces and energy", "Thermal physics", "Waves", "Electricity and magnetism","Nuclear physics","Space physics"]
    #The drop down box contains
    self.topics_list.items = self.topics

  #Function that opens the previous form
  def back_button_click(self, **event_args):
    open_form('Homepage')

  
  def enter_click(self, **event_args):
    open_form('Homepage.Topics.Questions', topicChosen = self.topics_list.selected_value)
    
    



  
