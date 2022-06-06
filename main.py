import itertools

from 선로정리3 import *
import subway

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
    route2 = recruSearch(st, end)
    return route + route2

def Search(st, end):
    # node의 맨 첫번째에 st역을 넣습니다.
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
        nodes.append(recruSearch(st, end))    #재귀탐색 실행

    return nodes




def recruSearch(st, end, visitedLines=[]):      #다중탐색
    nodes = []
    # 무한 반복을 피하기 위해 이미 탄 라인은 다시 타지 않음
    for hwanst in hwanlist:
        if st.line & hwanst.line :                  # st역의 환승역을 찾은 경우
            for i in list(st.line & hwanst.line):   # 겹치는 노선이 여러개일 경우를 대비해 각 노선 전부 검사
                newst = hwanst                      # 다음 st 인자로 환승역을 주기 위해 저장
                if i in visitedLines:               # 지금 검사하는 노선이 이미 탄 라인인 경우
                    return False                # 무한반복을 방지하기 위해 빠져나오고 검사가 실패했으니 False를 저장
                visitedLines.append(i)              # 탑승 노선 저장

                for endhwanst in hwanlist:
                    if end.line & endhwanst.line:                   # end의 환승역을 찾은 경우
                        for j in list(end.line & endhwanst.line):   # 겹치는 노선이 여러개일 경우 각 노선 전부 검사
                            newend = endhwanst                      # 다음 end 인자로 주기 위해 저장
                            if j in visitedLines:                   # 이미 방문한 노선인 경우 검색 실패
                                return False
                            visitedLines.append(j)
                            nownodes = []                     # 탑승 노선 저장
                            newnodes = Search(newst, newend)    # 새로운 st, end를 이용해 재귀탐색


                            for nnodes in newnodes:             # 탐색에 실패한 경우 저장하지 않음
                                nnodes = flatter(nnodes)
                                if False in nnodes:
                                    continue
                                nownodes += nnodes
                            visitedLines.remove(j)


                            appendlist = [st]
                            appendlist += nnodes
                            appendlist.append(end)
                            nodes.append(appendlist)




                visitedLines.remove(i)
    return nodes




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

        if len(line) >= 2:
            nowdistance = float('inf')
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


if __name__ == "__main__":

    while True:
        start = input('출발 역을 입력하세요:')
        if start in stins:
            break
        print('역 이름을 정확하게 다시 입력해주세요.')

    while True:
        end = input('도착 역을 입력하세요:')
        if end in stins:
            break
        print('역 이름을 정확하게 다시 입력해주세요.')

    throughstList = [start]
    through = input('경유역이 있다면 1, 아니라면 2를 입력해주세요:')
    while True:
        throughstList.append(input('역 이름을 입력해주세요:'))
        through = input('경유역이 더 있다면 1, 아니라면 2를 입력해주세요.')
    throughstList.append(end)
    print("=================================")
    print(f'출발역 : {st}({st.printline()}), 도착역 : {end}({end.printline()})')
    if throughstList:
        print(f'경유역 : {" ".join(throughstList)}')

    print('모드를 선택해주세요')
    print('1. 일반 모드')
    print('2. 선호 노선 모드 - 선호하는 노선이 포함된 경로를 검색합니다.')
    print('3. 기피 노선 모드 - 기피하는 노선이 없는 경로를 검색합니다.')
    mode = input('숫자 입력 >>')
    while mode not in range(1, 4):
        print('잘못 입력하셨습니다. ')
        mode = input('숫자 입력 >>')
    print("=================================")
    print('지하철 노선 검색을 시작합니다.')
    modelist = [None, '일반 모드', '선호 노선 모드', '기피 노선 모드']
    print(f'모드 : {modelist[mode]}')
    printsearch(mode, throughstList, specialline)


def printsearch(mode,stlist, specialline = None):

    allDistance = []
    allRoute = []
    for i in range(1, len(stlist)):
        allRoute = subwaySearch(stlist[i-1], stlist[i])
    for i in allRoute:
        allDistance.append(finaldistance(i))

    distance = float('inf')
    if mode == 1:           #일반검색
        for i in allRoute:
            finalRoute = allDistance.index(min(allDistance))
            finalDistance = min(allDistance)
    elif mode == 2:         #선호 노선 검색
        for i in allRoute:
            nowdistance = finaldistance(i)
            for j in range(len(i)):
                if j == range(len(i)):
                    print(f'{[specialline]}를 포함하는 노선이 없습니다.')
                    print('종료합니다.')
                    return False
                if specialline in i[j].line:
                    if distance > nowdistance:
                        distance = nowdistance
                        nowroute = i
        finalRoute = i
        finalDistance = distance

    elif mode == 3:
        for i in allRoute:
            nowdistance = finaldistance(i)
            for j in range(len(i)):
                if j == range(len(i)):
                    print(f'{[specialline]}를 포함하지 않는 노선이 없습니다.')
                    print('종료합니다.')
                    return False
                if specialline not in i[j].line:
                    if distance > nowdistance:
                        distance = nowdistance
                        nowroute = i
        finalRoute = i
        finalDistance = distance

    print()


