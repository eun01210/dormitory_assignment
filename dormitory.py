import random # random 모듈 사용
import pygame # pygame 모듈 사용
import numpy as np # numpy 모듈을 np라는 이름으로 사용

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ선행 조건

r4 = open('text\\grade.txt', 'r') # 사람 이름 목록 텍스트를 읽기 모드로 열어 r4에 저장
grade = r4.readlines() # r4의 모든 줄을 배열 형태로 names에 저장 
r4.close() # r 텍스트 닫기
for i in range(0, len(grade)) : # 줄바꿈 기호를 지우기 위한 반복문
    grade[i] = grade[i][:-1] # 마지막 글자를 지워서 저장

r2 = open('text\\hate.txt', 'r') # 싫어하는 텍스트 목록을 읽기모드로 열어서 r2에 저장

hat = "" # 학년/성별 별로 나누기 위한 변수
while True : # 모든 줄을 텍스트 형태로 저장하기 위한 반복문
    line = r2.readline() # r2의 줄을 읽어 line에 저장
    if not line : break # 만약 line이 비어있을 경우(모든 줄을 검사한 경우) 반복문 종료
    hat += line # hat에 line을 추가

r2.close() # r2 텍스트 닫기
hat = hat.split("\n\n") # 학년/성별 별로 나누기
for i in range(0, len(hat)) : # 묶음 개수만큼 반복
    hat[i] = hat[i].split("\n") # 줄바꿈 기호를 기준으로 나누기(싫어하는 쌍 나누기)

hates = [] # 싫어하는 목록을 저장할 배열 선언
for i in range(0, len(hat)) : # 묶음 개수만큼 반복
    hates.append([]) # 배열 공간 생성

for i in range(0, len(hat)) : # 묶음 개수만큼 반복
    for j in hat[i] : # 싫어하는 쌍 수만큼 반복
        hates[i].append(j.split("/")) # /로 구분한 싫어하는 사람을 hates 배열에 저장

r3 = open('text\\cnum.txt', 'r') # 학번 목록을 읽기모드로 열어서 r3에 저장

com = r3.readlines() # r3의 모든 줄을 배열의 형식으로 com에 저장
for i in range(0, len(com)) : # 줄바꿈 기호를 지우기 위한 반복문
    com[i] = com[i][:-1] # 마지막 글자를 지워서 저장

r3.close() # r3 텍스트 닫기

cnum2 = [] # 학번을 저장하는 배열 선언
for i in com : # com의 줄 수만큼 반복
    cnum2.append(i.split("/")) # /로 구분한 학번과 이름을 cnum2에 저장

cnum = {} # 학번을 저장하는 딕셔너리 선언

for i in range(0, len(cnum2)) : # cnum2의 수만큼 반복
    cnum[cnum2[i][0]] = cnum2[i][1] # 딕셔너리에 학번과 이름 쌍을 저장

che = 0 # 임시 변수
rm = [] # 호실 구성원을 배열로 정리하는 배열
ap = {} # 호실이 정해진 사람을 나타내는 딕셔너리

r = open('text\\name.txt', 'r') # 사람 이름 목록 텍스트를 읽기 모드로 열어 r에 저장
names = "" # 학년/성별 별로 나누기 위한 변수
while True : # 모든 줄을 텍스트 형태로 저장하기 위한 반복문
    line = r.readline() # r의 줄을 읽어 line에 저장
    if not line : break # 만약 line이 비어있을 경우(모든 줄을 검사한 경우) 반복문 종료
    names += line # names에 line을 추가

r.close() # r 텍스트 닫기
names = names.split("\n\n") # 학년/성별 별로 나누기
for i in range(0, len(names)) : # 묶음 개수만큼 반복
    names[i] = names[i].split("\n") # 줄바꿈 기호를 기준으로 나누기

dr = open('text\\dornum.txt', 'r') # 기숙사 호실 번호 텍스트를 읽기 모드로 열어 dr에 저장
drnums = "" # 기숙사 번호를 저장하는 배열
while True : # 모든 줄을 텍스트 형태로 저장하기 위한 반복문
    line = dr.readline() # dr의 줄을 읽어 line에 저장
    if not line : break # 만약 line이 비어있을 경우(모든 줄을 검사한 경우) 반복문 종료
    drnums += line # drnums에 line을 추가
