from ._anvil_designer import QuestionsListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class QuestionsList(QuestionsListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_subtopic.text = "Subtopic: "+ self.item['subtopic']
    self.label_questionText.text = self.item['text']
    if self.item['image'] != None:
      self.image_question.visible = True
      self.image_question.source = self.item['image']
    self.label_option1.text = self.item['option1']
    self.label_option2.text = self.item['option2']
    self.label_option3.text = self.item['option3']
    self.label_option4.text = self.item['option4']
    if self.item['correctAnswer'] == 'option1':
      self.label_option1.background = '#83f28f'
    elif self.item['correctAnswer'] == 'option2':
      self.label_option2.background = '#83f28f'
    elif self.item['correctAnswer'] == 'option3':
      self.label_option3.background = '#83f28f'
    elif self.item['correctAnswer'] == 'option4':
      self.label_option4.background = '#83f28f'

    self.label_used
    # Any code you write here will run before the form opens.

  def button_deleteQuestion_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Are you sure you want to delete this Question?")
    if c:
      self.item.delete()
      self.remove_from_parent()

  def button_editQuestion_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Homepage.Topics.Questions.QuestionsList.Editing', 
              topic = self.item['topic'], 
              subtopic = self.item['subtopic'], 
              questionText = self.item['text'], 
              image = self.item['image'], 
              option1 = self.item['option1'],
              option2 = self.item['option2'],
              option3 = self.item['option3'],
              option4 = self.item['option4'],
              correctAnswer = self.item['correctAnswer'])
  
