# Example 1 - Iteration through a list

string_list = ['Bob', 'Alice', 'Charlie', 'Dave', 'Eve']

# Print each name in the list
for name in string_list:
    print(name)
    
# Print each name in the list with its index
for each_name in range(len(string_list)):
    print(f'Index: {each_name}, Name: {string_list[each_name]}')