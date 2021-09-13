from flask_script import Manager,Server
from app import create_app

app = create_app('dev')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    '''Run unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(debug=True,port=8000)
