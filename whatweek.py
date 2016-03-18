import sys
import datetime
import dateparser

if len(sys.argv)<2:
    d = datetime.date.today().strftime("%B %d, %Y")
else:
    d = sys.argv[1]
date = dateparser.parse(d)

print "Week {}" .format(date.isocalendar()[1])
