M = 15804597 #15745224
p = (M%1000)%22
q = (M%1000)%16
print('M#:', M)
print('P:', p, 'Q:', q)
dp = [3, 5, 9, 14, 10, 1, 15, 22, p, q]
dp = sorted(dp)
epsilon = 3
minsup = 3
print(dp)
for i in range(len(dp)):
    count = 0
    for j in range(len(dp)):
        print(abs(dp[j]-dp[i]), end = ' ')
    print()
dic = {}
for i in range(len(dp)):
    count = 0
    lis = []
    for j in range(len(dp)):
        # print(abs(dp[j]-dp[i]), end = ' ')
        if (abs(dp[j]-dp[i]) <= epsilon and i!=j):
            # print()
            # print(i,j)
            lis.append('P'+str(j+1))
            # if ('P'+str(i+1) in dic.keys()):
            #     dic['P'+str(i+1)] = dic['P'+str(i+1)].append('P'+str(j+1))
            # else:
            #     dic['P'+str(i+1)] = ['P'+str(j+1)]
    dic['P'+str(i+1)] = lis
    # print()
# print(dic)
dic1 = {'core': [], 'noise': [], 'border': [], 'corereal': [], 'noisereal': []}
for i, j in dic.items():
    print(i, j)
    if (len([i]+j) >= minsup):
        x = dic1['core']
        x.append([i]+j)
        dic1['core'] = x
        x = dic1['corereal']
        x.append(i)
        dic1['corereal'] = x
    else:
        x = dic1['noise']
        x.append(i)
        dic1['noise'] = x
# print(dic1)
# print(str(dic1['core']))
for i in dic1['noise']:
    # print(i)
    if (i in str(dic1['core'])):
        x = dic1['border']
        x.append(i)
        dic1['border'] = x
    else:
        x = dic1['noisereal']
        x.append(i)
        dic1['noisereal'] = x
print('Core:', dic1['corereal'])
print('Noise:', dic1['noisereal'])
print('Border:', dic1['border'])