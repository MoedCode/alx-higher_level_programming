#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Creating the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating the tables
    Base.metadata.create_all(engine)

    # Using the session in a with statement
    with Session(engine) as session:
        # Querying and printing data
        states = session.query(State).order_by(State.id).all()
        for each_state in states:
            print("{}: {}".format(each_state.id, each_state.name))
