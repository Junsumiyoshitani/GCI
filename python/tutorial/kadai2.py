#encode: utf8

# if uru-year return 1, not uru-year return 0
def uruChecker(y):
    try:
        y = int(y)
    except Exception, e:
        print e
        print "please set integer @uruChecker"
        quit()

    uru = 0
    if y%4 == 0:
        uru = 1
    if y%100 == 0:
        uru = 0
    if y%400 == 0:
        uru = 1
    return uru

### main program ###
import sys

argvs = sys.argv
argc = len(argvs)
if argc != 2:
    print "please input argvs[1]:year"
    quit()

year = argvs[1]
chk = uruChecker(year)
if chk == 1:
    print "%s is uru-year" % year
else:
    print "%s is not uru-year" % year
