import fluidinfo

class Collection:
    """The class encapsulated the collection of works that a user can put together for a certain purpose."""
    @classmethod
    def list_all(klass, connection):
        pass

    def __init__(self, connection, name, description=None):
        self.connection = connection
        self.name = name
        if not self.exists_in_fluid():
            self.init_in_fluid(name, description)
        if not self.fluid_id:
            raise Exception("should have an identifier assigned by fluid")

    def exists_in_fluid(self):
        headers, response = fluidinfo.call('GET', self.collection_namespace())
        if headers['status'] == '200':
            self.fluid_id = response['id']
            return True
        elif headers['status'] == '404':
            return False
        else:
            raise Exception("unexpected status code %s" % headers['status'])

    def init_in_fluid(self, name, description):
        print "creating namespace..."
        namespace_info = {
            'name': name,
            'description': description
        }
        headers, response = fluidinfo.call('POST', self.parent_namespace(), namespace_info)
        # TODO check headers
        self.fluid_id = response['id']
        self.fluid_url = response['URI']

        print "creating element tag in namespace..."
        tag_info = {
            'name' : 'element',
            'description' : 'Tag indicating that object is part of a list',
            'indexed' : False
        }
        headers, response = fluidinfo.call('POST', self.collection_namespace(), tag_info)
        # TODO check headers

    def add_work(self, object_id):
        pass

    def parent_namespace(self):
        return "/namespaces/%s/biar/collections" % (self.connection.username)

    def collection_namespace(self):
        return "%s/%s" % (self.parent_namespace(), self.name)
