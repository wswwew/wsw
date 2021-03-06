from random import randint

def qsort(seq):
    if len(seq)<2:
        return seq
    smaller=[]
    larger=[]
    middle=seq[0]
    for i in seq[1:]:
        if i <= middle:
            smaller.append(i)
        else:
            larger.append(i)
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums=[randint(1,100) for i in range(10)]
    print(nums)
    print(qsort(nums))