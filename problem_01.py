"""
    An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

    Example: (Input --> Output)

    "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

    isIsogram "Dermatoglyphics" = true
    isIsogram "moose" = false
    isIsogram "aba" = false
"""

def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            return False
    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))