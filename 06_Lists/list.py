# refrence by Dhruv Prajapati
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

l1 = [10, 15, 3, 7]

k = 17

def isSumOfList(l, k):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i]+l[j]==k:
                return 1
    else:
        return 0

print(isSumOfList(l1, k))
