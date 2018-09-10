from office365api.model.event import Event
from office365api.calendar.api import Api


class Base(Api):

    def get_events_from_calendar(self,
                                 calendar,
                                 #select=None,
                                 #filters=None,
                                 #search=None,
                                 start,
                                 end,
                                 #order_by=None,
                                 top=100,
                                 skip=0):
        url = self.CALENDAR_VIEW_URL.format(calendar_id=calendar)

        #select = select or []
        #select.extend(Event.parameters())
        #print(top)
        #params = {'$select': (','.join(select)), '$top': top, '$skip': skip}
        params = {}

        def add(k, v):
            if v:
                params[k] = v

        # Search must be surrounded by quotes
        #add('$search', '"{}"'.format(search) if search else None)
        #add('$filter', filters)
        #add('$orderby', order_by)
        add('startDateTime', start)
        add('endDateTime', end)
        add('top', top)
        add('skip', skip)

        # search override
        #if search:
        #    for key in ['$skip', '$filter', '$orderby']:
        #        params.pop(key, None)

        response = self.connection.get(url=url, params=params)
        data = response.json()
        #return [value for value in data.get('value')] if data else []
        return [Event.from_dict(value) for value in data.get('value')] if data else []

    def create_event_to_calendar(self,
                                 calendar,
                                 event):
        pass

    def update_event_to_calendar(self,
                                 calendar,
                                 event):
        pass

    def accept_event(self, event, tentatively=False):
        pass

    def decline_event(self, event):
        pass

    def cancel_event(self, event):
        pass
