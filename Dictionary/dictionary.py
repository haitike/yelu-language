CONSONANTS = { "b" : "" ,
         "ch" : "",
         "d" : "",
         "f" : "",
         "g" : "",
         "h" : "",
         "k" : "",
         "l" : "human",
         "m" : "",
         "n" : "",
         "p" : "",
         "q" : "" ,
         "r" : "" ,
         "rr" : "" ,
         "s" : "" ,
         "sh" : "" ,
         "t" : "" ,
         "th" : "" ,
         "ts" : "" ,
         "w" : "" ,
         "y" : "matter" ,  }
VOWELS = {"a", "e", "i", "u", "\'"}

def unvowel(word):
    uv_word = word
    for vowel in VOWELS:
        uv_word = uv_word.replace(vowel,"")
    return uv_word

def has_invalid_letter(word):
    uv_word = unvowel(word)
    for letter in uv_word:
        if letter not in CONSONANTS:
            return True
    return False


def get_root(word):
    uv_word = unvowel(word)
    root_list = []
    for l in uv_word:
        root_list.append(l)
    return root_list

while True:

    option = input("Select an option:\n"
          "1 - Add Word\n"
          "2 - Search (Yelu)\n"
          "3 - Search (English)\n"
          "4 - Delete Word\n"
          "5 - Browse Roots\n"
          "e - Exit\n")

    if option == "1":
        new_word = input("Input a word: ")
        if has_invalid_letter(new_word):
            print("Some of the letters you introduced are not in Yelu alphabet")
        else:
            print("done. [{}] was introduced. Root: {}".format(new_word,get_root(new_word)))

    if option == "2":
        print("search...")

    if option == "3":
        print("search...")

    if option == "4":
        print("delete...")

    if option == "5":
        print("roots...")

    if option == "e":
        print("Exiting...")
        break

