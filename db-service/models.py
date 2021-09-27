from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

#TEST TABLES THAT WILL BE REPLACED BY DYNAMIC CLASS GENERATION

class Datasets(Base):
    __tablename__ = "dataset_table"
    id = Column(Integer, primary_key=True, index=True)
    checksum = Column(String)
    url = Column(String)
    evaluation = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def json(self):
        return {
            'id': self.id,
            'checksum': self.checksum,
            'url' : self.url,
            'evaluation' : self.evaluation,
            'time_created' : self.time_created,
            'time_updated' : self.time_updated
        }
