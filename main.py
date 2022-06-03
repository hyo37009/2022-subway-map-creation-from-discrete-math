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
    print("=================================")
    print('지하철 노선 검색을 시작합니다.')
    print(f'출발역 : {st}({st.printline()}), 도착역 : {end}({end.printline()})')

    #최소 거리를 탐색합니다
    route = []

    #시작역과 도착역이 같은 라인인 경우
    #단일라인추적
    for i in st.line:
        if i in end.line:
            nowline = retLineClass(i)
            nowst = nowline.stInLine(st)
            nowend = nowline.stInLine(end)
            nowroute = []
            nowstat = nowst

            #방향 결정
            distance = nowline.howfar(nowst, nowend)
            if distance < 1:
                derection = 1
                distance *= -1
            else:
                derection = 0

            for j in range(distance):
                nowroute.append(nowstat.name)
                nowstat = nowstat._neighbor[derection]
            nowroute.append(nowend.name)
            route.append(nowroute)

    #시작역과 도착역의 라인이 다른 경우
    #다중노선 경로를 추적합니다.
        else:
            route.append(recruSearch(st, end))
            # nowroute = []
            # nowstat = st
            # nowline = retLineClass(st.printline())
            # for i in range(len(multiLine) - 1):
            #     distance = nowline.howfar(multiLine[i], multiLine[i+1])
            #     if distance < 1:
            #         derection = 1
            #         distance *= -1
            #     else:
            #         derection = 0
            #
            #     for j in range(distance):
            #         nowroute.append(nowstat.name)
            #         nowstat = nowstat._neighbor[derection]
            # nowroute.append(end.name)



    for i in route:
        for j in i:
            print(j)


def recruSearch(st, end):
    #node의 맨 첫번째에 st역을 넣습니다.
    try:
        len(node)
    except:
        node = []
        visitedLines = []

    #모든 경우의 수를 확인합니다
    for stline in st.line:
        stline = retLineClass(stline)
        for endline in end.line:
            endline = retLineClass(endline)
            break
        break

    # 두 역이 같은 라인인 경우 검색 종료
    if stline.linename == endline.linename:
        node.append([st, end])
        return node

    # node 개수가 홀수인 경우 가운데 역
    nownodes = [st]
    hwanline = st.line.union(end.line)
    for nowstat in hwanlist:
        if len(set(hwanline) & nowstat.line) >= 2:
            #가운데 역을 찾은 경우 경로를 모두 찾은 것이므로 return
            nownodes.append(nowstat)
            visitedLines.append(hwanline.linename)
            break
    nownodes.append(end)
    node.append(nownodes)




    #node개수가 짝수인 경우 재탐색
    nownodes = [st]
    for hwan in hwanlist:
        if stline.linename in hwan.line:
            nextst = hwan
        elif endline.linename in hwan.line:
            nextend = hwan
    nownodes.append(nextst)
    recruSearch(nextst, nextend)
    nownodes.append(nextend)
    nownodes.append(end)
    node.append(nownodes)
    return node




if __name__ == "__main__":

    while True:
        start = input('시작 역을 입력하세요:')
        if start in stins:
            break
        print('역 이름을 정확하게 다시 입력해주세요.')

    while True:
        end = input('도착 역을 입력하세요:')
        if end in stins:
            break
        print('역 이름을 정확하게 다시 입력해주세요.')

    subwaySearch(start, end)