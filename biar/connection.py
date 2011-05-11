import fluidinfo

class Connection:
    @classmethod
    def connect(klass, username, password):
        conn = klass()
        conn.username = username
        
        # Check that we can actually connect, e.g. network is not down
        try:
            fluidinfo.login(username, password)
        except Exception as e:
            print "Encountered a problem loggin in"
            raise e

        # Check to ensure that the login creditials were accepted
        response = conn.user_info()
        if type(response) is str:
            errorMessage = "Log in failed for user %s, message: %s" % (conn.username, response)
            raise Exception(errorMessage)
        
        return conn

    def user_info(self):
        headers, response = fluidinfo.call('GET', "/users/%s" % self.username)
        return response

    def user_name(self):
        return self.user_info()['name']

    def user_id(self):
        return self.user_info()['id']
