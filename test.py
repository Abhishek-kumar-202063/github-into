import datetime

def greet(name):
    # Get the current hour
    current_hour = datetime.datetime.now().hour

    # Determine the appropriate greeting based on the time of day
    if current_hour < 12:
        time_of_day = "Good morning"
    elif current_hour < 18:
        time_of_day = "Good afternoon"
    else:
        time_of_day = "Good evening"

    # Return a personalized greeting message
    return f"{time_of_day}, {name}!"

# Ask for user input
user_name = "Abhishek"

# Call the greet function and print the greeting
print(greet(user_name))
