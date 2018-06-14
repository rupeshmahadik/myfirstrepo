import random

p=random.randint(1,6)
q=random.randint(1,6)
r=random.randint(1,6)
s=random.randint(1,6)
t=random.randint(1,6)

a=[p,q,r,s,t]

print a

total = 0
total1 = 0
total2 = 0


if a.count(1)==5:
    total=1150
if a.count(1)==4:
    total=1150
if a.count(1)==3:
    total=1000
if a.count(1)==2:
    total=200
if a.count(1)==1:
    total=100 



if a.count(2)==3:
    total1=200
if a.count(2)==4:
    total1=0
if a.count(2)==5:
    total1=0
if a.count(5)==3:
    total1=300
if a.count(5)==4:
    total1=0
if a.count(5)==5:
    total1=0
if a.count(2)==5:
    total1=0
if a.count(3)==3:
    total1=300
if a.count(3)==4:
    total1=0
if a.count(3)==5:
    total1=0
if a.count(4)==3:
    total1=400
if a.count(4)==4:
    total1=0
if a.count(4)==5:
    total1=0
if a.count(6)==3:
    total1=600
if a.count(6)==4:
    total1=0
if a.count(6)==5:
    total1=0

if a.count(5)==1:
    total2=50
if a.count(5)==2:
    total2=100
if a.count(5)==3:
    total2=500
if a.count(5)==4:
    total2=550
if a.count(5)==5:
    total1=600

print total + total1 + total2


 
