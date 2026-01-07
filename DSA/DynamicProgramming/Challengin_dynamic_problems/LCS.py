def LCS(s1,s2, lenS1, lenS2):
    if lenS1 == 0 or lenS2 == 0:
        return 0  
    
    if s1[lenS1-1]==s2[lenS2-1]:
        return LCS(s1,s2,lenS1-1, lenS2-1)+1
    
    return max(LCS(s1,s2,lenS1-1, lenS2),LCS(s1,s2,lenS1,lenS2-1))
    
print(LCS("Asdassa", "sasdsdaa",7,8))