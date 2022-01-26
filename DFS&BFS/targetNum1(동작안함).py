# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# 입출력 예 설명
# 문제에 나온 예와 같습니다.

#https://programmers.co.kr/learn/courses/30/parts/12077

def solution(numbers, target):
    totalNumbers = sum(numbers)
    answer = 0
    
    for idx1,num in enumerate(numbers):
        for idx2,num2 in enumerate(numbers):
            #조건 1 같은 숫자면 continue       
            #조건 3 idx가지씩 카운트
            calValue = cal1(totalNumbers,numbers,idx1,idx2+1)
            #print("idx1 :",idx1,"idx : 2",idx2)
            #print(calValue)
            if target == calValue:
                answer+=1
            #print("idx1 :",idx1, "idx2 :", idx2)
            #조건 4 idx번째와 idx+idx2합해서 카운트
            calValue = cal2(totalNumbers,numbers,num,num2)
            if target == calValue:
                answer+=1
                
            calValue = cal3(totalNumbers,numbers,idx1,idx2+1)
            if target == calValue:
                answer+=1
                
            calValue = cal4(totalNumbers,numbers,idx1,idx2+1)
            if target == calValue:
                answer+=1
                
            calValue = cal5(totalNumbers,numbers,idx1,idx2+1)
            if target == calValue:
                answer+=1
                
            calValue = cal6(totalNumbers,numbers,idx1,idx2+1)
            if target == calValue:
                answer+=1

    return answer

def cal1(totalNumbers,numbers,idx,idx2): 
    return totalNumbers - (sum(numbers[idx:idx2]) * 2)

def cal2(totalNumbers,numbers,num,num2):
    return totalNumbers - ((num+num2)*2)


def cal3(totalNumbers,numbers,idx,idx2):
    return totalNumbers - (numbers[idx] + (sum(numbers[(idx+1):idx2]))* 2)

def cal4(totalNumbers,numbers,idx,idx2): 
    return totalNumbers - (numbers[-idx] + (sum(numbers[-(idx+1):-idx2]))* 2)

def cal5(totalNumbers,numbers,idx,idx2):
    return totalNumbers - (numbers[(idx2-1)] + (sum(numbers[(idx+1):idx2]))* 2)

def cal6(totalNumbers,numbers,idx,idx2):
    return totalNumbers - (numbers[-(idx2-1)] + (sum(numbers[-(idx+1):-idx2]))* 2)