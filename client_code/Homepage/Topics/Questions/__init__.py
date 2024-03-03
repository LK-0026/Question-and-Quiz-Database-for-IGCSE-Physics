from ._anvil_designer import QuestionsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

class Questions(QuestionsTemplate):
  def __init__(self, topicChosen, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_title.text = topicChosen
    self.repeating_panel_1.items = app_tables.questions.search(topic = topicChosen)
    '''
    self.subtopics = {'Motion, forces and energy': ['Motion','Energy, work and power'],
                      'Thermal physics':[],
                      'Waves':['Sound'],
                      'Electricity and magnetism':[],
                      'Nuclear physics':[],
                    'Space physics':[]}
    '''
    self.subtopics = anvil.server.call('getSubtopics')
    self.drop_down_subtopics.items = ['All'] + self.subtopics[topicChosen]
    self.topicChosen = topicChosen
    
    # Any code you write here will run before the form opens.
  def back_button_click(self, **event_args):
    open_form('Homepage.Topics')

  def drop_down_subtopics_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_subtopics.selected_value == 'All':
      self.repeating_panel_1.items = app_tables.questions.search(topic = self.topicChosen)
    else:
      self.repeating_panel_1.items = app_tables.questions.search(topic = self.topicChosen, subtopic = self.drop_down_subtopics.selected_value)

  def button_addSubtopic_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.subtopics[self.topicChosen].append(self.text_box_addSubtopic.text)
