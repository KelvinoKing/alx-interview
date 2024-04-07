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
    # Function to check if the given integer represents a valid UTF-8 character
    def is_start_of_char(byte):
        return (byte >> 7) == 0b0

    def get_num_bytes_following(byte):
        if (byte >> 5) == 0b110:
            return 1
        elif (byte >> 4) == 0b1110:
            return 2
        elif (byte >> 3) == 0b11110:
            return 3
        else:
            return 0

    # Iterate over each byte in the data
    i = 0
    while i < len(data):
        byte = data[i]

        # If it's the start of a character
        if is_start_of_char(byte):
            num_bytes_following = get_num_bytes_following(byte)

            # Check if there are enough bytes following
            if num_bytes_following > len(data) - i - 1:
                return False

            # Check if following bytes start with 10
            for j in range(1, num_bytes_following + 1):
                if (data[i + j] >> 6) != 0b10:
                    return False

            i += num_bytes_following + 1
        else:
            return False

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
