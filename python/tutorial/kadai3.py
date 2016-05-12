# -*- coding: utf-8 -*-

data = [
    {"name": "田中花子", "gender": "女性", "birthY": 1980, "score": 58},
    {"name": "鈴木一郎", "gender": "男性", "birthY": 2000, "score": 76},
    {"name": "山田太郎", "gender": "男性", "birthY": 1989, "score": 69},
    {"name": "佐藤恵子", "gender": "女性", "birthY": 1992, "score": 62},
    {"name": "石井あや", "gender": "女性", "birthY": 1978, "score": 71}
]

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

# calculate array average
def avg(x):
    return 1.0 * sum(x) / len(x)


### main program ###
scores_uru = []
scores_nonuru = []

for datum in data:
    chk = uruChecker(datum["birthY"]) 
    if chk == 1:
        scores_uru.append(datum["score"])
    elif chk == 0:
        scores_nonuru.append(datum["score"])
    else:
        print("uruChecker Error!")

print "うるう年生まれの観客の平均評価点"
print avg(scores_uru)
print "うるう年以外に生まれた観客の平均評価点"
print avg(scores_nonuru)


