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
        self.object_id = object_id

    def set_public_attribute(self, name, value=None):
        # check if biar namespace exists
        # persist attribtue
        pass

    def set_personal_attribute(self, name, value=None):
        # check if personal namespace exists
        # persist attribute
        pass

    def get_public_attribute(self, name):
        pass

    def get_personal_attribute(self, name):
        pass

    def set_title(self, title):
        self.set_public_attribute(self, 'title', title)

    def title(self):
        self.get_public_attribute(self, 'title')

