def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)
value_list = [5, False, "Jan"]
value_dict = {"a" : 75, "b" : "summer", "c" : False}
value_list_2 = ["Orange", True]

print_params(a = 1, b = "строка", c = True)
print_params(a = "Apple", b = False, c = 7)
print_params ()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2)
print_params(*value_list_2, 42)
