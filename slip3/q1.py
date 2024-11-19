#add and remove element from set

my_set = set()

def add_element(element):
    my_set.add(element)
    print(f"{element} is added in set \n new set is {my_set}\n")

def remove_element(element):
    my_set.remove(element)
    print(f"{element} is removed from set \n new set is {my_set}\n")

add_element(45)
add_element(20)
add_element(15)
add_element(35)
remove_element(15)
    