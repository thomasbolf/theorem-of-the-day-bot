# Discord Theorem of The Day Bot

This is a Discord bot that fetches the daily theorem file from https://www.theoremoftheday.org, converts it to an image, and sends it to the "totd" channel on Discord as the Theorem of The Day! This bot runs everyday. I plan on adding more functionality over time. 

Currently this app is running on an AWS Free Tier EC2 instance. If I run into problems with this or find a better way, this app will no longer be running on an AWS Free Tier EC2 instance. 

## Project Structure

- **`bot.py`**: Main file that sets up the Discord client and manages posting the theorem of the day.
- **`utils.py`**: Contains utility functions for generating messages and handling images.
- **`pdf_handler.py`**: Handles PDF fetching and conversion to images.

## SETUP

https://discord.com/oauth2/authorize?client_id=1267223585940832298
