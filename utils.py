from datetime import datetime
import discord
URL = "http://www.theoremoftheday.org/todays.php"

def get_happy_day():
    # Get the current date and time
    now = datetime.now()
    # Get the day of the week as a string (e.g., "Monday")
    day_of_week = now.strftime("%A")
    return f"HAPPY {day_of_week.upper()}! Here is your [Theorem of the Day!]({URL})\n"

def get_image():
    with open('totdImage.png', 'rb') as f:
        picture = discord.File(f)
    return picture