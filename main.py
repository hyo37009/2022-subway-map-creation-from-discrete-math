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

    # 최소 거리를 탐색합니다
    route = recruSearch(st, end)

    # 디버깅용 출력
    for i in route:
        for j in i:
            print(f'{j}({" ".join(j.line)})', end=' ')
        print(f'거리 : {finaldistance(i)}')


def recruSearch(st, end, visitedLines=[]):
    # node의 맨 첫번째에 st역을 넣습니다.
    try:
        len(nodes)
    except:
        nodes = []

    # 모든 경우의 수를 확인합니다
    for stline in st.line:
        if stline not in visitedLines:
            stline = retLineClass(stline)
            for endline in end.line:
                endline = retLineClass(endline)
                break
            break
        return nodes

    # while True:
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
            visitedLines.append(nowstat.line)
            nownodes.append(end)
            nodes.append(nownodes)
            nownodes = [st]

    # #node개수가 짝수인 경우 재탐색
    # nownodes = [st]
    # visitedLines = [stline, endline]
    # for hwanst in hwanlist:
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
    #
    return nodes


def finaldistance(nodes:list) -> int:
    for i in range(len(nodes) - 1):
        st = nodes[i]
        end = nodes[i + 1]
        line = list(st.line & end.line)
        distance = 0

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
