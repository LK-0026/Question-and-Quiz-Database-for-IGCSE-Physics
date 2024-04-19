from ._anvil_designer import EditingAndViewingQuizTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EditingAndViewingQuiz(EditingAndViewingQuizTemplate):
  def __init__(self, quizName, savedQuestions, quizID, **properties):
    self.init_components(**properties)
    self.quizID = quizID
    
    #Sets the textbox above to show the quiz name which can be updated
    self.quizName = self.textBox_quizName.text = quizName

    #List of questions that are saved for the quiz
    self.savedQuestions = set(savedQuestions)
    
    self.topics = ["Motion, forces and energy", "Thermal physics", "Waves", "Electricity and magnetism","Nuclear physics","Space physics"]
    
    #Sets the items of the dropdown box to the list of topics
    self.drop_down_topicsList.items = ["All"] + self.topics
    self.repeating_panel_questionsList.items = self.savedQuestions

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
    
    #Hides the save quiz button
    self.button_saveQuiz.visible = False
    
    #Shows the filter selection
    self.card_filter.visible = True
  
  #View all the saved questions to be added to the quiz
  def button_viewSaved_click(self, **event_args):
    #All the questions displayed are in the set which contains the questions to be added to the quiz
    self.repeating_panel_questionsList.items = self.savedQuestions

    #Shows the save quiz button
    self.button_saveQuiz.visible = True

    #Hides filter selection
    self.card_filter.visible = False

  #Button to save any changes to the quiz
  def button_saveQuiz_click(self, **event_args):
    #Prevents the user from giving an empty name for the quiz
    if self.textBox_quizName.text == "":
      alert("You must put a name for this quiz")
    #Prevents the user from leaving a quiz with zero questions
    elif len(self.savedQuestions) == 0:
      alert("You cannot make a quiz with zero questions")
    #Updates all of the changes to the quiz and stores them in the data table
    else:
      quizToEdit = app_tables.quizzes.get_by_id(self.quizID)
      quizToEdit['quizName'] = self.textBox_quizName.text
      quizToEdit['questionsIncluded'] = list(self.savedQuestions)
      alert("Quiz has successfully been saved")

      #Goes back to the form containing all the quizzes
      open_form("Homepage.Quizzes")

  #Opens the previous form
  def back_button_click(self, **event_args):
    open_form('Homepage.Quizzes')
