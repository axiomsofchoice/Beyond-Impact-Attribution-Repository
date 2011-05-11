import fluidinfo

class Connection:
    @classmethod
    def connect(klass, username, password):
        conn = klass()
        conn.username = username
        fluidinfo.login(username, password)
        return conn

    def user_info(self):
        headers, response = fluidinfo.call('GET', "/users/%s" % self.username)
        return response

    def user_name(self):
        return self.user_info()['name']

    def user_id(self):
        return self.user_info()['id']
