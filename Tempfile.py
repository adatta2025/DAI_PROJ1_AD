"""subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV Serials', 'Netflix']

def create_sent1():
    for val0 in subjects:
        for val1 in verbs:
            for val2 in objects:
                print(val0, val1, val2)
            print()
        print()

create_sent1()

def create_sent2():
    list1 = [''.join(val0+val1+val2) for val0 in subjects for val1 in verbs for val2 in objects]
    print(list1)

create_sent2()

def compute():
    num = input("Enter any digit between 2-9")
    sum = int(num) + int(num*2) + int(num*3) + int(num*4)
    print(sum)

compute()

from math import pi
lst1 = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]
lst2 = list(map(lambda rad:round(pi*rad*rad, 2), lst1))
print(lst2)

nums = [10, 20, 30, 40, 50, 60, 70, 80]
strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
lst1 = list(map(lambda x, y: (x , y), nums, strs))
print(lst1)

def dict_fn(dict1):
    if dict1[1] > 40:
        return dict1[0]
    else:
        return None

dict1 = {"Rohan":85, "Shail":55, "Sahil":35, "Vikram":22, "John":78}
lst1 = list(filter(dict_fn, dict1.items()))
lst2 = [lst1[idx][0] for idx,val in enumerate(lst1)]
print(lst2)

list1 = ["Rohan", "Shailesh", "Sahil", "Vikramaditya", "John", "Nirupama"]
list2 = list(filter(lambda str1:len(str1) >=8, list1))
print(list2)

lst = ['Benevolent', 'Dictator', 'For', 'Life']
str1 = ' '.join(lst)
print(str1)

list1 = ["Rohan", "Shailesh", "Sahil", "Vikramaditya", "John", "Nirupama"]
lst1 = list(map(lambda str1: str1.upper(), list1))
print(lst1)

def fun():
    try:
        return 10
    finally:
        return 20
k=fun()
print(k)"""