dr.close() # dr 텍스트 닫기
    
drnums = drnums.split("\n\n") # 학년/성별 별로 나누기
for i in range(0, len(drnums)) : # 묶음 개수만큼 반복
    drnums[i] = drnums[i].split("\n") # 줄바꿈 기호를 기준으로 나누기(호실 이름)

abcd = [] # ABCD자리를 랜덤으로 배치하기 위한 배열
abcds = ["A", "B", "C", "D"] # ABCD를 반복문으로 담기 위한 배열
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ함수

def change(rmc) : # 호실을 섞는 함수
    global che, r, rm, ho, abcd # 전역 변수 사용

    nam = [] # 임시로 사용할 이름을 담을 배열 선언
    rm = [] # 특정한 ho의 모든 방의 정보를 담을 배열
    abcd = [] # ABCD자리를 랜덤으로 배치하기 위한 배열

    for i in names[ho] : # 해당 학년/성별의 이름을 모두 검사
        if i not in ap : nam.append(i) # 해당하는 이름이 이미 배치된 이름에 없을 경우 추가

    while rmc : # 호실 개수만큼 반복
        rm.append([]) # rm에 빈 배열(호실)을 추가
        rmc -= 1 # 반복문을 위한 변수 감소

    for i in ap : # 호실이 정해져 있는 사람 수만큼 반복
        try : rm[drnums[ho].index(ap[i][:-1])].append(i) # 해당하는 사람을 해당 호실에 추가
        except : pass # try-except문은 해당하는 묶음이 아닌 사람일 경우 오류가 나는 상황을 패스하는 코드

    roomnum = 0 # 몇 번째 호실인지 나타내는 변수

    while len(nam) : # 이름 목록이 남지 않을 때 까지 반복
        if len(rm[roomnum]) >= 4 : # 방이 꽉 차 있는 경우
            roomnum += 1 # 다음 호실로 설정
            if roomnum >= len(rm) : # 모든 호실을 순회한 경우
                roomnum = 0 # 첫 번째 호실로 설정
        else : # 방이 비어있는 경우
            rm[roomnum].append(nam.pop(random.randrange(0, len(nam)))) # 이름 목록에서 무작위로 하나를 추출해서 해당하는 호실에 저장
            roomnum += 1 # 다음 호실로 설정
            if roomnum >= len(rm) : # 모든 호실을 순회한 경우
                roomnum = 0 # 첫 번째 호실로 설정

    che = 1 # 체크 변수를 1로 설정 (여기서는 싫어하는 사람이 붙었는지 확인하기 위함) [0:붙음, 1:안붙음]

    for i in rm : # 모든 호실 확인
        for j in hates[ho] : # 해당 묶음의 싫어하는 사람 쌍을 모두 확인
            if j[0] in i : # 싫어하는 쌍의 한명이 들어있은 경우
                if j[1] in i : # 해당하는 쌍의 다른 한명이 들어있는 경우
                    che = 0 # 체크 변수를 0으로 설정
                    break # 반복문 나가기
        if che == 0 : break # 체크 변수가 0이면 반복문 나가기

    if che != 0 : # 싫어하는 사람이 안 붙은 경우
        for i in range(0, len(rm)) : # 호실 수 만큼 반복
            abcd.append([]) # abcd 자리 파악을 위한 배열을 추가
            for j in range(0, len(rm[i])) : abcd[i].append(abcds[j]) # A,B,C,D를 모두 추가

        for i in range(0, len(rm)) : np.random.shuffle(abcd[i]) # 모든 방의 abcd 순서 섞기
        
        for i in ap : # 호실이 정해져 있는 사람 수만큼 반복
            try : # try-except문은 해당하는 묶음이 아닌 사람일 경우 오류가 나는 상황을 패스하는 코드
                abcd[drnums[ho].index(ap[i][:-1])].remove(ap[i][-1:]) # 해당하는 사람의 알파벳을 삭제
                abcd[drnums[ho].index(ap[i][:-1])].insert(rm[drnums[ho].index(ap[i][:-1])].index(i), ap[i][-1:]) # 해당하는 사람의 알파벳을 그 사람의 자리 번째에 추가
            except : pass # 오류가 날 경우 패스

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ파이 게임

