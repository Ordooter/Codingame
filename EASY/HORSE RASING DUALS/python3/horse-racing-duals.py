# https://www.codingame.com/ide/puzzle/horse-racing-duals
pi = []
n = int(input())
for i in range(n):
    pi.append(int(input()))
pi.sort()

min = 10000000
for i in range(n-1):    
    if min>abs(pi[i]-pi[i+1]):
        min = abs(pi[i]-pi[i+1])
        if min==0:
            break
print(min)
