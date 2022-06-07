import itertools

from 선로정리3 import lines, linenamelist, hwanlist, retStationClass, retLineClass, flatter, stins

'''
변수 설명
stins : 모든 역의 이름이 담긴 list
lines : 지하철 노선(class line)들이 담긴 list
line1~lineEujungbu : 각 지하철 노선의 정보가 담긴 line 클래스
hwanlist: 환승역(class station)들이 담긴 list

클래스 설명
class station:
    각 역의 정보를 가진 class
    변수:
        name: 역 이름
        line: 역이 속해있는 노선 이름이 저장되어있다
        hwan: 환승역 여부. 환승역이라면 True, 아니라면 False
        _neighbor : 인접한 역이 연결되어있다. 
                    [0] : 이전 역, [1] : 다음 역 
    함수:
        is_lineN(line:str): line에 속해있다면 True, 아니면 False를 반환
        prevStation: 이전 역 노드를 반환한다.
        nextStation: 다음 역 노드를 반환한다.
        printconnection : 이전역과 다음역을 출력한다.
        
class line:
    각 라인의 정보를 가진 class
    각 라인의 지하철역들이 저장되어있다.
    변수:
        linename: 라인 이름
        linenum: 속해있는 역 개수
        linelist: 속해있는 역의 list
    함수:
        ret_station(station:str): 입력한 역의 노드를 반환한다.
                                    역이 존재하지 않으면 False를 반환한다.
'''


def subwaySearch(st, end):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            stat = lines[i].linelist[j]
            if stat.name == st:
                st = stat

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            stat = lines[i].linelist[j]
            if stat.name == end:
                end = stat


    # 최소 거리를 탐색합니다
    route = Search(st, end)
    route1 = []
    for i in route:
        if len(i) <= 4:
            route1.append(i)

    route2 = recruSearch(st, end)
    pass

    tem = []
    tem2 = []
    for a in route1:
        i = 0
        for b in range(len(a)):
            if a[b] == st:
                triger = a[-2]
                if a.count(a[-2]) < a.count(a[-3]):
                    triger = a[-3]
            elif a[b] == end:
                if triger == a[-3]:
                    tem2.pop()
                break

            if a[b] == triger:
                tem.append(st)
                tem += a[i+1:b+1]
                tem.append(end)
                tem2.append(tem)
                tem = []
                i = b

    tem = []
    for a in route2:
        i = 1
        outer = []
        inner = []
        now = []
        triger = a[1]
        trigercount = 0
        for b in range(len(a)):
            if triger in a[b:]:
                if triger == a[b]:
                    now.append(a[i:b])
                    i = b
                continue
            else:
                triger = a[b]
                outer.append(now)
                outer = []



    pass

    for a in tem2:
        for b in a:
            if a.count(b) >= 2:
                tem2.remove(a)
                break
    return tem2

def Search(st, end, flag=False, visitedst = []):
    if flag == True:
        return False
    try:
        len(nodes)
    except:
        nodes = []

    # 두 역이 같은 라인인 경우 검색 종료
    if st.line & end.line:
        nodes.append([st, end])
        return nodes

    # node 개수가 홀수인 경우 가운데 역
    # 모든 경우의 수를 검사
    nownodes = [st]
    distance = float('inf')
    nowdistance = 0
    for nowstat in hwanlist:
        if nowstat in visitedst:
            continue
        if len(nowstat.line & st.line) >= 1 and len(nowstat.line & end.line) >= 1:
            # 가운데 역을 찾은 경우 중 거리가 가장 작은 것 만을 저장
            # 거리가 가장 작은지 검사합니다.
            sthwanline = st.line & nowstat.line
            for i in sthwanline:
                i = retLineClass(i)
                temst = i.stInLine(st)
                temend = i.stInLine(nowstat)
                nowdistance = i.howfar(temst, temend)
            endhwanline = end.line & nowstat.line
            for i in endhwanline:
                i = retLineClass(i)
                temst = i.stInLine(nowstat)
                temend = i.stInLine(end)
                nowdistance += i.howfar(temst, temend)

                if nowdistance > distance:
                    continue

            distance = nowdistance
            nownodes.append(nowstat)
            nownodes.append(end)
            nodes.append(nownodes)
            nownodes = [st]

    if not nodes:               #위 두가지 모두 안 되는 경우
        nodes.append(recruSearch(st, end, flag, visitedst=visitedst))    #재귀탐색 실행

    return nodes




