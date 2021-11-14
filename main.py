import discord
import os
import requests
import json
import random
import credentials

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")

    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

def get_popular():
    response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key="+credentials.tmdb)

    json_data = json.loads(response.text)
    msg = "Popular movies (updated daily):\n"
    for movie in json_data["results"]:
        msg += "{}\n".format(movie["title"])
    return msg

def get_upcoming():
    response = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key="+credentials.tmdb)

    json_data = json.loads(response.text)
    msg = "Upcoming movies:\n"
    for movie in json_data["results"]:
        msg += "{}\n".format(movie["title"])
    return msg

def get_toprated():
    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+credentials.tmdb)

    json_data = json.loads(response.text)
    msg = "Top rated movies:\n"
    for movie in json_data["results"]:
        msg += "{}\n".format(movie["title"])
    return msg

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith("!popular"):
        popular = get_popular()
        await message.channel.send(popular)

    if msg.startswith("!upcoming"):
        upcoming = get_upcoming()
        await message.channel.send(upcoming)
    
    if msg.startswith("!toprated"):
        toprated = get_toprated()
        await message.channel.send(toprated)

print(os.getenv('HOME'))
client.run(credentials.discord)