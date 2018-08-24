from office365api import Calendar
#from dotenv import load_dotenv
from os.path import join, dirname, normpath
from os import environ

#dot_env_path = normpath(join(dirname(__file__), '../', '.env'))
#load_dotenv(dot_env_path)

def simplest(auth):
    cal = Calendar(auth=auth)
    cals = cal.get_all_calendars()
    print(cals)
    print(cal.calendar)
    e = cal.calendar.get_events()
    print('simplest {count}'.format(count=(len(e))))
    for event in e:
        print(event.Subject)


if __name__ == '__main__':
    authorization = (environ.get('OFFICE_USER'), environ.get('OFFICE_USER_PASSWORD'))
    simplest(authorization)

