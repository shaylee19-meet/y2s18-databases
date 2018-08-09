from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
    __tablename__="knowledge"
    knowledge_id=Column(Integer,primarykey=TRUE)
    topic=Column(String)
    title=Column(String)
    rating=Column(Integer)
    def __repr__(self):
        return ("knowledge id{}"
        "topic{}"
        "title{}".format)
        "rating{}"
        self.knowledge_id
        self.topic
        self.title
        self.rating
        first=knowledge(topic="weter", title="rainbow", rating=9)
        if first=true:
            print"(read this articl")