def recruSearch(st, end, flag=False, visitedLines=[], visitedst=[]):      #다중탐색
    if flag == True:
        return False
    nodes = []
    # 무한 반복을 피하기 위해 이미 탄 라인은 다시 타지 않음
    for hwanst in hwanlist:
        if st.line & hwanst.line :                  # st역의 환승역을 찾은 경우
            pass
            for i in list(st.line & hwanst.line):   # 겹치는 노선이 여러개일 경우를 대비해 각 노선 전부 검사
                newst = hwanst                      # 다음 st 인자로 환승역을 주기 위해 저장
                if newst.name in visitedst:
                    flag = True                     # 무한반복을 방지하기 위해 빠져나오고 검사가 실패했으니 False를 저장
                visitedLines.append(i)              # 탑승 노선 저장
                visitedst.append(newst.name)

                for endhwanst in hwanlist:
                    if end.line & endhwanst.line:                   # end의 환승역을 찾은 경우
                        pass
                        for j in list(end.line & endhwanst.line):   # 겹치는 노선이 여러개일 경우 각 노선 전부 검사
                            newend = endhwanst                      # 다음 end 인자로 주기 위해 저장
                            if newend.name in visitedst:                   # 이미 방문한 노선인 경우 검색 실패
                                flag = True
                            visitedLines.append(j)
                            visitedst.append(newend.name)
                            nownodes = []                     # 탑승 노선 저장
                            newnodes = flatter(Search(newst, newend, flag, visitedst))    # 새로운 st, end를 이용해 재귀탐색
                            pass
                            if newnodes is False:
                                flag = True

                            if newnodes:
                                for nnodes in newnodes:             # 탐색에 실패한 경우 저장하지 않음
                                    nnodes = flatter(nnodes)
                                    if nnodes == False or False in nnodes:
                                        flag = True
                                    nownodes += nnodes
                            visitedLines.remove(j)
                            visitedst.remove(newend.name)

                            if flag == True:
                                break
                            appendlist = []
                            appendlist.append(st)
                            appendlist += newnodes
                            appendlist.append(end)
                            if len(appendlist) >100:
                                return nodes
                            nodes.append(appendlist)


                visitedLines.remove(i)
                visitedst.remove(newst.name)
                if flag == True:
                    break
            if flag == True:
                break
        if flag == True:
            break




    #     if hwanst.line in visitedLines:
    #         continue
    #     if stline.linename in hwanst.line:
    #         visitedLines.append(stline.linename)
    #         nextst = hwanst
    #     elif endline.linename in hwanst.line:
    #         try:
    #             nextend.stname
    #         except:
    #             visitedLines.append(endline.linename)
    #             nextend = hwanst
    # nownodes.append(nextst)
    # recruSearch(nextst, nextend, visitedLines)
    # nownodes += [nextend, end]
    # nodes.append(nownodes)

    return nodes


def finaldistance(nodes:list) -> int:
    distance = 0

    for i in range(len(nodes) - 1):
        st = nodes[i]
        end = nodes[i + 1]
        line = list(st.line & end.line)
        nowdistance = float('inf')
        if len(line) >= 2:      # 겹치는 노선이 여러개일 경우 더 짧은 경로를 선택
            for nowlinename in line:
                nowline = retLineClass(nowlinename)
                st = nowline.stInLine(st)
                end = nowline.stInLine(end)
                temdistance = nowline.howfar(st, end)
                if temdistance < nowdistance:
                    nowdistance = temdistance
        else:
            nowline = retLineClass(line[0])
            st = nowline.stInLine(st)
            end = nowline.stInLine(end)
            nowdistance = nowline.howfar(st, end)

        distance += nowdistance
    return distance


