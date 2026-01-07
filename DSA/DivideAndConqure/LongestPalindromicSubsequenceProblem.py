def palindromicLSP(s1,startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s1[startIndex] == s1[endIndex]:
        return 2+palindromicLSP(s1,startIndex+1, endIndex-1)
    else:
        option1 = palindromicLSP(s1, startIndex, endIndex-1)
        option2 = palindromicLSP(s1, startIndex+1, endIndex)
        return max(option1, option2)

print(palindromicLSP("ELRMENMET",0,8))