import fluidinfo

class Work:
    """
    Possible examples of works include traditional works such as papers and non traditional works such videos.
    """

    @classmethod
    def create(klass, connection):
        """Create a new, blank work."""
        headers, response = fluidinfo.call('POST', '/objects/')
        work = klass(response['id'])
        work.connection = connection
        return work

    def __init__(self, object_id):
        """object_id is the fluiddb object id
        """
        self.object_id = object_id

    def SetCanonicalTag(self, name, value=None):
        # check if biar namespace exists
        # persist attribtue
        pass

    def SetPersonalTag(self, name, value=None):
        # check if personal namespace exists
        # persist attribute
        pass

    def GetCanonicalTag(self, name):
        pass

    def GetPersonalTag(self, name):
        pass

    def set_title(self, title):
        self.set_public_attribute(self, 'title', title)

    def title(self):
        self.get_public_attribute(self, 'title')

