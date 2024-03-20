from ._anvil_designer import MakingQuizTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MakingQuiz(MakingQuizTemplate):
  def __init__(self, quizName,**properties):
    self.init_components(**properties)
    self.quizName = self.label_quizName.text = quizName
    self.topics = ["Motion, forces and energy", "Thermal physics", "Waves", "Electricity and magnetism","Nuclear physics","Space physics"]
    #Sets the items of the dropdown box to the list of topics
    self.drop_down_topicsList.items = ["All"] + self.topics
    self.repeating_panel_questionsList.items = app_tables.questions.search()
    
    #List of questions that are saved for the quiz
    self.savedQuestions = set()

  def drop_down_topicsList_change(self, **event_args):
    if self.drop_down_topicsList.selected_value == "All":
      self.drop_down_subtopicsList.items = []  
    else:
      #Assigns a dictionary of the topic name as the key and a list of subtopics as the value
      self.subtopics = anvil.server.call('getSubtopics')
      #Sets the values of the dropdown boxes to contain the list of subtopics that will be filtered
      topicChosen = self.drop_down_topicsList.selected_value
      self.drop_down_subtopicsList.items = ["All"] + self.subtopics[topicChosen]

  def button_applyFilter_click(self, **event_args):
    if 

  def button_viewAll_click(self, **event_args):
    self.repeating_panel_questionsList.items = app_tables.questions.search()
    self.button_addQuiz.visible = False
    self.card_filter.visible = True
  
  def button_viewSaved_click(self, **event_args):
    self.repeating_panel_questionsList.items = self.savedQuestions
    self.button_addQuiz.visible = True
    self.card_filter.visible = False

  def button_addQuiz_click(self, **event_args):
    app_tables.quizzes.add_row(quizName = self.quizName, questionsIncluded = list(self.savedQuestions))
    for question in self.savedQuestions:
      question['isUsed'] = True
    alert("Quiz has successfully been added")
    open_form("Homepage.Quizzes")

  #Opens the Previous Form
  def back_button_click(self, **event_args):
    open_form("Homepage.Quizzes.EnterQuizName")