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
line_incheon1 = stins[52:81]
line_incheon2 = stins[81:108]
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

line5 = line('5호선', len(line_5))
line5.setline(line_5)

line6 = line('6호선', len(line_6))
line6.setline(line_6)

line7 = line('7호선', len(line_7))
line7.setline(line_7)

line8 = line('8호선', len(line_8))
line8.setline(line_8)

line9 = line('9호선', len(line_9))
line9.setline(line_9)

lineSuin = line('수인선', len(line_suin))
lineSuin.setline(line_suin)

lineKyongchun = line('경춘선', len(line_kyongchun))
lineKyongchun.setline(line_kyongchun)

lineKyongchung = line('경의중앙선', len(line_kyongchung))
lineKyongchung.setline(line_kyongchung)
lineKyongchung.linetree(line_kyongchung_1, '가좌')

lineKyongkang = line('경강선', len(line_kyongkang))
lineKyongkang.setline(line_kyongkang)

lineDonghae = line('동해선', len(line_donghae))
lineDonghae.setline(line_donghae)

lineSeohae = line('서해선', len(line_seohae))
lineSeohae.setline(line_seohae)

lineUi = line('우이신설선', len(line_ui))
lineUi.setline(line_ui)

lineEujungbu = line('의정부경전철', len(line_eujungbu))
lineEujungbu.setline(line_eujungbu)

linekong = line('공항철도', len(line_kong))
linekong.setline(line_kong)

linebun = line('신분당선', len(line_bun))
linebun.setline(line_bun)

lineyong = line('용인에버라인', len(line_yong))
lineyong.setline(line_yong)

linekimpo = line('김포골드라인', len(line_kimpo))
linekimpo.setline(line_kimpo)

lineincheon1 = line('인천1호선', len(line_incheon1))
lineincheon1.setline(line_incheon1)

lineincheon2 = line('인천2호선', len(line_incheon2))
lineincheon2.setline(line_incheon2)




lines = [line1, line2, line3, line4, line5, line6, line7, line8,\
         line9, lineSuin, lineKyongchun, lineKyongchung, lineKyongkang, \
         lineDonghae, lineUi, lineEujungbu, linekong, linebun,\
         lineyong, linekimpo, lineincheon1, lineincheon2]


hwanlist = []
hwanname = []

for i in range(len(lines)):
    for j in range(len(lines[i])):
        stat = lines[i].linelist[j]
        if stat.hwan:
            for k in range(len(lines)):
                for l in range(len(lines[k])):
                    if stat.name == lines[k].linelist[l].name:
                        stat.line.add(lines[k].linename)

            hwanname.append(stat.name)
            if hwanname.count(stat.name) >= 2:
                continue
            hwanlist.append(stat)




def retLineClass(line):
    for i in lines:
        if i.linename == line:
            return i
    return False

def flatter(nodes, flattenned=False):
    try:
        result == 0
    except:
        result = []

    if False in nodes:
        return False
    for i in nodes:
        if type(i) == list:
            result += flatter(i)
            flattenned = True
        else:
            result.append(i)
    return result