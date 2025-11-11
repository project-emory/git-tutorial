#!/usr/bin/env python3
"""
A greetings module for practicing Git operations.
"""

def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}!"

def farewell(name):
    """Return a personalized farewell."""
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("Student"))
    print(farewell("Student"))
