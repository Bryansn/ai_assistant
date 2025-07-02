from typing import Dict  # define dictionary type


class UserProfile:
    # store name, age, prefrences, and premium status
    def __init__(
        self, name: str, age: int, preferences: Dict[str, str], is_premium: bool
    ):
        # Validation for name
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")

        # Validation for age
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        # must be a dictionary
        if not isinstance(preferences, dict):
            raise ValueError(
                "Preferences must be a dictionary with string keys and values."
            )

        # Validation for is_premium
        if not isinstance(is_premium, bool):
            raise ValueError("is_premium must be a boolean value.")

        # Save the values
        self.name = name
        self.age = age
        self.preferences = preferences
        self.is_premium = is_premium

    # how the profile will be printed
    def __repr__(self):
        return (
            f"UserProfile(name='{self.name}', age={self.age}, "
            f"preferences={self.preferences}, is_premium={self.is_premium})"
        )
