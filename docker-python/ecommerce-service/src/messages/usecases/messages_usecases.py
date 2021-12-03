from src.messages.domain.message import Message

class MessagesUsecases:
    def __init__(self, books_repository):
        self.messages_repository = messages_repository

    def get_messages(self):
        return self.messages_repository.get_messages()



