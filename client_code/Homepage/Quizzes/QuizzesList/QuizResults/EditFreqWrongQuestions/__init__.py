from ._anvil_designer import EditFreqWrongQuestionsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EditFreqWrongQuestions(EditFreqWrongQuestionsTemplate):
  def __init__(self, quizRow, resultRow, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.quizRow = quizRow
    self.resultRow = resultRow
    self.repeating_panel_quizQuestions.items = quizRow['questionsIncluded']
    self.savedQuestions = set()
    if len(resultRow['freqWrongQuestions']) > 0:
      self.savedQuestions = set(resultRow['freqWrongQuestions'])

  def button_viewAll_click(self, **event_args):
    self.repeating_panel_quizQuestions.items = quizRow['questionsIncluded']
    self.button_saveQuiz.visible = False

  def button_viewSaved_click(self, **event_args):
     self.repeating_panel_quizQuestions.items = list(self.savedQuestions)
    self.button_saveQuiz.visible = True
  
  def button_saveQuiz_click(self, **event_args):
    self.resultRow['freqWrongQuestions'] = list(self.savedQuestions)
    open_form("Homepage.Quizzes.QuizzesList.QuizResults", quizID = self.quizRow.get_id())
  
  def back_button_click(self, **event_args):
    open_form("Homepage.Quizzes.QuizzesList.QuizResults", quizID = self.quizRow.get_id())

  

  

  
