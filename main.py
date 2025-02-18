def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    my_dict = {}
    for char in text:
        char = char.lower()
        if char in my_dict:
            my_dict[char] += 1
        else: 
            my_dict[char] = 1
    return my_dict

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "books/Frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    
    num_words = get_num_words(file_contents)
    char_counts = count_characters(file_contents)
    chars_sorted_list = char_dict_to_sorted_list(char_counts)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")
   
if __name__ == "__main__":
    main()