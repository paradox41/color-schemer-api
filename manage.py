import logging

from flask.ext.script import Shell, Manager, Server, prompt_bool

from color_schemer import db, create_app
import color_schemer.core.models as models


log = logging.getLogger(__name__)

manager = Manager(create_app)
manager.add_command('runserver', Server())
manager.add_option('-c', '--config', dest='config',
                   default=None, required=False)


def _make_context():
    from flask import current_app

    return dict(
        app=current_app,
        drop=drop,
        create=create,
        recreate=recreate,
        populate=populate,
        **vars(models))

manager.add_command('shell', Shell(make_context=lambda: _make_context()))


@manager.command
def drop():
    """Drops database tables"""
    if prompt_bool('Are you sure you want to lose all your data'):
        db.drop_all()


@manager.command
def create(default_data=False, sample_data=False):
    """Creates database tables from sqlalchemy models"""
    db.create_all()
    if default_data or sample_data:
        populate(default_data, sample_data)


@manager.command
def recreate(default_data=False, sample_data=False):
    """Recreates database tables (same as issuing 'drop' and then 'create')"""
    drop()

    create(default_data, sample_data)


@manager.command
def populate(default_data=False, sample_data=False):
    """Populate database with default data"""
    from fixtures import dbfixture

    if default_data:
        from fixtures import UserData
        default_data = dbfixture.data(UserData)
        default_data.setup()


def main():
    manager.run()

if __name__ == '__main__':
    main()
