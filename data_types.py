print(type(3))
print(type(3.13))
print(type(3.13 + 1j))
print(type('abc'))
print(type(True))
print(type(None))
print(int(3.13))

print(int(float('3.13')))

a_string = 'Abc xyz' # immutable
a_new_string = a_string.replace('xyz', 'cde')
print(a_new_string)
print(a_string)
print(a_string[0])
print(a_string[1])
print(a_string[2])
# print(a_string[3]) # causes error

print(a_string.count('a'))
print(a_string.count('d'))
print(a_string.find('a'))
print(a_string.istitle())
print(a_string.upper())

an_int = 0
an_int2 = -1
an_int3 = 100

a_float = 1.234
a_complex = 1 + 2j
a_list = [1, 2, 3, 1, 'abc', True, None]  # mutable, indexed, duplicates allowed
# a_list.
print(a_list)
a_list[0] = 4
print(a_list)

a_tuple = (1, 2, 3, 1, 'abc', True, None)  # immutable, indexed, duplicates allowed

print(a_tuple)
# a_tuple[0] = 4
# print(a_tuple)

a_set = {1, 2, 3, 'abc', True, None}  # mutable, non-indexed, duplicates not allowed
print(a_set)
# a_set[0] = 4
# print(a_set)

a_dict = {'key': 'value', 'key2': 3, 123: None} #mutable, not indexed, duplicates not allowed in keys, allowed in values
print(a_dict)
a_dict['key'] = 'new_value'
print(a_dict)

