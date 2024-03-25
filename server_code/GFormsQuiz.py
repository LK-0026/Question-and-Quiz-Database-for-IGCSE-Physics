import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.google.auth

@anvil.server.callable
def createGFormsQuiz(quiz):
  anvil.google.auth.login(["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/forms.body"])
  accessToken = anvil.google.auth.get_user_access_token()
  createGFormResponse = anvil.http.request(
                                  url = "https://forms.googleapis.com/v1/forms",
                                  method = "POST",
                                  json = {
                                    "info": {
                                        "title": quiz['quizName']
                                    }
                                  },
                                  headers = {
                                      'Authorization': 'Bearer ' + accessToken
                            })