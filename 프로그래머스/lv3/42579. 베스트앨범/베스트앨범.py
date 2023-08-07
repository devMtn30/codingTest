def solution(genres, plays):
    genreDic = {} #장르 종류별 고유번호
    totalDic = {} #장르별 플레이 합계
    for i in range(len(genres)):
        if genres[i] in genreDic.keys() and genres[i] in totalDic.keys():
            genreDic[genres[i]].append(i) #장르 종류가 몇번째 고유번호인지 담음
            totalDic[genres[i]] += plays[i]
        else:
            genreDic[genres[i]] = [i]
            totalDic[genres[i]] = plays[i]
    print(genreDic)
    print(totalDic)
    answer = []
    
    #totalDic를 가장 높은 값 순으로 정렬
    for i in genreDic:
        genreDic[i] = [k for _,k in sorted(zip([plays[j] for j in genreDic[i]], genreDic[i]),key= lambda x: x[0], reverse=True)]
        print(genreDic[i])
    
    sortGenre = sorted(totalDic.items(), key= lambda item:item[1], reverse=True)
    for genre in sortGenre: #가장 인기가 많은 장르순으로 정렬된 튜플
        #print(genre[0])
        cnt = 0
        #print(genreDic[genre[0]])
        for res in genreDic[genre[0]]: #장르별 2개씩 저장
            if cnt < 2: 
                answer.append(res)
            cnt += 1
    return answer