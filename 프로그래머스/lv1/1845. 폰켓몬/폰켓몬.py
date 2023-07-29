def solution(nums):
    monster = {}
    for n in nums:
        if n in monster:
            monster[n] += 1
        else:
            monster[n] = 1
    print(monster)
    max_type_size = int(len(nums) / 2)
    monster_type_size = 0
    for _ in monster:
        monster_type_size += 1
        
    if monster_type_size >= max_type_size:
        return max_type_size
    else:
        return monster_type_size