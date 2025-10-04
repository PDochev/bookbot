def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_chars(text):
    lower_case = text.lower()
    chars = {}
    for char in lower_case:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
        
def sorted_dict(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c , "num": dict[c]})
        sorted_list.sort(reverse=True , key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]

