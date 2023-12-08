def fn_binary_search(result_fn, start_val, success_fn, max_val = None, max_find_multiple = 10, output = False):
    left = start_val
    if max_val is None:
        right = 0
        val = max_find_multiple
    else:
        right = max_val
        val = (left + right) // 2
    left_result = None
    right_result = None
    while True:
        result = result_fn(val)
        success = success_fn(result)
        if success:
            right = val
            right_result = result
        else:
            left = val
            left_result = result
        if output:
            print(f'Trying {val}, result {result}, success {success} [{left}, {right}]')
        if right == 0:
            val *= max_find_multiple
            continue
        if right - left <= 1:
            return left, right, left_result, right_result
        val = (left + right) // 2
