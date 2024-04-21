from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """Returns the list of City objects linked to this State."""
        # Assuming all_objects belongs to the storage and holds all objects
        return [city for city in all_objects.values() if city.__class__ == City and city.state_id == self.id]    
