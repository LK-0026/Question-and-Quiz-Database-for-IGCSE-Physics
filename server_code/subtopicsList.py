import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import logging

subtopicsDict = {}
for row in app_tables.subtopics.search():
  subtopics = (json.loads(row['subtopics'])).strip('[]').split(',')

  subtopicsList = None
  for subT in subtopics:
    subT.strip().strip('"')
  subtopicsDict[row['topic']] = subtopicsList
  
logging.info("Subtopics dictionary: %s", subtopicsDict)

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
  for row in app_tables.subtopics.search():
    if row['topic'] == topic:
      row['subtopics'] = json.dumps(subtopicList)
      row.save()
      break

  


