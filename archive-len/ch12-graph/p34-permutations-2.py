data = [1, 2, 3]


# nPn

def permute(_stack):
    for d in data:
        if d not in _stack:
            # pushed_stack = _stack + [d]
            # _stack.append(d)
            # permute(_stack)
            permute(_stack + [d])
            _stack
            # _stack.pop()

    if len(_stack) == len(data):
        result.append(_stack)

    return result


nums = [1, 2, 3]
result = []
permute = permute(nums)
print(permute)
