def add_list(List) :
    Sum = 0.0
    for i in List:
        Sum += i

    return Sum

def balance(List) :
    total = add_list(List)
    Sum = 0.0
    i = 0
    while Sum < total/2.0:
        Sum += List[i]
        i += 1

    i = i-1
    Sum -= List[i]
    diff = total/2.0 - Sum
    return float(i) + diff/float(List[i])

List = [1,2,3,78]
print(List,balance(List))
