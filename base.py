from sqla_wrapper import SQLAlchemy

# db = SQLAlchemy(dialect='sqlite', name='localhost.sqlite')
db = SQLAlchemy("sqlite:///localhost.sqlite")
