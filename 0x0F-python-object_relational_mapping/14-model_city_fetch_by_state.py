#!/usr/bin/python3
"""
Update name of state with an id of 2
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    r = session.query(State, City).join(City, State.id == City.state_id).all()
    for state, city in r:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
