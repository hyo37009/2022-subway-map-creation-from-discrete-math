import pandas as pd
from subway import *


allData = pd.read_excel('운영기관_역사_코드정보.xlsx')

# print(allData.head())

newData = allData[['LN_NM', 'STIN_NM']]

lines = allData['LN_NM'].tolist()
stins = allData['STIN_NM'].tolist()
linelist = []

line_kong = stins[:14]
line_bun = stins[14:27]
line_yong = stins[27:42]
line_kimpo = stins[42:52]
line_incheon = stins[52:108]
line_1 = stins[108:170]
line_1_1 = stins[170:204]
line_1_2 = stins[204]
line_1_3 = stins[205]
line_2 = stins[206:249]
line_2_1 = stins[249:253]
line_2_2 = stins[253:257]
line_3 = stins[257:301]
line_4 = stins[301:349]
line_5 = stins[349:405]
line_6 = stins[405:448]
line_7 = stins[448:495]
line_8 = stins[495:512]
line_9 = stins[512:550]
line_suin = stins[550:613]
line_kyongchun = stins[613:638]
line_kyongchung = stins[691:667:-1] + stins[638:667]
line_kyongchung_1 = stins[692:694]
line_kyongkang = stins[694:705]
line_donghae = stins[705:720]
line_seohae = stins[720:732]
line_ui = stins[732:745]
line_eujungbu = stins[745:]


line1 = line('1호선', len(line_1))
line1.setline(line_1)
line1.linetree(line_1_1, '구로')
line1.linetree(line_1_2, '금천구청')
line1.linetree(line_1_3, '병점')

line2 = line('2호선', len(line_2))
line2.setline(line_2)
line2.linetree(line_2_1, '성수')
line2.linetree(line_2_2, '신도림')
line2.ret_station('충정로(경기대입구)').connection(line2.ret_station('시청'), 1)
line2.ret_station('시청').connection(line2.ret_station('충정로(경기대입구)'), 0)

line3 = line('3호선', len(line_3))
line3.setline(line_3)

line4 = line('4호선', len(line_4))
line4.setline(line_4)

line5 = line('5호선', )