import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
fill = input()
empty = input()
s=[[empty]*w for i in range(h)]
if h%2==0 or w==0 or h==0:
    print("Invalid Input")
    exit()
start=h//2
dis=0
if h==1:
    print(fill*w)
    exit()

for i in range(w):
    s[start][i]=fill
    if (dis==0):
        start-=1
    else:
        start+=1
    if start==-1:
        dis=1
        start=1
    if start==h:
        start=h-2
        dis=0
for i in range(h):
    print("".join(s[i]))