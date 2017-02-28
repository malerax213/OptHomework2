# OptHomework2
Sistemes i Tecnologies Web - Optional Homework 2

Homework 2: Simple Web API access

Part 1 (0.25 extra points)

Using Weather Underground API available at:
https://www.wunderground.com/weather/api

And using the Hourly entry point:
https://www.wunderground.com/weather/api/d/docs?d=data/hourly

Parse it to provide relevant information to the user, for example, a short hourly
forecast.

Part 2 (0.25 extra points)

Choose one of the following: - Implement more 2 calls to more entry points
(astronomy, conditions, satellite, etc.). Do it in a easy to extend way, using
good programming practices, etc. and letting user choose which entry point via
command line.

• Implement a, somewhat, more useful use of the data you are already getting
(almanac+hourly). For instance, to give advice on clothing: first time
in the morning calm, later wind then advise to take sweater when going
out.

Your goal is to build a simple python application, using the following libraries:
• requests (valid with urllib2)
• json

Tips

If you need to access command line options, you can use any of the standard 
python methods (sys.argv, argparse, optparse), or, better take a look at docopt
and/or click libraries.

Requirements

• Code must be developed entirely on github.com.
• Code must follow good practice and good python conventions: variable naming, identation, documentation, etc.
• Code must work.
Scoring: If all requeriments are met students get 0.5 extra points for Practice1.
