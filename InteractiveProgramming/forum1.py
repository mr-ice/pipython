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
    print "No error detected"
