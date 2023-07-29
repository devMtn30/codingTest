def solution(phone_book):
    dic = {}
    
    for num in phone_book:
        dic[num] = 1
    
    for tel in phone_book:
        num = ""
        for i in tel:
            num += i
            
            if tel != num and num in dic:
                return False;
    
    return True
    