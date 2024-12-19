from sqlalchemy import select
from sqlalchemy.orm import Session

from db import (
    Base,
    engine
)

from db import Association

# create sqlite database as defined in db.py
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


with Session(engine) as session:
    # insert Association violating Foreign Key constraints
    with session.begin():
        a = Association(parent_id=1, child_id=1, extra_data="TEST-01")
        session.add(a)

    # extract newly created Association
    with session.begin():
        result = session.execute(
            select(Association)
        ).scalars().all()

        for assoc in result:
            print(assoc)



