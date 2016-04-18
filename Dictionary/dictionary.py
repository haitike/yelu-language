import shelve

CONSONANTS = { "b" : "" ,
         "c" : "",
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
         "R" : "" ,
         "s" : "" ,
         "t" : "" ,
         "ç" : "" ,
         "w" : "" ,
         "x" : "" ,
         "y" : "matter" ,
         "z" : "" ,}
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

def get_root_string(word):
    uv_word = unvowel(word)
    sorted_list = ''.join(sorted(uv_word))
    return sorted_list

def get_root_meanings(root_string):
    meanings = []
    for i in root_string:
        meanings.append(CONSONANTS[i])
    return meanings

while True:
    option = input("\nSelect an option:\n"
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
            root_string = get_root_string(new_word)
            if root_string:
                print("Root: {}. Root meanings: {}".format(list(root_string), get_root_meanings(root_string)))
                meaning = input("Now introduce the english meaning of <{}>: ".format(new_word))

                d = shelve.open("Words/data")
                if root_string not in d:
                    d[root_string] = dict()
                temp = d[root_string]
                temp[new_word] = meaning
                d[root_string] = temp
                d.close()
                print("Done. Word was added.")

            else:
                print("You introduced an empty word or a word without consonants")
        input()

    if option == "2":
        print("search...")

    if option == "3":
        print("search...")

    if option == "4":
        print("delete...")

    if option == "5":
        l = input("Write the first element of a root and all related words will be displayed :  ")
        if l:
            if l[0] in CONSONANTS:
                d = shelve.open("Words/data")
                empty = True
                for i in d:
                    if i[0] == l[0]:
                        empty = False
                        print("\n--> {} {}".format(i, get_root_meanings(i)))
                        for e in d[i]:
                            print("{} : {}".format(e, d[i][e]))
                d.close()

                if empty:
                    print("There is no words beginning with that letter")

            else:
                print("That letter is not in Yelu Alphabet or it is a vowel")
        else:
            print("You must write a letter")
        input()

    if option == "e":
        print("Exiting...")
        break


