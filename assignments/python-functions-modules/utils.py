def greet_student(name):
    """Return a personalized greeting message."""
    return f"Hello, {name}! Welcome to Python functions and modules."


def calculate_rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def is_palindrome(text):
    """Return True if text is a palindrome, ignoring case and spaces."""
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]
