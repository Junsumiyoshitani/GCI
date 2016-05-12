#encode: utf8

print "uru-year list 1900~2200"

for i in range(1900, 2201):
    uru = 0
    if i%4 == 0:
        uru = 1
    if i%100 == 0:
        uru = 0
    if i%400 == 0:
        uru = 1

    if uru == 1:
        print i,
print
