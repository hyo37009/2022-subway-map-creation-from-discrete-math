import pandas as pd


allData = pd.read_excel('운영기관_역사_코드정보.xlsx')

print(allData.head())

newData = allData[['LN_NM', 'STIN_NM']]

lines = allData['LN_NM'].tolist()
stins = allData['STIN_NM'].tolist()

st = []
li = []

now = '공항철도'
li.append(now)
tem = []
for i in range(len(lines)):
    if now == lines[i]:
        tem.append(stins[i])
    else:
        st.append(tem)
        tem = []
        now = lines[i]
        li.append(now)
        tem.append(stins[i])
st.append(tem)

train_dict = {li[i] : st[i] for i in range(len(li))}
print(train_dict)

hwan = []

for i in range(len(st)):
    for j in st[i]:
        for k in st[i+1:]:
            if j in k:
                hwan.append(j)
hwan = list(set(hwan))
print(hwan)
print(len(hwan))

f = open("역 정보.txt", 'w')
f.write(str(train_dict))
f.write('\n')
f.write('라인 정보 : ')
f.write('\n')
f.write(str(li))
f.write('\n')
f.write('역 정보 : ')
f.write('\n')
f.write(str(st))
f.write('\n')
f.write('환승역 정보 : ')
f.write('\n')
f.write(str(hwan))
f.write('\n')

f.close()