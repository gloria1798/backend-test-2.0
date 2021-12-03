class Message():

    def __init__(self, identifier, message, user, created_at = None):
        self.identifier = identifier
        self.message = message
        self.user = user
        self.created_at = created_at

    def to_dict(self):
        return {
            "identifier": self.identifier,
            "message": self.message,
            "user": self.user,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, dict):
        identifier = dict.get("identifier")
        message = dict.get("message")
        user = dict.get("user")    
        created_at = dict.get("created_at")
        return Message(identifier, message, user, created_at)
