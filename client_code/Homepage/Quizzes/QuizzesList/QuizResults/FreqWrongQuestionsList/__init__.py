from ._anvil_designer import FreqWrongQuestionsListTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class FreqWrongQuestionsList(FreqWrongQuestionsListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_topic.text = "Topic: " + self.item['topic']
    self.label_subtopic.text = "Subtopic: "+ self.item['subtopic']
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


