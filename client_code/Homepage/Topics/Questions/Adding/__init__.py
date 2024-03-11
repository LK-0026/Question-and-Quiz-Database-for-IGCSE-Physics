from ._anvil_designer import AddingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Adding(AddingTemplate):
  def __init__(self, topicChosen,**properties):
    self.init_components(**properties)
    self.topicChosen = topicChosen
    self.correctAnswer = None
    self.label_topic.text = topicChosen
    self.subtopics = anvil.server.call('getSubtopics')
    self.drop_down_subtopics.items = [""] + self.subtopics[topicChosen]

  def file_loader_OCR_change(self, file, **event_args):
    imgOCR = self.file_loader_OCR
    self.text_area_OCR = anvil.server.call('imageToText', imgOCR)
  
  #When an image is uploaded, the image will be shown
  def file_loader_image_change(self, file, **event_args):
    self.image_question.source = self.file_loader_image.file
    self.image_question.visible = True

  #The image will be removed when the button is clicked
  def button_removeImage_click(self, **event_args):
    self.image_question.source = None
    self.file_loader_image.clear()
    self.image_question.visible = False

  #Functions below set's the correct answer to 1 of the 4 options
  def radio_button_option1_clicked(self, **event_args):
    self.correctAnswer = "option1"

  def radio_button_option2_clicked(self, **event_args):
    self.correctAnswer = "option2"

  def radio_button_option3_clicked(self, **event_args):
    self.correctAnswer = "option3"

  def radio_button_option4_clicked(self, **event_args):
    self.correctAnswer = "option4"

  #Adds a question to the 'question' database when button is clicked and goes back to the form shoing all the questions
  def button_addQuestion_click(self, **event_args):
    #Creates a string that will be used as an alert if any of the fields are missing
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

    #If there are any missing fields when adding the question, an alert will pop up telling the user fields aren't filled yet
    if missingFields != "":
      alert("The following field(s) must be filled before a question can be added:\n" + missingFields)
    #Adds a question to the 'question' database based on the fields entered
    else:
      app_tables.questions.add_row(
        topic = self.topicChosen,
        subtopic = self.drop_down_subtopics.selected_value,
        text = self.text_area_questionText.text,
        image = self.file_loader_image.file,
        option1 = self.text_area_option1.text,
        option2 = self.text_area_option2.text,
        option3 = self.text_area_option3.text,
        option4 = self.text_area_option4.text,
        correctAnswer = self.correctAnswer,
        isUsed = False)
      alert("Question has succesfully been added.")

      #Goes back to the form showing all the question
      open_form('Homepage.Topics.Questions', topicChosen = self.topicChosen)
  
  #Goes back to the previous form when clicked
  def back_button_click(self, **event_args):
    open_form('Homepage.Topics.Questions', topicChosen = self.topicChosen)


