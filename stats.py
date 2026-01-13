def get_num_words(books_content):
    words = books_content.split()
    num_words = len(words)    
    return f"Found {num_words} total words"
def get_num_characters(books_content):
    chars=list(books_content)
    lowered_chars=[]
    for char in chars:
        lowered_chars.append(char.lower())
    character_count = {}  
    for char in lowered_chars:
        if char in character_count:
            character_count[char]+=1
        else:
            character_count[char]=1
    return character_count
def sorting(num_chars_dict):
    return num_chars_dict["num"]
def sort_dictionary(num_chars_dict):
    sorted_List = []
    for ch in num_chars_dict:
        sorted_List.append({"char" : ch, "num" : num_chars_dict[ch]})
    sorted_List.sort(reverse=True, key=sorting)
    return sorted_List


