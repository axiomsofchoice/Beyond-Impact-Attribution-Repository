"""This collection of classes provides the core abstration of the Beyond Impact Attribution Repository
"""


class Work:
    """Possible examples of works include traditional works such as papers and non traditional works such videos.
    """
    def __init(self,title):
        pass
    
    def createNew(self):
        """Writes the work down to the underlying database.
        """
        pass
    
    def SetPersonalTag(self, tagname, tagvalue):
        self.personaltags[tagname] = tagvalue

    def SetCanonicalTag(self, tagname, tagvalue):
        pass
        self.canonicaltags[tagname] = tagvalue

class ListOfWorks:
    """The class encapsulated the collection of works that a user can put together for a certain purpose.
    """
    def __init(self,description):
        pass

    def createNew(self):
        pass
    
    def AddWork(self,workToAdd):
        """Creates a new list membership with a work and adds it to this list.
        """
        pass

class ListMembership:
    """This list membership class allows a work to be added to a list. 
    """
    def __init(self):
        pass

    def SetPersonalTag(self,tagvalue):
        pass

    def SetCanonicalTag(self,tagvalue):
        pass


