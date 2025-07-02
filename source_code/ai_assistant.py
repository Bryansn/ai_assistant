from abc import ABC, abstractmethod
from request import Request
from response import Response


# Other assistants will inherit from this (Inheritance)
# Shows what the assistant should do, not how it does it (Abstraction)
# Subclasses will overide these methods differently (Polymorphism)
# define core assistant behaviors
class AIAssistant(ABC):
    @abstractmethod
    # greet the user
    def greetUser(self) -> None:
        """Greet the user in a general way."""
        pass

    # handle request
    @abstractmethod
    def handleRequest(self, request: Request) -> None:
        """Process the user’s request."""
        pass

    # give response
    @abstractmethod
    def generateResponse(self) -> Response:
        """Return a response object after processing."""
        pass
