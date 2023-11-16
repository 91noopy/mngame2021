def intro() :
    print("반갑습니다! ")
    gs = input("""게임코드를 입력하세요
               숫자야구 :: baseball
               업다운 :: updown
               가위바위보 :: rsp 
               베스킨라빈스 31 :: bsk...""") #초기화면
    if gs == "baseball" :
        baseball()
    elif gs == "updown":
        UD()
    elif gs == "rsp" :
        rsp()
    elif gs == "bsk" :
        bsk()


#baseball
def ask():
    defense = input("THROW!!") #팀1의 투구
    print ("\n" * 30) #띄어쓰기
    attack = input("HIT!!") #팀2의 스윙
    return defense, attack

def baseball():
    #팀이름 설정
    print(""" === BASEBALL WITH NUMBER ===
     
     #게임 규칙
     -선공 , 후공으로 팀을 나눠 1:1로 경기를 진행한다
     -후공팀 먼저 수비(THROW) 차례에 중복되지 않는 네 자릿수를 입력한다
     -공격(HIT) 차례에 수비팀이 입력한 수를 유추하여 입력한다
     -같은 자릿수/같은 수 매칭에 성공할 경우 1점, 그렇지 못할 경우 0점 카운트된다.
     -세 번 매칭에 실패할 경우 쓰리아웃으로 공수가 교체된다.
     -4차례 매칭 후, 점수가 더 높은 팀의 승리! 


    """)
    Team1 = input("선공팀의 이름을 설정하시오.")
    Team2 = input("후공팀의 이름을 설정하시오.")

    #1회차
    score1 = 0
    score2 = 0
    D,A = ask()
    
    out = 0
    DISPLAY_NUM = ["ONE","TWO","THREE"]
    for i in range(4):
        if A[i] != D[i]:
            out += 1
            print(f'\n{DISPLAY_NUM[out-1]} OUT!!')
            if out==3:
                print("\n\nCHANGE!")
                break
        if A[i] == D[i]: score2 += 1
    
    D,A = ask()
    out = 0
    DISPLAY_NUM = ["ONE","TWO","THREE"]
    for i in range(4):
        if A[i] != D[i]:
            out += 1
            print(f'\n{DISPLAY_NUM[out-1]} OUT!!\n')
            if out==3:
                print("\n\nCHANGE!")
                break
        if A[i] == D[i]: score1 += 1
    
    D,A = ask()
    out = 0
    DISPLAY_NUM = ["ONE","TWO","THREE"]
    for i in range(4):
        if A[i] != D[i]:
            out += 1
            print(f'{DISPLAY_NUM[out-1]} OUT!!')
            if out==3:
                print("CHANGE!")
                break
        if A[i] == D[i]: score2 += 1

    D,A = ask()
    out = 0
    DISPLAY_NUM = ["ONE","TWO","THREE"]
    for i in range(4):
        if A[i] != D[i]:
            out += 1
            print(f'\n{DISPLAY_NUM[out-1]} OUT!!\n')
            if out==3:
                print("\n\nCHANGE!")
                break
        if A[i] == D[i]: score1 += 1

    if score1 > score2:
        print(Team1 + "팀의 승리! 축하합니다!")
    elif score2 > score1:
        print(Team2 + "팀의 승리! 축하합니다!")
    elif score1 == score2:
        print("무승부!")






#RSP
def rsp() :
    import random

    print ('가위바위보 게임을 시작합니다.')
    print ('만약 그만하고 싶다면 그만할래 라고 입력하세요.')
    game = ['가위', '바위', '보']
    count = 0
    win = 0

    while 1 :
        computer = random.choice(game)
        answer = input('무엇을 내시겠습니까?')

        if answer == '그만할래' :
            break

        count = count +1

        print('컴퓨터: ' + computer)
        print('나: ' + answer)

        if computer == '가위' :
            if answer == '가위' :
                print('tie')
            elif answer == '바위' :
                print('win')
                win = win +1
            elif answer == '보' :
                print('lose')
        elif computer == '바위' :
            if answer == '가위' :
                print('lose')
            elif answer == '바위' :
                print('tie')
            elif answer == '보' :
                print('win')
                win = win+1
        elif computer == '보' :
            if answer == '주먹':
                print('lose')
            elif answer == '보' :
                print('tie')
            elif answer == '가위':
                print('win')
                win = win+1
    print(count,'번 승부 중',win,'번 이겼습니다.')

    if count-win<win :
        print('축하드립니다! 당신이 승리하였습니다٩( ᐛ )و')
    else :
        print('아쉽지만 당신은 졌습니다. 다시 도전해보세요 (๑ó⌓ò๑)')



        



#31
def bsk():
    import random

    print('베스킨라빈스 31게임')
    print('1부터 31까지의 숫자를 번갈아 불러 31을 부르는 사람이 지는 게임 입니다.')

    number = 0

    turn = 0
    while True :
        if turn == 0 :
            p1 = int(input('p1 부를 숫자의 개수를 입력하세요 (1 ~ 3):'))
            for _ in range(p1):
                number += 1
                print('p1:',number)

            turn +=1
            turn %=2
        elif turn == 1:
            p2 = random.randint(1,3)
            for _ in range(p2):
                number += 1
                print('p2', number)
            
            turn += 1
            turn %= 2
        if number >= 31:
            break


#UD
def UD() :
    import random

    rn = random.randrange(1, 101, 1)
    num = -1

    t_cnt = 0

    print("1~100 숫자 Up&Down 게임을 시작합니다 !!!")
    print("---------------------------------------")
    while(rn != num):

        num = int(input("1~100사이의 숫자를 입력하세요 :"))

        if (num>rn):
            print("Down")
        elif(num>rn):
            print("Up")

        t_cnt += 1
    print("---------------------------------------")
    print(t_cnt, "번 만에 정답을 맞추셨습니다.")

intro()

