#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding,
else return False. A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Iterate over each byte in the data
    i = 0
    while i < len(data):
        # Get the number of bytes in the current UTF-8 character
        num_bytes = 0
        mask = 1 << 7
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        # Validate the number of bytes
        if num_bytes == 0:
            num_bytes = 1
        elif num_bytes == 1 or num_bytes > 4:
            return False

        # Validate the remaining bytes
        i += 1
        for _ in range(num_bytes - 1):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
            i += 1

    return True


# Testing the function
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # Output: True

    data = [
        80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99,
        111, 111, 108, 33]
    print(validUTF8(data))  # Output: True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Output: False
