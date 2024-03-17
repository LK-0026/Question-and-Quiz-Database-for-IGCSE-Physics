from ._anvil_designer import MakingQuizTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MakingQuiz(MakingQuizTemplate):
  def __init__(self, **properties):
    self.init_components(quizName, **properties)
    self.quizName = self.label_quizName.text = quizName
    self.topics = ["Motion, forces and energy", "Thermal physics", "Waves", "Electricity and magnetism","Nuclear physics","Space physics"]
    #Sets the items of the dropdown box to the list of topics
    self.drop_down_topicsList.items = ["All"] + self.topics

    self.

    if self.drop_down_topicsList.selected_value == "All":
      self.drop_down_topicsList.items = []
      self.repeati
    else:
      subtopics = 
      
