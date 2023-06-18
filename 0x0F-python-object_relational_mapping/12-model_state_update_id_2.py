#!/usr/bin/python3
"""
This script updates the State object with the given ID
in the database to have a new name.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    uri = 'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    db_url = uri.format(
        username=db_username,
        password=db_password,
        dbname=db_name
    )

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
