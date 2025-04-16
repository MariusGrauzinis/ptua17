from sqlalchemy.orm import sessionmaker

from models import Child, Parent, engine, Base

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

# Create

child = Child(name="John", surname="Smith", school="School No.1")
child2 = Child(name="Jane", surname="Smith", school="School No.2")

parent = Parent(name="Naujas", surname="Smith")
parent2 = Parent(name="Naujas2", surname="Smith")

parent.children.append(child)
parent.children.append(child2)

child.parents.append(parent2)
parent2.children.append(child2)

session.add(parent)
session.add(parent2)
session.commit()