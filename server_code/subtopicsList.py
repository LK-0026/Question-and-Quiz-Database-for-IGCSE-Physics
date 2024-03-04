import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

subtopicsDict = {}
for row in app_tables.subtopics.search():
  subtopicsList = json.loads(row['subtopics'])
  subtopicsDict[row['topic']] = subtopicsList
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def getSubtopics():
  return subtopicsDict

@anvil.server.callable
def addSubtopic(topic, newSubtopic):
  subtopicList = subtopicsDict[topic]
  subtopicList.append(newSubtopic)
  app_tables.subtopics.get(topic = topic)['subtopics'] = json.dumps(subtopicList)
  
@anvil.server.callable
def removeSubtopic(topic, removedSubtopic):
  subtopicList = subtopicsDict[topic]
  subtopicList.remove(removedSubtopic)
  app_tables.subtopics.get(topic = topic)['subtopics'] = json.dumps(subtopicList)