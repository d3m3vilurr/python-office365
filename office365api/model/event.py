from office365api.model.model import Model


class Event(Model):

    select = ['Subject', 'Body', 'DateTimeCreated', 'DateTimeLastModified',
              'Start', 'End', 'Reminder', 'Location', 'Attendees', 'Organizer', 'iCalUId', 'HasAttachments']

    def __init__(self, Subject, Body,
                 HasAttachments=False, Id=None, DateTimeCreated=None, DateTimeLastModified=None,
                 Start=None, End=None,
                 Reminder=None, Location=None, Attendees=None,
                 Organizer=None):
        self.Id = Id
        self.Subject = Subject
        self.Body = Body
        self.HasAttachments = HasAttachments
        self.DateTimeCreated = DateTimeCreated
        self.DateTimeLastModified = DateTimeLastModified
        self.Start = Start
        self.End = End
        self.Reminder = Reminder
        self.Location = Location
        self.Attendees = Attendees
        self.Organizer = Organizer

    def __iter__(self):
        """
        Convert objects back to dictionary.
        :return: Dictionary representation.
        """
        for k, v in self.__dict__.items():
            if v is not None and k != 'HasAttachments':
                yield k, Model.get_value(v)

