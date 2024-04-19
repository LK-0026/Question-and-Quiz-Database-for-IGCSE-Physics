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

    #Sets the name of the title of the form
    self.label_title.text = self.quizRow['quizName'] + " Results"

    #If an average score already exists, sets the textbox to the average score of the quiz
    if self.resultRow['averageScore'] != None:
      self.text_box_avgScore.text = str(self.resultRow['averageScore'])
    
    #Sets the frequently wrong question section
    self.repeating_panel_freqWrongQuestions.items = self.resultRow['freqWrongQuestions']
    
    #If no frequently wrong questions are shown, a text saying that there are none will be shown
    if self.resultRow['freqWrongQuestions'] == None or len(self.resultRow['freqWrongQuestions']) == 0:
      self.label_noQuestions.visible = True
    
  #Action when trying to add a score
  def button_saveAvgScore_click(self, **event_args):
    #Gives an alert which prevents to user to put nothing in the textbox
    if self.text_box_avgScore.text == "":
      alert("You cannot add an empty score")
    #Gives and alert which tells user to put a score within the percentages of 0-100
    elif int(self.text_box_avgScore.text) < 0 or int(self.text_box_avgScore.text) > 100:
      alert("The average score must lie between 0 - 100")
    #Add's the score to the results data table
    else:
      alert("Average score has been saved")
      self.resultRow['averageScore'] = int(self.text_box_avgScore.text)

  #Goes back to the previous form
  def back_button_click(self, **event_args):
    open_form("Homepage.Quizzes")

  def button_editFreqWrongQues_click(self, **event_args):
    open_form("Homepage.Quizzes.QuizzesList.QuizResults.EditFreqWrongQuestions", quizRow = self.quizRow, resultRow = self.resultRow)