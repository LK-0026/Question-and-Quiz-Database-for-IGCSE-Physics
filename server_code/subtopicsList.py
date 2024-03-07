import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

#Creates a dictionary by using the the topic name as the key and a list of subtopics as the value
subtopicsDict = {}
for row in app_tables.subtopics.search():
  #Uses the .loads method json library to convert a string containing a list to a list
  subtopicsList = json.loads(row['subtopics'])
  subtopicsDict[row['topic']] = subtopicsList

#Returns the dictionary of subtopics
@anvil.server.callable
def getSubtopics():
  return subtopicsDict

#Adds a subtopic to the subtopic list(value) that corresponds to the topic(key)
@anvil.server.callable
def addSubtopic(topic, newSubtopic):
  #Finds the list of subtopic that relates to the topic
  subtopicList = subtopicsDict[topic]
  #Adds the new subtopic to the list
  subtopicList.append(newSubtopic)
  #Edits the value of the subtopic table with the new list
  #The row is found by finding the topic which corresponds to the subtopics
  #Uses the .dumps from the json library to convert list to a string containing that list
  app_tables.subtopics.get(topic = topic)['subtopics'] = json.dumps(subtopicList)
  
#Removes a subtopic to the subtopic list(value) that corresponds to the topic(key)
@anvil.server.callable
def removeSubtopic(topic, removedSubtopic):
  #Finds the list of subtopic that relates to the topic
  subtopicList = subtopicsDict[topic]
  #Removes subtopic from the list
  subtopicList.remove(removedSubtopic)
  #Edits the value of the subtopic table with the new list
  #The row is found by finding the topic which corresponds to the subtopics
  #Uses the .dumps from the json library to convert list to a string containing that list
  app_tables.subtopics.get(topic = topic)['subtopics'] = json.dumps(subtopicList)