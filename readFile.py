def read_entire_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return "File was  not found."

def read_first_lines(file_name, n):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            return "".join(lines[:n])
    except FileNotFoundError:
        return "File was not found."

def read_last_lines(file_name, n):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            return "".join(lines[-n:])
    except FileNotFoundError:
        return "File was not found."

def count_words(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

def read_last_lines_bonus(file_name, n):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            return ''.join(lines[-n:])
    except FileNotFoundError:
        return "File not found."

file_name = "readFile.txt"  
n = 5  

entire_file_content = read_entire_file(file_name)
print("Entire File Content:")
print(entire_file_content)
print("=" * 40)

first_n_lines = read_first_lines(file_name, n)
print(f"First {n} Line:")
print(first_n_lines)
print("=" * 40)

last_n_lines = read_last_lines(file_name, n)
print(f"Last {n} Line:")
print(last_n_lines)
print("=" * 40)

word_count = count_words(file_name)
print(" Word count:", word_count)
print("=" * 40)

#not sure if this is correct
last_n_lines_bonus = read_last_lines_bonus(file_name, n)
print(f"Last {n} Lines (Bonus):")
print(last_n_lines_bonus)
print("=" * 40)
