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
    
    #Initilizes the set which contains all the frequently wrong questions
    
    #Creates an empty set if there are no frequently wrong questions in the results
    if len(resultRow['freqWrongQuestions']) == 0:
      self.savedQuestions = set()
    #Otherwise the set contains all the frequently wrong questions in the results
    else:
      self.savedQuestions = set(resultRow['freqWrongQuestions'])

  #Views all of the questions in the quiz
  def button_viewAll_click(self, **event_args):
    #Sets the section to show all the questions in the quiz
    self.repeating_panel_quizQuestions.items = quizRow['questionsIncluded']

    #Hides the save results button
    self.button_saveResults.visible = False

  #Views all of the frequently wrong questions
  def button_viewSaved_click(self, **event_args):
    #Sets the section to show all the questions that are frequently wrong
    self.repeating_panel_quizQuestions.items = list(self.savedQuestions)

    #Shows the save results button
    self.button_saveResults.visible = True

  #Save results of the frequently wrong questions
  def button_saveResults_click(self, **event_args):
    self.resultRow['freqWrongQuestions'] = list(self.savedQuestions)
    open_form("Homepage.Quizzes.QuizzesList.QuizResults", quizID = self.quizRow.get_id())
  
  #Goes back to previous form
  def back_button_click(self, **event_args):
    open_form("Homepage.Quizzes.QuizzesList.QuizResults", quizID = self.quizRow.get_id())