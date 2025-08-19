def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    num_chars = {}
    for char in text:
        char = char.lower()
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    
    return num_chars

def get_sorted_num_chars(num_chars):
    num_chars_list = []
    for key, value in num_chars.items():
        if key.isalpha():
            num_chars_list.append({"char":key, "num":value})
    num_chars_list.sort(key=lambda x: x["num"], reverse=True)
    return num_chars_list
        