from office365api import Calendar
#from dotenv import load_dotenv
from os.path import join, dirname, normpath
from os import environ
import pytz
from datetime import date, datetime, timedelta, time

def sunday(delta=0):
    today = date.today()
    d = timedelta(days=today.isoweekday())
    sunday = today - d
    sunday += timedelta(days=(7 * delta))
    sunday = datetime.combine(sunday, time())
    return sunday.astimezone(pytz.utc)


#dot_env_path = normpath(join(dirname(__file__), '../', '.env'))
#load_dotenv(dot_env_path)

def simplest(auth):
    cal = Calendar(auth=auth)
    cals = cal.get_all_calendars()
    e = cal.calendar.get_events(start=sunday().isoformat(), end=sunday(2).isoformat())
    print('simplest {count}'.format(count=(len(e))))
    for event in e:
        print(event.Subject, event.Location, event.Start, event.End)


if __name__ == '__main__':
    authorization = (environ.get('OFFICE_USER'), environ.get('OFFICE_USER_PASSWORD'))
    simplest(authorization)

