def reverse_map(map:dict)->dict:
    rmap = {}
    for key,value in map.items():
        rmap.update({value:key})
    return rmap