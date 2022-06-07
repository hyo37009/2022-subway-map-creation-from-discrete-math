class station:
    '''
    역에 대한 class입니다
    '''

    def __init__(self, name: str, line: list):
        self.name = name
        self.line = set(line)
        self.hwan = False
        self._neighbor = [None, None]

    def __str__(self):
        return self.name

    def is_lineN(self, n: str):
        '''
        :param n: 검사하고 싶은 라인
        :return: 라인에 속해있다면 True
        '''
        return n in self.line

    def connection(self, station: str, prev=0):
        '''
        각 노드를 그래프로 잇는 작업
        :param station: 연결할 노드
        '''
        if prev:
            self._neighbor[0] = station
        elif not prev:
            self._neighbor[1] = station
        else:
            raise KeyError('0 또는 1만을 입력하셈')
        return True

    def prevStation(self):
        return self._neighbor[0]

    def nextStation(self):
        return self._neighbor[1]

    def printconnection(self):
            return str(self.prevStation(), self.nextStation())

    def printline(self):
        return ", ".join(self.line)



class line:
    '''
   각 line에 대한 역을 순차적으로 갖는 class
   '''
    hwan = ['소사', '검암', '신당', '광운대', '석촌', '영등포구청', '창동', '연신내', '고속터미널', '노량진', '총신대입구(이수)', '여의도', '동대문', '회룡', '안산', '도봉산', '원인재', '사당', '인천공항1터미널', '김포공항', '교대(법원·검찰청)', '망우', '한대앞', '까치산', '올림픽공원(한국체대)', '인천', '부평', '을지로3가', '오금', '서울역', '중앙', '청량리', '중랑', '효창공원앞', '건대입구', '동묘앞', '동작(현충원)', '불광', '옥수', '공덕', '을지로4가', '강남', '판교(판교테크노밸리)', '충무로', '태릉입구', '종로3가', '디지털미디어시티', '충정로(경기대입구)', '당산', '노원', '천호(풍납토성)', '석계', '신도림', '양재(서초구청)', '회기', '청구', '신촌', '정자', '동대문역사문화공원', '마곡나루', '합정', '부평구청', '주안', '초지', '삼각지', '기흥(백남준아트센터)', '약수', '도곡', '신길', '시청', '대림(구로구청)', '가산디지털단지', '송정', '오이도', '미금(분당서울대병원)', '보문', '신길온천', '고잔', '계양', '신내', '상봉', '왕십리', '신설동', '용산', '모란', '잠실(송파구청)', '가락시장', '강남구청', '종합운동장', '홍대입구', '수원', '선릉', '정왕', '군자(능동)', '대곡', '금정', '인천시청', '양평', '수서']


    def __init__(self, linename, linenum):
        self.linename = linename
        self.linenum = linenum
        self.linelist = [None] * linenum

    def __len__(self):
        return self.linenum

    def setline(self, line:list):
        for i in range(self.linenum):
            #station class를 생성합니다(double connected node)
            self.linelist[i] = station(line[i], [self.linename])
        for i in range(self.linenum):
            if i != 0 and i != len(self.linelist)-1:
                #연결관계를 설정합니다
                self.linelist[i].connection(self.linelist[i-1], 0)
                self.linelist[i].connection(self.linelist[i+1], 1)
            if i == 0:
                self.linelist[i].connection(self.linelist[i+1], 1)
            if i == len(self.linelist)-1:
                self.linelist[i].connection(self.linelist[i-1], 0)

            #환승역 여부를 저장합니다.
            if self.linelist[i].name in self.hwan:
                self.linelist[i].hwan = True

    def linetree(self, line:list, connected:str):
        '''
        라인이 가지로 뻗어 나오는 경우의 노드 설정입니다
        :param line: 새로 추가되는 line의 list입니다
        :param connected: 연결되는 노드 이름입니다
        '''
        for i in range(len(line)):
            self.linelist.append([None])
        connectedStation = None
        for i in self.linelist:
            if i.name == connected:
                connectedStation = self.linelist.index(i)
                break
        if connectedStation is None:
            raise ValueError(f'{connected} is not in line')

        for i in range(len(line)):
            # station class를 생성합니다
            self.linelist[self.linenum + i] = station(line[i], [self.linename])
            # 노선 구분을 위해 환승가능역으로 설정합니다
            self.linelist[connectedStation].hwan = True
        for i in range(len(line)):
            #연결관계를 설정합니다
            if i == 0:
                self.linelist[self.linenum + i].connection(self.linelist[connectedStation], 0)
                self.linelist[i].connection(self.linelist[i + 1], 1)
            elif i == self.linenum + len(line):
                self.linelist[self.linenum + i].connection(self.linelist[self.linenum + i - 1], 0)
            else:
                self.linelist[i].connection(self.linelist[i-1], 0)
                self.linelist[i].connection(self.linelist[i+1], 1)
        self.linenum += len(line)

    def ret_station(self, station):
        if type(station) == int:
            return self.linelist[station]
        for i in range(len(self.linelist)):
            if self.linelist[i].name == station:
                return self.linelist[i]
        return False

    def stInLine(self, st):
        try:
            st = st.name
        except:
            pass

        for i in self.linelist:
            if i.name == st:
                return i
        return False

    def howfar(self, st1:station, st2:station):
        if type(st1) != station or type(st2)!= station:
            raise ValueError('입력값이 station이 아닙니다')

        num1 = self.linelist.index(st1)
        num2 = self.linelist.index(st2)
        return abs(num1 - num2)