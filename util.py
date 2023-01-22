import unicodedata


def remove_control_characters(string):
    return "".join(ch for ch in string if unicodedata.category(ch)[0] != "C")
