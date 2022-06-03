def postive_negative(*args):
    positives = 0
    negatives = 0
    for c in args:
        if c > 0:
            positives += c
        else:
            negatives += c
    return positives, negatives


numbers = [int(x) for x in input().split(' ')]
positives, negatives = postive_negative(*numbers)
print(negatives)
print(positives)

if abs(positives) > abs(negatives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")