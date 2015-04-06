
wumpuses = {
   'year' : 1,
   'fast' : 1.0,
   'slow' : 1000.0,
   }

def advance(wumpuses):
    wumpuses['year'] += 1
    wumpuses['slow'] *= 2
    wumpuses['slow'] *= .6
    wumpuses['fast'] *= 2
    wumpuses['fast'] *= .7

print "Year     Slow     Fast"
while True:
    print "%4d     %4f     %4f"%(wumpuses['year'],wumpuses['slow'],wumpuses['fast'])
    advance(wumpuses)

    if wumpuses['fast'] >= wumpuses['slow']:
        break

