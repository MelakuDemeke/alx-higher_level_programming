#!/usr/bin/python3
"""
This script establishes a connection to a MySQL database
and creates a table based on the State model.
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db_url = 'mysql+mysqldb://{username}:{password}@localhost/{dbname}'.format(
        username=db_username,
        password=db_password,
        dbname=db_name
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
