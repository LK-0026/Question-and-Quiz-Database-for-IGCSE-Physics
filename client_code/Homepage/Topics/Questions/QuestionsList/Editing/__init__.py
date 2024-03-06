from ._anvil_designer import EditingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Editing(EditingTemplate):
  def __init__(self, topic, subtopic, questionText, image, option1, option2, option3, option4, correctAnswer, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.topicChosen = topic
    self.correctAnswer = correctAnswer
    # Any code you write here will run before the form opens
    self.label_topic.text = topic
    self.subtopics = anvil.server.call('getSubtopics')
    self.drop_down_subtopics.items = [""] + self.subtopics[topic]
    self.drop_down_subtopics.selected_value = subtopic
    questionTextBefore = self.text_area_questionText.text = questionText
    if image != None:
      self.image_question.source = self.file_loader_image.file
      self.image_question.visible = True
    self.text_area_questionText.text = questionText
    self.text_area_option1.text = option1
    self.text_area_option2.text = option2
    self.text_area_option3.text = option3
    self.text_area_option4.text = option4
    
    if correctAnswer == "option1":
      self.radio_button_option1.selected = True
    elif correctAnswer == "option2":
      self.radio_button_option2.selected = True
    elif correctAnswer == "option3":
      self.radio_button_option3.selected = True 
    else:
      self.radio_button_option4.selected = True 

  def file_loader_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.image_question.source = self.file_loader_image.file
    self.image_question.visible = True

  def button_removeImage_click(self, **event_args):
    self.image_question.source = None
    self.file_loader_image.clear()
    self.image_question.visible = False

  def radio_button_option1_clicked(self, **event_args):
    self.correctAnswer = "option1"

  def radio_button_option2_clicked(self, **event_args):
    self.correctAnswer = "option2"

  def radio_button_option3_clicked(self, **event_args):
    self.correctAnswer = "option3"

  def radio_button_option4_clicked(self, **event_args):
    self.correctAnswer = "option4"

  def button_saveChanges_click(self, **event_args):
    missingFields = ""
    if self.drop_down_subtopics.selected_value == "":
      missingFields += "     - Subtopic\n"
    if self.text_area_questionText.text == "":
      missingFields += "     - Question Text\n"
    if self.text_area_option1.text == "" or self.text_area_option2.text == "" or self.text_area_option3.text == "" or self.text_area_option4.text == "":
      missingFields += "     - Option(s)\n"
    if self.correctAnswer == None:
      missingFields += "     - Correct Answer"

    missingFields.strip()
    if missingFields != "":
      alert("The following field(s) must be filled before a question can be edited:\n" + missingFields)
    else:
      rowToEdit = app_tables.questions.get(text = questionTextBefore)
      rowToEdit['subtopic'] = self.drop_down_subtopics.selected_value
      rowToEdit['text'] = self.text_area_questionText.text
      rowToEdit['image'] = self.file_loader_image.file
      rowToEdit['option1'] = self.text_area_option1.text
      rowToEdit['option2'] = self.text_area_option2.text
      rowToEdit['option3'] = self.text_area_option3.text
      rowToEdit['option4'] = self.text_area_option4.text
      rowToEdit['correctAnswer'] = self.correctAnswer
      alert("Changes have been saved")
      open_form('Homepage.Topics.Questions', topicChosen = self.topicChosen)
  
  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Homepage.Topics.Questions', topicChosen = self.topicChosen)
