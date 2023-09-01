# parrot.py

def parrot_says(message):
    """
    Parrot says the provided message.

    Args:
    message (str): The message to be echoed.

    Returns:
    str: The same message that the parrot "says."
    """
    return message

# Example usage
if __name__ == "__main__":
    message = input("Enter a message: ")
    response = parrot_says(message)
    print(f"The parrot says: {response}")
