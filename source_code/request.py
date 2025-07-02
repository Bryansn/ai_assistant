from datetime import datetime  # time stamp
from enum import Enum


class CommandType(Enum):
    SEARCH = "SEARCH"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    OTHER = "OTHER"


class Request:
    # Holds the users text, time, and command type
    def __init__(self, input_text: str, timestamp: datetime, command_type: CommandType):
        # Validate input_text
        if not isinstance(input_text, str) or not input_text.strip():
            raise ValueError("Input text must be a non-empty string.")

        # Validate timestamp
        if not isinstance(timestamp, datetime):
            raise ValueError("Timestamp must be a datetime object.")

        # Validate command_type
        if not isinstance(command_type, CommandType):
            raise ValueError("command_type must be a valid CommandType enum value.")

        # store data inside object, can use later
        self.input_text = input_text
        self.timestamp = timestamp
        self.command_type = command_type

    # print in nice format
    def __repr__(self):
        return (
            f"Request(input_text='{self.input_text}', "
            f"timestamp='{self.timestamp}', command_type={self.command_type})"
        )
