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
    #Sets the items of the dropdown box to the list of topics
    self.topics_list.items = self.topics

  #Opens the previous when button is clicked
  def back_button_click(self, **event_args):
    open_form('Homepage')

  #Opens the tab which contains all the question from the specific topics
  #A parameter which contains the selected topic from the dropdown box is passed into the next form
  def enter_click(self, **event_args):
    open_form('Homepage.Topics.Questions', topicChosen = self.topics_list.selected_value)
    
    



  
