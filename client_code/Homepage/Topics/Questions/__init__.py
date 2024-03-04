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
    self.subtopics = anvil.server.call('getSubtopics')
    self.drop_down_subtopics.items = ['All'] + self.subtopics[topicChosen]
    self.topicChosen = topicChosen
    self.drop_down_subtopicsRemoval.items = [''] + self.subtopics[topicChosen]
    
    # Any code you write here will run before the form opens.

  def drop_down_subtopics_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_subtopics.selected_value == 'All':
      self.repeating_panel_1.items = app_tables.questions.search(topic = self.topicChosen)
    else:
      self.repeating_panel_1.items = app_tables.questions.search(topic = self.topicChosen, subtopic = self.drop_down_subtopics.selected_value)

  def button_addSubtopic_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_addSubtopic.text == "":
      alert("You cannot leave this field blank")
    elif self.text_box_addSubtopic.text in self.subtopics[self.topicChosen]:
      alert("This subtopic already exists.")
    else:
      anvil.server.call('addSubtopic', self.topicChosen, self.text_box_addSubtopic.text)
      alert("The '" + self.text_box_addSubtopic.text + "' subtopic has successfully been added.")
      self.drop_down_subtopics.items += [self.text_box_addSubtopic.text]
      self.drop_down_subtopicsRemoval.items += [self.text_box_addSubtopic.text]
      self.text_box_addSubtopic.text = ''

  def button_removeSubtopic_click(self, **event_args):
    if self.drop_down_subtopicsRemoval.selected_value == '':
      alert("You have to select a subtopic before it can be removed")
    else:
      c = confirm("Do you wish to delete the '" + self.drop_down_subtopicsRemoval.selected_value + "' subtopic?")
      if c:
        anvil.server.call('removeSubtopic',self.topicChosen,self.drop_down_subtopicsRemoval.selected_value)
        self.drop_down_subtopics.items = ['All'] + self.subtopics[self.topicChosen]
        self.drop_down_subtopicsRemoval.items = [''] + self.subtopics[self.topicChosen]

  def back_button_click(self, **event_args):
    open_form('Homepage.Topics')