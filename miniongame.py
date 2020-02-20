
s = str(input())

listVowel = 'AEIOU'

def minion_game(s):
    """
    INPUT:
        s = string
    OUTPUT:
        Print the winner and the corresponding score
    """
    countK = 0
    countS = 0
    for i in range(len(s)):
        if s[i] in listVowel:
            for letter in s[i:]:
                countK += 1
        else:
            for letter in s[i:]:
                countS += 1
    if countK > countS:
        print('Kevin ' + str(countK))
    elif countS > countK:
        print('Stuart ' + str(countS))
    else:
        print('Draw')
        
minion_game(s)