def printsearch(mode, stlist, specialline = None):


    allRoute = []
    distance = float('inf')
    for i in range(0, len(stlist)-1):
        try:
            allRoute = subwaySearch(stlist[i], stlist[i+1])
            pass
        except:
            continue

    finalRoute = []
    for routes in allRoute:
        if mode != '1':
            temlists = set()
            for i in routes:
                temlists.add(i.line)
            if mode == '2':
                if specialline not in temlists:
                    allRoute.remove(routes)
            if mode == '3':
                if specialline in temlists:
                    allRoute.remove(routes)

    for routes in allRoute:
        nowdistance = finaldistance(routes)
        if nowdistance < distance:
            finalRoute = routes
            distance = nowdistance


    return finalRoute, distance

if __name__ == "__main__":

    while True:
        start = input('출발 역을 입력하세요:')
        if start in stins:
            start = retStationClass(start)
            break
        print('역 이름을 정확하게 다시 입력해주세요.')

    while True:
        end = input('도착 역을 입력하세요:')
        if end in stins:
            end = retStationClass(end)
            break
        print('역 이름을 정확하게 다시 입력해주세요.')

    throughstList = [start]
    through = input('경유역이 있다면 1, 아니라면 2를 입력해주세요:')
    while through not in ['1', '2']:
        if through not in ['1', '2']:
            through = input('다시 입력해주세요.')
    while through == '1':
        while True:
            while True:
                temst = input('경유 역을 입력하세요:')
                if temst in stins:
                    throughstList.append(retStationClass(temst))
                    break
                print('역 이름을 정확하게 다시 입력해주세요.')
            through = input('경유역이 더 있다면 1, 아니라면 2를 입력해주세요.')
            if through != '1':
                break
        if through not in ['1', '2']:
            through = input('다시 입력해주세요.')
    throughstList.append(end)
    print("=================================")
    print(f'출발역 : {start}({start.printline()}), 도착역 : {end}({end.printline()})')
    if through == '1':
        print(f'경유역 : {(lambda i: i for i in through[1:-1])}')

    print('모드를 선택해주세요')
    print('1. 일반 모드')
    print('2. 선호 노선 모드 - 선호하는 노선이 포함된 경로를 검색합니다.')
    print('3. 기피 노선 모드 - 기피하는 노선이 없는 경로를 검색합니다.')
    mode =  input('숫자 입력 >>')
    while mode not in ['1', '2', '3']:
        print('잘못 입력하셨습니다. ')
        mode = input('숫자 입력 >>')
    specialline = None
    if mode in ['2', '3']:
        print("=================================")
        while True:
            if mode == '2':
                specialline = input('선호하는 노선을 입력해주세요:')
            else:
                specialline = input('기피하는 노선을 입력해주세요:')
            if specialline in linenamelist:
                break
            print('노선 이름을 정확하게 다시 입력해주세요.')
        if mode == '2':
            print(f'{specialline}을 포함하는 경로를 검색합니다.')
        else:
            print(f'{specialline}을 포함하지 않는 경로를 검색합니다.')
    print("=================================")
    print('지하철 노선 검색을 시작합니다.')
    modelist = [None, '일반 모드', '선호 노선 모드', '기피 노선 모드']
    print(f'모드 : {modelist[int(mode)]}')

    route = []
    distance = []
    for i in range(len(throughstList)-1): # 경유역까지의 노선을 검색하기 위해
        nowroute, nowdistance = printsearch(mode, [throughstList[i], throughstList[i+1]], specialline)
        pass
        if nowroute:
            route += nowroute[:-1]
            distance.append(finaldistance(route))
            pass
            route.append(end)
    print("=================================")
    print("검색이 완료되었습니다.")
    print('경로를 츨력합니다.')

    kyonst = [i.name for i in throughstList[1:-1]]


    print(f"{'출발역'} : {route[0].name:10}")
    print(f'          |  ')
    for i in range(len(route[1:])):
        if route[i+1].name in kyonst:
            print(f'{"경유역":3} : {route[i+1].name:10}')
            print(f'          |  ')
            continue
        if route[i+1] != end:
            print(f'{"환승역":3} : {route[i+1].name:10}')
            print(f'          |  ')
    print(f"도착역 : {route[-1].name:10}")



