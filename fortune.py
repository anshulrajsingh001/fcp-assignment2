import sys
import random
filename = sys.argv[1]
lines = open(filename).readlines()
quotes = "".join(lines)
quote = random.choice(quotes.split("%"))
print(quote)
