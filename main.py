seconds = input('Enter the number of seconds (integer): ')
seconds = int(seconds)

# ... complete the code below
minutes, seconds = divmod(seconds,60)
hours, minutes = divmod(minutes, 60)

# Follow the formatting given
# e.g. The duration is X hours, X minutes, and X seconds.
print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
