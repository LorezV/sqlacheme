from flask import request, render_template, url_for, Flask
import sys
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = '21'
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

    col1 = User()
    col1.surname = 'Derkach'
    col1.name = 'Dima'
    col1.age = '23'
    col1.position = 'polomoishik'
    col1.speciality = 'research engineer'
    col1.address = 'module_1'
    col1.email = 'scott12_chief@mars.org'

    col2 = User()
    col2.surname = 'Kaha'
    col2.name = 'Sergo'
    col2.age = '26'
    col2.position = 'polomoishik'
    col2.speciality = 'research engineer'
    col2.address = 'module_1'
    col2.email = 'scott_33chief@mars.org'
    
    col3 = User()
    col3.surname = 'Alex'
    col3.name = 'Boiko'
    col3.age = '21'
    col3.position = 'pilot'
    col3.speciality = 'research engineer'
    col3.address = 'module_1'
    col3.email = 'scott_chie22f@mars.org'

    job1 = Jobs()
    job1.team_leader = 1
    job1.job = 'deployment of residential modules 1 and 2'
    job1.work_size = 15
    job1.collaborators = '2, 3'

    session.add(user)
    session.add(col1)
    session.add(col2)
    session.add(col3)
    session.add(job1)
    session.commit()

    app.run(port=8080, host='127.0.0.1')

if __name__ == "__main__":
    sys.exit(main())
