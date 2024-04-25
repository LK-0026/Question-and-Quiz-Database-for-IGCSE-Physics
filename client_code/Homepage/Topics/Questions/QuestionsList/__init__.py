from ._anvil_designer import QuestionsListTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class QuestionsList(QuestionsListTemplate):
  def __init__(self, **properties):
    #Setting up the values that are going to be displayed
    self.init_components(**properties)
    self.label_topic.text = "Topic: " + self.item['topic']
    self.label_subtopic.text = "Subtopic: " + self.item['subtopic']
    self.label_questionText.text = self.item['text']
    if self.item['image'] != None:
      self.image_question.visible = True
      self.image_question.source = self.item['image']
    self.label_option1.text = self.item['option1']
    self.label_option2.text = self.item['option2']
    self.label_option3.text = self.item['option3']
    self.label_option4.text = self.item['option4']
    
    #Highlights the option that is correct green
    if self.item['correctAnswer'] == 'option1':
      self.label_option1.background = '#83f28f'
    elif self.item['correctAnswer'] == 'option2':
      self.label_option2.background = '#83f28f'
    elif self.item['correctAnswer'] == 'option3':
      self.label_option3.background = '#83f28f'
    elif self.item['correctAnswer'] == 'option4':
      self.label_option4.background = '#83f28f'


    #Adjusts the label of the question if the question has or not been used in a quiz before
    if self.item['isUsed']:
      self.label_used.text = "❌ HAS been used"
      self.label_used.foreground = '#FF0000'
    else:
      self.label_used.text = "✅ NOT been used"
      self.label_used.foreground = '#00FF00'

  #Deletes the question from the 'question' database
  #Function is called when button is clicked
  def button_deleteQuestion_click(self, **event_args):
    #User is asked for confirmation whether they want to delete the question
    c = confirm("Are you sure you want to delete this Question?")
    if c:
      #Deletes the question from the question Bank and database itself
      self.item.delete()
      self.remove_from_parent()

  #Edits the detail of the question
  #Function is called when button is clicked
  def button_editQuestion_click(self, **event_args):
    #Opens a form which displays all the data of the selected question 
    questionID = self.item.get_id()
    open_form('Homepage.Topics.Questions.QuestionsList.EditingQuestions', 
              topic = self.item['topic'], 
              subtopic = self.item['subtopic'], 
              questionText = self.item['text'], 
              image = self.item['image'], 
              option1 = self.item['option1'],
              option2 = self.item['option2'],
              option3 = self.item['option3'],
              option4 = self.item['option4'],
              correctAnswer = self.item['correctAnswer'],
              questionID = questionID)