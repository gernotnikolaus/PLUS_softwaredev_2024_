import random
def randomList(ran_range):
    count = 10
    counter = 0
    random_range = ran_range
    random_list = []

    while(counter < count):
        random_list.append(random.randint(0, random_range))
        counter = counter + 1

    print(random_list)
    print()
    print("min of the list: " + str(min(random_list)))
    print("max of the list: " + str(max(random_list)))
    print("sum of the list: " + str(sum(random_list)))
    print()
    print("length of the list: " + str(len(random_list)))
    print("sorted of the list: " + str(sorted(random_list)))
