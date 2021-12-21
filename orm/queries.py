from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Fish, FishMonthAvailability

engine = create_engine('sqlite:///acnh', echo=True)

# create a session
Session = sessionmaker(bind = engine)
session = Session()

# select all from fish table and the months that fish is available
result = session.query(Fish).all() #.join(FishMonthAvailability)

# display each fish and list of months it is available
for row in result:
    print(row) # repr in Fish handles how this should be printed
