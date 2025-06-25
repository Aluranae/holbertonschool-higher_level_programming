#!/usr/bin/python3
"""Script that updates the name of the State object
with id = 2 to 'New Mexico'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the SQLAlchemy engine connected to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Initialize a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the State object with id = 2 from the database
    state = session.query(State).filter(State.id == 2).first()

    # If the State exists, update its name and commit the change
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    # Close the session to release resources
    session.close()
