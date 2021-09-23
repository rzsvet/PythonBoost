def normalize(text):
    return text.capitalize() + "!" if text == text.upper() else text


print(normalize("CAPS LOCK DAY IS OVER"))  # "Caps lock day is over!"

print(normalize("Today is not caps lock day."))  # "Today is not caps lock day."

print(normalize("Let us stay calm, no need to panic."))  # "Let us stay calm, no need to panic."

