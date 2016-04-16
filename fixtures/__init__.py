from fixture import SQLAlchemyFixture, DataSet
from color_schemer import db
from color_schemer.models import User

dbfixture = SQLAlchemyFixture(env={'UserData': User}, engine=db.engine)


class UserData(DataSet):

    class user_1:
        email = 'user@email.com'
