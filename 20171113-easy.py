"""
Description
Write a program that outputs the first recurring character in a string.

Formal Inputs & Outputs
Input Description
A string of alphabetical characters. Example:

ABCDEBC
Output description
The first recurring character from the input. From the above example:

B
Challenge Input
IKEUNFUVFV
PXLJOUDJVZGQHLBHGXIW
*l1J?)yn%R[}9~1"=k7]9;0[$
Bonus
Return the index (0 or 1 based, but please specify) where the original character is found in the string.

Credit
This challenge was suggested by user /u/HydratedCabbage
, many thanks! Have a good challenge idea? Consider submitting it to /r/dailyprogrammer_ideas and there's a good chance we'll use it.
"""

def get_first_recurring_character(s):
    seen_chars = dict()
    index = 0
    for char in s:
        if char in seen_chars:
            return char, seen_chars[char]
        seen_chars[char] = index
        index += 1

print(get_first_recurring_character('IKEUNFUVFVPXLJOUDJVZGQHLBHGXIW*l1J?)yn%R[}9~1"=k7]9;0[$'))