pygame.init() # pygame 초기화

size = (1500, 900) # 크기 설정
board = pygame.display.set_mode(size) # 크기를 기반으로 게임판 설정
pygame.display.set_caption("기숙사 호실 배정 프로그램") # 게임 이름 설정
ndnum = 0 # 현재 표시중인 호실 변수

done = True # 무한 반복을 위한 done 변수를 True로 설정

showt = "" # 입력중인 숫자를 보여주는 변수
nown = "" # 사람 이름을 표시하기 위한 변수
nameche = False # 학번이 입력됐는지 확인하는 변수
ho = -1 # 어느 묶음인지 확인하는 변수
number = "" # 학번을 담는 변수
siz = 0 # 표시되는 호실의 글씨 크기를 결정하는 변수
action = False # 글씨를 점점 크게하는 이펙트가 작동하는지 확인하는 변수

while done : # done이 True일 경우 (무한 반복)
    for event in pygame.event.get() : # 이벤트 인식
        if event.type == pygame.QUIT : # 종료 버튼을 누른 경우
            w = open('text\\data.txt', 'w') # data라는 텍스트파일 생성(원래 있을 경우 삭제 후 생성)
            wt = [] # 호실이 결정된 사람을 담을 배열 생성
            for i in range(0, len(ap)) : wt.append(list(ap.values())[i] + " : " + list(ap.keys())[i] + "\n") # 호실이 결정된 사람 수 만큼 반복 : 해당하는 사람의 호실과 이름을 추가
            wt.sort() # wt배열 정렬
            for i in wt : w.write(i) # wt 배열의 모든 값 검사 : 텍스트파일에 값 쓰기
            done = False # done을 False로 설정 (종료)

        elif event.type == pygame.KEYDOWN : # 키가 눌린 경우
            if event.key == 271 or event.key == 13 : # 엔터를 누른 경우
                if showt in cnum : # 입력중인 글이 학번 목록에 있는 경우
                    nown = cnum[showt] # 사람 이름을 해당 학번의 이름으로 설정
                    nameche = True # 학번이 입력됨
                    number = str(showt) # 학번을 입력중인 글로 설정
                    showt = "" # 입력중인 글 초기화
                    for i in range(0, len(names)) : # 모든 묶음을 확인
                        if nown in names[i] : # 해당하는 이름이 해당 묶음에 있는 경우
                            ho = i # 현재 묶음을 해당 묶음으로 설정
                            break # 반복문 종료
                    if nown in ap : del(ap[nown]) # 해당하는 이름이 호실이 결정된 사람 배열에 있는 경우 : 해당하는 이름 삭제
                    action = True # 글자 커지는 이펙트 시작
                    siz = 0 # 크기를 0으로 설정
                    che = 0 # 싫어하는 사람이 안 붙을 때까지 반복하기 위한 변수 조정
                    while che == 0 : change(len(drnums[ho])) # che가 0일 경우 : 기숙사 재배치
                    for i in range(0, len(rm)) : # 모든 호실 검사
                        for j in range(0, len(rm[i])) : # 모든 자리 검사
                            if rm[i][j] == nown : ap[nown] = drnums[ho][i] + abcd[i][j] # 해당 호실의 해당 자리가 현재 사람이름의 자리인 경우 : 호실이 결정된 사람 목록에 이름과 호실, 자리를 추가
                    
                elif nameche and ho != -1 and not showt : # 다시 엔터를 누른 경우
                    if nown in ap : del(ap[nown]) # 해당하는 이름이 호실이 결정된 사람 배열에 있는 경우 : 해당하는 이름 삭제
                    action = True # 글자 커지는 이펙트 시작
                    siz = 0 # 크기를 0으로 설정
                    che = 0 # 싫어하는 사람이 안 붙을 때까지 반복하기 위한 변수 조정
                    while che == 0 : change(len(drnums[ho])) # che가 0일 경우 : 기숙사 재배치
                    for i in range(0, len(rm)) : # 모든 호실 검사
                        for j in range(0, len(rm[i])) : # 모든 자리 검사
                            if rm[i][j] == nown : ap[nown] = drnums[ho][i] + abcd[i][j] # 해당 호실의 해당 자리가 현재 사람이름의 자리인 경우 : 호실이 결정된 사람 목록에 이름과 호실, 자리를 추가

                else : # 학번을 잘못 입력한 경우
                    nown = "학번을 다시 확인해 주세요." # 표시할 텍스트 설정
                    nameche = False # 학번이 입력되지 않음
                    showt = "" # 입력중인 글 초기화
                    number = "" # 학번 초기화
                    ho = -1 # 묶음 초기화


            elif event.key == pygame.K_BACKSPACE : # 지우기 키를 누른 경우
                if len(showt) >= 1 : showt = showt[:-1] # 입력중인 글이 존재하는 경우 : 글 하나 지우기
            elif 48 <= event.key < 58 : # 0~9까지의 숫자를 입력한 경우
                if len(showt) <= 9 : showt += str(event.key-48) # 입력중인 글이 9글자 이하인 경우 : 해당하는 숫자 추가
            elif 256 <= event.key < 266 : # 0~9까지의 숫자를 입력한 경우(키패드)
                if len(showt) <= 9 : showt += str(event.key-256) # 입력중인 글이 9글자 이하인 경우 : 해당하는 숫자 추가
                            

    board.fill((255,255,255)) # 배경을 흰색으로 채운다
    pygame.draw.rect(board, (0, 0, 0), (500, 700, 500, 70), 10) # 입력란을 나타내는 사각형 그리기
    
    tT = pygame.font.Font('font\\acharismaBk.ttf', 60) # 입력중인/이름+학번 텍스트 폰트
    tTS3 = tT.render(showt, True, (0, 0, 0)) # 입력중인 텍스트 글씨
    tTR3 = tTS3.get_rect() # 입력중인 텍스트 위치
    tTR3.center = (750, 735) # 입력중인 텍스트 위치 설정

    tTS32 = tT.render(nown+" - "+number, True, (0, 0, 255)) # 이름+학번 텍스트 글씨
    tTR32 = tTS32.get_rect() # 이름+학번 텍스트 위치
    tTR32.center = (750, 665) # 이름+학번 텍스트 위치 설정
    if ho != -1 : # 묶음이 정해진 경우
        tTS1 = tT.render(grade[ho], True, (0, 150, 0)) # 어느 묶음인지 표시하는 텍스트 글씨
        tTR1 = tTS1.get_rect() # 어느 묶음인지 표시하는 텍스트 위치
        tTR1.center = (750, 595) # 어느 묶음인지 표시하는 텍스트 위치 설정
        board.blit(tTS1, tTR1) # 어느 묶음인지 표시하는 텍스트 그리기

    if action : # 글자 커지는 이펙트가 작동중인 경우
        siz += 7 # 글자 크기 증가
        if siz >= 350 : action = False # 글자 크기가 350에 도달(초과)한 경우 이펙트 종료

    if ap.get(nown) : # 해당하는 사람의 호실이 결정된 경우
        T1 = pygame.font.Font('font\\acharismaBk.ttf', int(siz)) # 호실 번호 텍스트 폰트
        TS1 = T1.render(ap.get(nown), True, (0, 0, 0)) # 호실 번호 텍스트 글씨
        TR1 = TS1.get_rect() # 호실 번호 텍스트 위치
        TR1.center = (750, 250) # 호실 번호 텍스트 위치 설정
        board.blit(TS1, TR1) # 호실 번호 텍스트 그리기

    board.blit(tTS3, tTR3) # 입력중인 텍스트 그리기
    board.blit(tTS32, tTR32) # 이름+학번 텍스트 그리기

    pygame.display.flip() # 게임판을 그린다
    pygame.time.delay(10) # 딜레이 설정 (0.01초)
