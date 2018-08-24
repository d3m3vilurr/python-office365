from office365api.connection import Connection


class Api(object):
    BASE_URL = 'https://outlook.office365.com/api/v1.0/me'
    CALENDAR_URL = BASE_URL + '/calendars/{calendar_id}'
    EVENTS_URL = CALENDAR_URL + '/events'
    EVENT_URL = BASE_URL + '/events/{events_id}'

    UPDATE_URL = EVENT_URL
    ACCEPT_URL = EVENT_URL + '/accept'
    TENTATIVELY_ACCEPT_URL = EVENT_URL + '/tentativelyaccept'
    DECLINE_URL = EVENT_URL = '/decline'

    def __init__(self, auth):
        self.auth = auth
        self.connection = Connection(auth)

