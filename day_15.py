def reverse_lookup(name_dictionary, name_value):
    keys = [k for k, v in name_dictionary.items() if v == name_value]
    if keys:
        return f"Keys found for value {name_value}: {keys}"
    else:
        return f"No keys found for value {name_value}."

def add_entry(name_dictionary, key, value):
    if key in name_dictionary:
        return f"Error: Key '{key}' already exists with value {name_dictionary[key]}."
    name_dictionary[key] = value
    return f"Added entry: {key} -> {value}"

def remove_entry(name_dictionary, key):
    if key in name_dictionary:
        del name_dictionary[key]
        return f"Removed entry: {key}"
    return f"Error: Key '{key}' not found."

def display_dictionary(name_dictionary):
    if not name_dictionary:
        return "The dictionary is empty."
    return "\n".join(f"{k}: {v}" for k, v in name_dictionary.items())

name_dictionary = {'Alice': 90, 'Bob': 85, 'Charlie': 90, 'David': 80}

print(reverse_lookup(name_dictionary, 90))  
print(reverse_lookup(name_dictionary, 100))  

print(add_entry(name_dictionary, 'Eve', 95))
print(add_entry(name_dictionary, 'Alice', 92)) 

print(remove_entry(name_dictionary, 'Bob'))
print(remove_entry(name_dictionary, 'John'))  

print("\nCurrent Dictionary:")
print(display_dictionary(name_dictionary))
