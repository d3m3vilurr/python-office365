from office365api.calendar.api import Api
from office365api.calendar.base import Base


class Calendar(Base):

    _calendar = None

    @property
    def calendar(self):
        if not self._calendar:
            self._calendar = Cal(self.auth, 'Calendar')
        return self._calendar

    def get_all_calendars(self):
        response = self.connection.get(Api.CALENDAR_URL.format(calendar_id=''))
        data = response.json()
        return [Cal(self.auth, x.get('Name'), x.get('Id')) for x in data.get('value')] if data else []


class Cal(Base):

    def __init__(self, auth, calendar_name, calendar_id=None):
        super(Base, self).__init__(auth)
        self._calendar_name = calendar_name
        self._calendar_id = calendar_id

    @property
    def calendar_id(self):
        if self._calendar_id:
            return self._calendar_id
        if self._calendar_name:
            return self._calendar_name
        raise ValueError('Unknown calendar id')

    def get_events(self,
                   #select=None,
                   #filters=None,
                   #search=None,
                   start,
                   end,
                   #order_by=None,
                   top=50,
                   skip=0):
        """
        Downloads messages to local memory.

        :param skip:  Page results, skip - default 0.

        :param top: Page size, default take first 50 messages.

        :param select: The list of additional fields to retrieve.
        ['Bcc', 'IsDeliveryReceiptRequested']. By default returns only fields required for
        Message class.

        :param filters: Filters for messages OData 4.0 compatible.
        Example: "From/EmailAddress/Address ne 'MicrosoftOffice365@email.office.com'"

        :param search: Search criteria. When supplying string looks in subject, body etc
        if you want to look in a particular field 'from:microsoft'

        :param order_by: Order by field name. Example: 'DateTimeReceived desc'

        :param top: How many messages to retrieve. Default 50.

        :param skip: How many messages to skip. Default 0.
        """
        return self.get_events_from_calendar(calendar=self.calendar_id,
                                             #select=select,
                                             #filters=filters,
                                             #search=search,
                                             start=start,
                                             end=end,
                                             #order_by=order_by,
                                             top=top,
                                             skip=skip)

