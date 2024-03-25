def num(file_contents):
    words = file_contents.split()
    return len(words)

def char(file_contents):
    character_dict = {}
    lowered_string = file_contents.lower()
    for chars in lowered_string:
        if chars.isalpha():
            if chars not in character_dict:
                character_dict[chars] = 1
            else:
                character_dict[chars] += 1
    list_of_dict = []
    for char, count in character_dict.items():
        char_count_dict = {"char": char, "count": count}
        list_of_dict.append(char_count_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report---")
    for char_dict in list_of_dict:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")



def sort_on(char_dict):
    return char_dict["count"]





def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = num(file_contents)
    print(f"{word_count} words found in the document")
    char(file_contents)

if __name__ == "__main__":
    main()




