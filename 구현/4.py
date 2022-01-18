#알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어짐
#이떄 모든 알파뱃을 오름차순 정렬하고 출력하고 뒤에 모든 숫자를 더한값을 이어서 출력해라.
#예를들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력


inputStr = input()

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 

resultAlpha = []
result = 0
for inputIdx,inputVal in enumerate(inputStr):
    if inputVal in alphabet:
      resultAlpha.append(inputVal)
    else :
      result+=int(inputVal)
resultAlpha.sort()

print("".join(resultAlpha)+str(result))


#x.isalpha() 라는 알파벳 판별 함수 있음.... ㅠ