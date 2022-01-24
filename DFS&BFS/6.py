def solution(progresses, speeds):
    answer = []
    done = []
    cnt = 0
    #작업이 완료되는 날짜 구하기
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            done.append((100 - progresses[i]) // speeds[i])
        else:
            done.append((100 - progresses[i]) // speeds[i] + 1)

    #작업 완료처리하기.
    for day in range(max(done)):
      for i, val in enumerate(done):
          toggle= True
          #일수마다 값 줄이기
          if done[i] != 0:
              done[i] = val - 1
            #맨 앞의 작업이 끝났다면
      if done[0] == 0:
          cnt = 1
          #뒤 작업 만큼 카운트
          for i in range(1, len(done)):
            print("i값:",i,done[i])
              #만약 뒤의 작업이 안끝났으면
            if done[i] <= 0 and toggle:
                print("통과")
                #카운트 종료
                cnt += 1
            elif done[i] > 0:
              toggle=False
          #작업이 아직 남아있다면
          if len(done) > 0:
              answer.append(cnt)
              del done[:cnt]
              cnt = 0

    return answer