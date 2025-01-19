def main():
    with open("books/frankenstein.txt") as file:
        contents = file.read()
       
    words = contents.split()
    

    lower_contents = contents.lower()

    counts = {}
    for char in lower_contents:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    chars_list = []
    for char, count in counts.items():
        chars_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]

    chars_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of books/frankenstein.txt --- {len(words)} words found in the document")
    for char in chars_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")   
main()