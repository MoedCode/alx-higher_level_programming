#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # engine = create_engine("musql+mysqldb://{}:{}@localhost:3306/{}"
    #    .format(argv[1], argv[2], argv[3]),
    #    pool_pre_ping=True)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_list = session.query(State).order_by(State.id).first()
    if not state_list:
        print("Nothing")
    else:
        print(f"{state_list.id}: {state_list.name}")
    session.close()
