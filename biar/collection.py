import fluidinfo
import pprint

def pp(text):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(text)

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
        pp("creating namespace...")
        namespace_info = {
            'name': name,
            'description': description
        }
        headers, response = fluidinfo.call('POST', self.parent_namespace(), namespace_info)
        # TODO check headers
        self.fluid_id = response['id']
        self.fluid_url = response['URI']
        pp(headers)
        pp(response)


        tag_info = {
            'name' : 'element',
            'description' : 'Tag indicating that object is part of a list',
            'indexed' : False
        }
        headers, response = fluidinfo.call('POST', "/tags/%s/biar/collections/%s"
                                           % (self.connection.username,
                                              self.name), tag_info)
        # TODO check headers
        pp(headers)
        pp(response)

    def add_work(self, work):
        tag_path = "/objects/%s/%s/biar/collections/%s/%s" % (work.object_id,
                                                              self.connection.username,
                                                              self.name, 'element')
        headers, response = fluidinfo.call('PUT', tag_path)
        # TODO check headers

    def list_works(self):
        querystring = "has %s/biar/collections/%s/element" % (self.connection.username, self.name)
        headers, response = fluidinfo.call('GET', '/objects', query=querystring)
        # TODO check headers
        return response['ids']

    def parent_namespace(self):
        return "/namespaces/%s/biar/collections" % (self.connection.username)

    def collection_namespace(self):
        return "%s/%s" % (self.parent_namespace(), self.name)
