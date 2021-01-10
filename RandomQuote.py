import requests
import json
import random

quotes = requests.get("https://type.fit/api/quotes")
allQuotes = json.loads(quotes.text)
randomQuote = random.randint(0, len(allQuotes))
print(allQuotes[randomQuote]["text"] + "\nBy: " + allQuotes[randomQuote]["author"])
