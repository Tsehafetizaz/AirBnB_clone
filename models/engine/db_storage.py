from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        # Break the line to avoid exceeding 79 characters
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        pass  # Add a pass or proper implementation here

    def new(self, obj):
        pass  # Add a pass or proper implementation here

    def save(self):
        pass  # Add a pass or proper implementation here

    def delete(self, obj=None):
        pass  # Add a pass or proper implementation here

    def reload(self):
        pass  # Add a pass or proper implementation here

    def close(self):
        """Releases resources associated with the current database session."""
        self.__session.close()
