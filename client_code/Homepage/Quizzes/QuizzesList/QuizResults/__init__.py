from ._anvil_designer import QuizResultsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class QuizResults(QuizResultsTemplate):
  def __init__(self, quizID, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.quizRow = app_tables.quizzes.get_by_id(quizID)
    resultsID = self.quizRow['results'].get_id()
    self.resultRow = app_tables.results.get_by_id(resultsID)
    
    self.label_title.text = self.quizRow['quizName'] + " Results"
    if self.resultRow['averageScore'] != None:
      self.text_box_avgScore.text = str(self.resultRow['averageScore'])
    self.repeating_panel_freqWrongQuestions.items = self.resultRow['freqWrongQuestions']
    if self.resultRow['freqWrongQuestions'] == None or len(self.resultRow['freqWrongQuestions']) == 0:
      self.label_noQuestions.visible = True
    
  def button_saveAvgScore_click(self, **event_args):
    if self.text_box_avgScore.text == "":
      alert("You cannot add an empty score")
    elif int(self.text_box_avgScore.text) < 0 or int(self.text_box_avgScore.text) > 100:
      alert("The average score must lie between 0 - 100")
    else:
      alert("Average score has been saved")
      self.resultRow['averageScore'] = int(self.text_box_avgScore.text)

  def back_button_click(self, **event_args):
    open_form("Homepage.Quizzes")

  def button_editFreqWrongQues_click(self, **event_args):
    open_form("Homepage.Quizzes.QuizzesList.QuizResults.EditFreqWrongQuestions", quizRow = self.quizRow, resultRow = self.resultRow)