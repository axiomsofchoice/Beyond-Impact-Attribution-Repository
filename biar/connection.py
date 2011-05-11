import fluidinfo

class Connection:
    @classmethod
    def connect(klass, username, password):
        fluidinfo.login(username, password)
        conn = klass()
        conn.username = username
        conn.setup_biar_namespaces()
        return conn

    def setup_biar_namespaces(self):
        pass

    def user_info(self):
        headers, response = fluidinfo.call('GET', "/users/%s" % self.username)
        return response

    def user_id(self):
        return self.user_info()['id']
