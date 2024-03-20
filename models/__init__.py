from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage = None
if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
``
