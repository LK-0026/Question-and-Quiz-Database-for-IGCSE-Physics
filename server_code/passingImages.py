import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


#Http API to pass the image 
@anvil.server.http_endpoint('/images/:id')
def getImage(id):
    print(f"Request was made for image with id {id}")
    imageRow = app_tables.questions.get_by_id(id)
    image = imageRow['image']
    return image

#Creates a url of the image that is publicly accesible
@anvil.server.callable()
def getImageUrl(id):
    return f"{anvil.server.get_api_origin()}/images/{id}"