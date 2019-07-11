timeList1 = ['13.670194864273071','14.400002479553223','13.689579010009766','13.032463073730469']
timeList2 = ['14.033664464950562','14.763322830200195','15.465596914291382','13.273434877395630']

timeVal1 = float()
avgVal1 = float()

for a in range(len(timeList1)):
    timeVal1 += float(timeList1[a])
    avgVal1 = timeVal1/len(timeList1)
print('평균값1:', avgVal1)
print()

timeVal2 = float()
avgVal2 = float()
for b in range(len(timeList2)):
    timeVal2 += float(timeList2[b])
    avgVal2 = timeVal2 / len(timeList2)
print('평균값2:', avgVal2)

