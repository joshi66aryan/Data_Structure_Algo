# top down approach
def numberFactor(n, tempDict): 
  if n in (0, 1, 2): 
    return 1 

  if n == 3: 
    return 2 
  else: 
    if n not in tempDict: 
      sub1 = numberFactor(n-1, tempDict) 
      sub2 = numberFactor(n-3, tempDict) 
      sub3 = numberFactor(n-4, tempDict) 
      tempDict[n] = sub1+sub2+sub3
    return tempDict[n]



# bottom up approach
def numberFactorBU(n): 
    tempArr = [1,1,1,2]
    for i in range(4,n+1):
        tempArr.append(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
    return tempArr[n]

print(numberFactorBU(5))