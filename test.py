from itertools import combinations


my_list = ["A", "B", "C", "D"]

for i in range(len(my_list)):
    for item in combinations(my_list, i):
        keyword = " ".join(word for word in item)
        print(keyword)
