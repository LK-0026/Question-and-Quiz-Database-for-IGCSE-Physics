from ._anvil_designer import AddingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Adding(AddingTemplate):
  def __init__(self, topicChosen,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.topicChosen = topicChosen
    self.correctAnswer = None
    # Any code you write here will run before the form opens
    self.label_topic.text = topicChosen
    self.subtopics = anvil.server.call('getSubtopics')
    self.drop_down_subtopics.items = [""] + self.subtopics[topicChosen]

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Homepage.Topics.Questions', topicChosen = self.topicChosen)

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

  def button_addQuestion_click(self, **event_args):
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
      alert("The following field(s) must be filled before a question can be added:\n" + missingFields)
    else:
      app_tables.questions.add_row(topic = self.topicChosen,subtopic = self.drop_down_subtopics.selected_value, )
