from ._anvil_designer import QuizzesListTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import anvil.js

class QuizzesList(QuizzesListTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_quizName.text = self.item['quizName']
    self.quizID = self.item.get_id()

  def button_delete_click(self, **event_args):
    c = confirm("Are you sure you want to delete  '" + self.item['quizName'] +"' ?")
    if c:
      resultsID = self.item['results'].get_id()
      resultsRow = app_tables.results.get_by_id(resultsID)
      resultsRow.delete()
      self.item.delete()
      self.remove_from_parent()

  def button_editAndView_click(self, **event_args):
    open_form('Homepage.Quizzes.QuizzesList.EditingAndViewingQuiz', quizName = self.item['quizName'], savedQuestions = self.item['questionsIncluded'], quizID = self.quizID)

  def button_createGForms_click(self, **event_args):
    anvil.google.auth.login(["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/forms.body"])
    accessToken = anvil.google.auth.get_user_access_token()
    createGFormResponse = anvil.http.request("https://forms.googleapis.com/v1/forms/",
                                  method = "POST",
                                  json = True,
                                  data = 
                                  {
                                    "info": {
                                      "title": self.item['quizName']
                                    }
                                  },
                                  headers = {
                                      'Authorization': 
                                        'Bearer ' + accessToken
                                    })
    formURL = "https://docs.google.com/forms/d/" + createGFormResponse["formId"] + "/edit"
    clickableLink = f'<a href="{formURL}">{formURL}</a>'
    alert(f"Google Form for quiz has been created, link to the Google form:\n{clickableLink}")

  def button_results_click(self, **event_args):
    open_form("Homepage.Quizzes.QuizzesList.QuizResults", quizID = self.quizID)