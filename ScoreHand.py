#!/usr/bin/python

import sys
import itertools

Ranks = {}
Ranks['a'] = 1
Ranks['2'] = 2
Ranks['3'] = 3
Ranks['4'] = 4
Ranks['5'] = 5
Ranks['6'] = 6
Ranks['7'] = 7
Ranks['8'] = 8
Ranks['9'] = 9
Ranks['t'] = 10
Ranks['j'] = 11
Ranks['q'] = 12
Ranks['k'] = 13

Values = {}
Values['a'] = 1
Values['2'] = 2
Values['3'] = 3
Values['4'] = 4
Values['5'] = 5
Values['6'] = 6
Values['7'] = 7
Values['8'] = 8
Values['9'] = 9
Values['t'] = 10
Values['j'] = 10
Values['q'] = 10
Values['k'] = 10

HandRank = []
HandValue = []
HandSuit = []
for i in range(1,len(sys.argv)):
    Card = sys.argv[i]
    Rank = Ranks[Card[0:1]]
    Value = Values[Card[0:1]]
    Suit = Card[1:2]
    HandRank.append(Rank)
    HandValue.append(Value)
    HandSuit.append(Suit)

#=====================================================================================
# 15s 
#=====================================================================================
Total15s = 0
for NumCards in range(2,6):
    Combos = itertools.combinations(HandValue,NumCards)
    for Combo in Combos:
        if(sum(Combo) == 15):
            Total15s += 2
print "15s:", Total15s

#=====================================================================================
# Pairs
#=====================================================================================
TotalPairs = 0
Combos = itertools.combinations(HandRank,2)
for Combo in Combos:
    v1, v2 = Combo
    if v1 == v2:
        TotalPairs += 2
print "Pairs:", TotalPairs

#=====================================================================================
# Runs 
#=====================================================================================
TotalRuns = 0
SortedRanks = sorted(HandRank)
RunTally = 1
Multiplier = 0
NoMultiplier = 1
PrevDiff = 100
for i in range(1,5):
    diff = SortedRanks[i] - SortedRanks[i-1]
    if diff == 0:
        NoMultiplier = 0
        Multiplier += 1
        if diff != PrevDiff:
            Multiplier += 1
    if diff == 1:
        RunTally += 1
    if diff > 1:
        if RunTally >= 3:
            TotalRuns = RunTally * (Multiplier + NoMultiplier)
        RunTally = 1
        Multiplier = 0
        NoMultiplier = 1
    PrevDiff = diff
if RunTally >= 3: 
    TotalRuns = RunTally * (Multiplier + NoMultiplier)
print "Runs:", TotalRuns

#=====================================================================================
# Flush 
#=====================================================================================
TotalFlush = 1
BaseSuit = HandSuit[0]
for i in range(1,4):
    if HandSuit[i] == BaseSuit:
        TotalFlush += 1
if TotalFlush == 4:
    if HandSuit[4] == BaseSuit:
        TotalFlush += 1
else:
    TotalFlush = 0

print "Flush:", TotalFlush

#=====================================================================================
# Nobs 
#=====================================================================================
TotalNobs = 0
for i in range(3):
    if HandRank[i] == 11 and HandSuit[i] == HandSuit[4]:
        TotalNobs += 1

print "Nobs:", TotalNobs

print ""
print "Total:", Total15s + TotalPairs + TotalRuns + TotalFlush + TotalNobs

