from ._anvil_designer import QuizzesListTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import webbrowser
import anvil.media
from anvil.js import window

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
    createGFormResponse = anvil.http.request("https://forms.googleapis.com/v1/forms/", method = "POST", json = True,
                          data = 
                          {
                            "info": {
                              "title": self.item['quizName']
                            }
                          },
                          headers = {'Authorization': 'Bearer ' + accessToken})
    
    formID = createGFormResponse["formId"]
    
    anvil.http.request(f"https://forms.googleapis.com/v1/forms/{formID}:batchUpdate", method = "POST", json = True,
                      data = 
                       {
                        "requests": [
                          {
                            "updateSettings": {
                              "settings": {
                                "quizSettings": {
                                  "isQuiz": True
                                }
                              },
                            "updateMask": "quizSettings.isQuiz"
                            }
                          }
                        ]
                      },
                      headers = {'Authorization': 'Bearer ' + accessToken})
    for i in range(len(self.item['questionsIncluded'])):
      question = self.item['questionsIncluded'][i]
      correctAnsValue = question[question['correctAnswer']]
      print("Text:",question['text'])
      print("Option1:",question['option1'])
      print("Option2:",question['option2'])
      print("Option3:",question['option3'])
      print("Option4:",question['option4'])
      print("Correct Ans:",correctAnsValue)
      if question['image'] != None:
        questionId = question.get_id
        print(imageUrl)
        anvil.http.request(f"https://forms.googleapis.com/v1/forms/{formID}:batchUpdate", method = "POST", json = True,
                           data = 
                        {
                          "requests": [
                            {
                              "createItem": {
                                "item": {
                                  "title": question['text'],
                                  "imageItem": {
                                    "image": {
                                      "sourceUri": str(imageUrl)
                                    }
                                  },
                                  "questionItem": {
                                    "question": {
                                      "required": True,
                                      "grading": {
                                        "correctAnswers": {
                                          "answers": [
                                            {
                                              "value": correctAnsValue
                                            }
                                            
                                          ]
                                        },
                                        "pointValue": 1
                                        
                                      },
                                      "choiceQuestion": {
                                        "shuffle": True,
                                        "type": "RADIO",
                                        "options": [
                                          {
                                            "value": question["option1"]
                                            
                                          },
                                          {
                                            "value": question['option2']
                                            
                                          },
                                          {
                                            "value": question['option3']
                                            
                                          },
                                          {
                                            "value": question['option4']
                                            
                                          }
                                          
                                        ]
                                      }
                                      
                                    }
                                    
                                  }
                                  
                                },
                                "location": {
                                  "index": i
                                }
                              }
                              
                            }
                            
                          ]
                          
                        },
                        headers = {'Authorization': 'Bearer ' + accessToken})
      else:
        anvil.http.request(f"https://forms.googleapis.com/v1/forms/{formID}:batchUpdate", method = "POST", json = True,
                           data = 
                        {
                          "requests": [
                            {
                              "createItem": {
                                "item": {
                                  "title": question['text'],
                                  "questionItem": {
                                    "question": {
                                      "required": True,
                                      "grading": {
                                        "correctAnswers": {
                                          "answers": [
                                            {
                                              "value": correctAnsValue
                                            }
                                            
                                          ]
                                        },
                                        "pointValue": 1
                                        
                                      },
                                      "choiceQuestion": {
                                        "shuffle": True,
                                        "type": "RADIO",
                                        "options": [
                                          {
                                            "value": question["option1"]
                                            
                                          },
                                          {
                                            "value": question['option2']
                                            
                                          },
                                          {
                                            "value": question['option3']
                                            
                                          },
                                          {
                                            "value": question['option4']
                                            
                                          }
                                          
                                        ]
                                      }
                                      
                                    }
                                    
                                  }
                                  
                                },
                                "location": {
                                  "index": i
                                }
                              }
                              
                            }
                            
                          ]
                          
                        },
                        headers = {'Authorization': 'Bearer ' + accessToken})
    formURL = f"https://docs.google.com/forms/d/{formID}/edit"
    webbrowser.open(formURL)
    alert("Google Form for quiz has been created. If you have not been redirected, open google drive")

  def button_results_click(self, **event_args):
    open_form("Homepage.Quizzes.QuizzesList.QuizResults", quizID = self.quizID)