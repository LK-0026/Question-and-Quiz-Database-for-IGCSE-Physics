from ._anvil_designer import QuestionsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

class Questions(QuestionsTemplate):
  def __init__(self, topicChosen, **properties):
    self.init_components(**properties)
    self.topicChosen = topicChosen
    
    #Sets the tile of the page to the topic selected from the dropdown list from the previous form
    self.label_title.text = topicChosen
    
    #Form initially opens with all the question from the selected topic
    #A search is done from the 'question' database to get all the questions with the selected topic
    #Repeating panel loops through each data that will be displayed from database
    self.repeating_panel_questionsList.items = app_tables.questions.search(topic = topicChosen)
    
    #Assigns a dictionary of the topic name as the key and a list of subtopics as the value
    self.subtopics = anvil.server.call('getSubtopics')
    
    #Sets the values of the dropdown boxes to contain the list of subtopics that will be filtered or removed
    self.drop_down_subtopics.items = ['All'] + self.subtopics[topicChosen]
    self.drop_down_subtopicsRemoval.items = [''] + self.subtopics[topicChosen]
    
  #Filters the questions displayed by their subtopic
  #Method is called when an item is selected
  def drop_down_subtopics_change(self, **event_args):
    #Shows all of the question if the "All" option is selected
    if self.drop_down_subtopics.selected_value == 'All':
      self.repeating_panel_questionsList.items = app_tables.questions.search(topic = self.topicChosen)
    #Searches from the 'question' database the questions with the selected subtopic from the dropdown box 
    else:
      self.repeating_panel_questionsList.items = app_tables.questions.search(topic = self.topicChosen, subtopic = self.drop_down_subtopics.selected_value)

  #Adds a subtopic to the current list of subtopics
  #Method is called when the button is clicked
  def button_addSubtopic_click(self, **event_args):
    #Gives an alert which prevents the user from entering a new subtopic when nothing is in the text box
    if self.text_box_addSubtopic.text == "":
      alert("You cannot leave this field blank")
    #Gives an alert which prevents the user from adding an existing subtopic
    elif self.text_box_addSubtopic.text in self.subtopics[self.topicChosen]:
      alert("This subtopic already exists.")
    else:
      #Calls the 'addSubtopic' function to add the new subtopic to the 'subtopic' database and gives an alert
      anvil.server.call('addSubtopic', self.topicChosen, self.text_box_addSubtopic.text)
      alert("The '" + self.text_box_addSubtopic.text + "' subtopic has successfully been added.")

      #Updates the addition to the other dropdown boxes without refreshing
      self.drop_down_subtopics.items += [self.text_box_addSubtopic.text]
      self.drop_down_subtopicsRemoval.items += [self.text_box_addSubtopic.text]
      
      #Empties out the text of the textbox
      self.text_box_addSubtopic.text = ''

  #Removes a subtopic to the current list of subtopics
  #Method is called when the button is clicked
  def button_removeSubtopic_click(self, **event_args):
    #When no subtopic is selected gives an alert
    if self.drop_down_subtopicsRemoval.selected_value == '':
      alert("You have to select a subtopic before it can be removed")
    else:
      #Asks the user to make sure if they delete the subtopic which returns a True or False value depending on their answer
      c = confirm("Do you wish to delete the '" + self.drop_down_subtopicsRemoval.selected_value + "' subtopic?")
      if c:
        #Calls the 'removeSubtopic' function to delete the subtopic to the 'subtopic' database and gives an alert
        anvil.server.call('removeSubtopic',self.topicChosen,self.drop_down_subtopicsRemoval.selected_value)
        alert("The '" + self.drop_down_subtopicsRemoval.selected_value + "' subtopic has deleted.")
       #Updates the removal to the other dropdown boxes without refreshing
        self.drop_down_subtopics.items = ['All'] + self.subtopics[self.topicChosen]
        self.drop_down_subtopicsRemoval.items = [''] + self.subtopics[self.topicChosen]

  #Leads to another form which allows the user to add a question
  #Method is called when the button is clicked
  def outlined_button_manualAdd_click(self, **event_args):
    open_form('Homepage.Topics.Questions.Adding', topicChosen = self.topicChosen)
  
  #Opens the previous form when button is clicked
  def back_button_click(self, **event_args):
    open_form('Homepage.Topics')