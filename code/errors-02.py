def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is tuesday!",
        "wednesday": "It is the middle of the week.",
        "thursday": "Today is Donnerstag in German!",
        "friday": "Last day of the week!",
        "saturday": "Hooray for the weekend!",
        "sunday": "Aw, the weekend is almost over."
    }
    print(messages[day])


def print_friday_message():
    print_message("Friday")
