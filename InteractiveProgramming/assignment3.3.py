try:
    s = raw_input("Enter score between 0.0 and 1.0: ")
    score = float(s)
    if score < 0 or score > 1:
        raise Exception
except ValueError:
    print "You didn't even enter a number"
except:
    print "Not a possible score."
else:
    if score >= 0.9:
        print "A"
    elif score >= 0.8:
        print "B"
    elif score >= 0.7:
        print "C"
    elif score >= 0.6:
        print "D"
    else:
        print "F"
