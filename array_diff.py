def array_diff(a, b):
    #your code here
    return_list = []
    for i in a:
        if i not in b:
            return_list.append(i)
    return return_list