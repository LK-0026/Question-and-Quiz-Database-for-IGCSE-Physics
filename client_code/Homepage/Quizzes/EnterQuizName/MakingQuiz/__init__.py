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
    
    #Initially fills the square with all the questions in the questionbank
    self.repeating_panel_questionsList.items = app_tables.questions.search()
    
    #Collection containing a set of questions that are saved for the quiz
    self.savedQuestions = set()

  #Function that changes the value of the subtopic dropdown depending on the topic
  def drop_down_topicsList_change(self, **event_args):
    #Makes the subtopic dropdown empty if all the topics are selected
    if self.drop_down_topicsList.selected_value == "All":
      self.drop_down_subtopicsList.items = []  
    else:
      #Assigns a dictionary of the topic name as the key and a list of subtopics as the value
      self.subtopics = anvil.server.call('getSubtopics')
      #Sets the values of the dropdown boxes to contain the list of subtopics that will be filtered
      topicChosen = self.drop_down_topicsList.selected_value
      self.drop_down_subtopicsList.items = ["All"] + self.subtopics[topicChosen]

  #Button used to apply filter based on the selection of the topic, subtopic and if has been used or not
  def button_applyFilter_click(self, **event_args):
    topicChosen = self.drop_down_topicsList.selected_value
    subtopicChosen = self.drop_down_subtopicsList.selected_value

    #Filter for only if question has not been used
    if self.check_box_notBeenUsed.checked:
      #Filter if all topics are chosen
      if topicChosen == "All":
        self.repeating_panel_questionsList.items = app_tables.questions.search(isUsed=False)
      #Filter if all subtopics are chosen
      elif subtopicChosen == "All":
        self.repeating_panel_questionsList.items = app_tables.questions.search(isUsed=False, topic= topicChosen)
      #Filter if a specific subtopic is chosen
      else:
        self.repeating_panel_questionsList.items = app_tables.questions.search(isUsed=False, topic= topicChosen, subtopic= subtopicChosen)
    
    #Filter for only if question has not been used
    else:
      #Filter if all topics are chosen
      if topicChosen == "All":
        self.repeating_panel_questionsList.items = app_tables.questions.search()
      #Filter if all subtopics are chosen
      elif subtopicChosen == "All":
        self.repeating_panel_questionsList.items = app_tables.questions.search(topic= topicChosen)
      #Filter if a specific subtopic is chosen
      else:
        self.repeating_panel_questionsList.items = app_tables.questions.search(topic= topicChosen, subtopic= subtopicChosen)

    #Reveals a text which says that no questions fit the filter if no questions are displayed
    if len(self.repeating_panel_questionsList.items) == 0:
      self.label_noResults.visible = True
    else:
      self.label_noResults.visible = False
  
  #View all the questions from the question bank
  def button_viewAll_click(self, **event_args):
    #Defaults to all the questions that exist in the question bank
    self.repeating_panel_questionsList.items = app_tables.questions.search()
    
    #Hides the add quiz button
    self.button_addQuiz.visible = False
    
    #Shows the filter selection
    self.card_filter.visible = True
  
  #View all the saved questions to be added to the quiz
  def button_viewSaved_click(self, **event_args):
    #All the questions displayed are in the set which contains the questions to be added to the quiz
    self.repeating_panel_questionsList.items = self.savedQuestions

    #Shows the add quiz button
    self.button_addQuiz.visible = True

    #Hides filter selection
    self.card_filter.visible = False

  #Action for adding the quiz
  def button_addQuiz_click(self, **event_args):
    #Gives an alert if no questions has not been saved that will be added to the quiz
    if len(self.savedQuestions) == 0:
      alert("You cannot make a quiz with zero questions")
    else:
      #Creates an empty list that contains all the frequently wrong question for the Results column
      emptyResults = app_tables.results.add_row(freqWrongQuestions= [])

      #Adds the quiz to the datatable
      app_tables.quizzes.add_row(quizName = self.quizName, questionsIncluded = list(self.savedQuestions), results = emptyResults)

      #Sets every questions status that has not beed used to True
      for question in self.savedQuestions:
        question['isUsed'] = True
      alert("Quiz has successfully been added")

      #Goes back to the form containing all the quizzes
      open_form("Homepage.Quizzes")
    
  #Opens the Previous Form
  def back_button_click(self, **event_args):
    open_form("Homepage.Quizzes.EnterQuizName")


