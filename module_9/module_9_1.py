def apply_all_func(int_list, *functon):
    dict_res = {}
    for func in functon:
        dict_res[func.__name__] = func(int_list)

    return dict_res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
