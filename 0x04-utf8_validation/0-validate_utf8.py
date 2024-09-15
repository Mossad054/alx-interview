#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""
    skip = 0
    n = len(data)

    for i in range(n):
        if skip > 0:
            skip -= 1
            continue

        byte = data[i]

        # Ensure byte is a valid integer and within UTF-8 range
        if not isinstance(byte, int) or byte < 0 or byte > 0x10FFFF:
            return False

        # 1-byte character (ASCII)
        if byte <= 0x7F:
            continue

        # 4-byte character
        elif byte & 0b11111000 == 0b11110000:
            span = 4

        # 3-byte character
        elif byte & 0b11110000 == 0b11100000:
            span = 3

        # 2-byte character
        elif byte & 0b11100000 == 0b11000000:
            span = 2

        # Invalid leading byte
        else:
            return False

        # Validate continuation bytes
        if (n - i < span or 
            not all(data[j] & 0b11000000 == 0b10000000 for j in range(i + 1, i + span))):
            return False

        skip = span - 1

    return True
