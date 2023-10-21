from operator import add, mul

# Write your code here for Q1 and Q2





#############################################
# Q3

square = lambda x: x + x

sqrt = lambda x: x ** 0.5 # x^0.5 == √x

def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"
    
    total = 0
    for num in numbers:
        total += num

    return total // len(numbers)


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers) 
    # `sorted` returns a sorted list. `sorted` works. 
    if len(numbers) % 2 == 0:
        left_mid = len(numbers) // 2
        right_mid = left_mid + 1
        return mean([left_mid, right_mid])
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[running_high_num] = 0
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > counts[running_high_num]:
            running_high_num = num

    return running_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers:
        total_dist += square(num - avg)

    return sqrt(total_dist / len(numbers))


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    info = {}
    info["mean"] = mean(numbers)
    info["median"] = median(numbers)
    info["mode"] = mode(numbers)
    info["std_dev"] = std_dev(numbers)
    return info
    

#############################################
# (OPTIONAL) Write your code here for Invert and Change
