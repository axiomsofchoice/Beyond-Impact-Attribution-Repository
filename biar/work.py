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
        """object_id is the fluidinfo object id"""
        self.object_id = object_id

    def set_canonical_tag(self, name, value=None):
        namespace = '/namespaces/biar'
        headers, response = fluidinfo.call('GET', namespace, returnTags=True)
        if not headers['status'] == '200':
            raise Exception("namespace %s does not exist" % namespace)
        if not name in response['tagNames']:
            raise Exception("tag %s not found in namespace" % (tag,
                                                               namespace))

        tag_path = "/objects/%s/%s/%s" % (self.object_id, 'biar', name)
        headers, response = fluidinfo.call('PUT', tag_path, value)
        print headers
        print response


    def set_personal_tag(self, name, value=None):
        namespace = "/namespaces/%s/biar" % self.connection.username

        headers, response = fluidinfo.call('GET', namespace, returnTags=True)
        if not headers['status'] == '200':
            raise Exception("namespace %s does not exist" % namespace)
        if not name in response['tagNames']:
            raise Exception("tag %s not found in namespace" % (name,
                                                               namespace))

        tag_path = "/objects/%s/%s/biar/%s" % (self.object_id,
                                               self.connection.username, name)
        headers, response = fluidinfo.call('PUT', tag_path, value)
        print headers
        print response


    def get_canonical_tag(self, name):
        namespace = "/namespaces/biar"
        tag_path = "/objects/%s/biar/%s" % (self.object_id,name)
        headers, response = fluidinfo.call('GET', tag_path)
        print headers
        print response

    def get_personal_tag(self, name):
        namespace = "/namespaces/%s/biar" % self.connection.username
        tag_path = "/objects/%s/%s/biar/%s" % (self.object_id,
                                               self.connection.username, name)
        headers, response = fluidinfo.call('GET', tag_path)
        print headers
        print response

    def set_title(self, title):
        self.set_canonical_tag(self, 'title', title)

    def title(self):
        self.get_canonical_tag(self, 'title')

