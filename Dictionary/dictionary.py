import shelve

CONSONANTS = { "b" : "fire" ,
         "c" : "negative",
         "d" : "far",
         "f" : "fast",
         "g" : "nothing",
         "h" : "air",
         "k" : "earth",
         "l" : "human",
         "m" : "life",
         "n" : "universe",
         "p" : "spirit",
         "q" : "perfect" ,
         "r" : "light" ,
         "s" : "water" ,
         "t" : "near" ,
         "ç" : "thunder" ,
         "w" : "up" ,
         "x" : "mind" ,
         "y" : "matter" ,
         "z" : "middle" ,}
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

#################### MAIN ####################
d = shelve.open("Words/data")
while True:
    option = input("\nSelect an option:\n"
          "1 - Add Words\n"
          "2 - Delete Word\n"
          "3 - Search (Yelu)\n"
          "4 - Search (English)\n"
          "5 - Browse Roots\n"
          "e - Exit\n")

    if option == "1":
        while True:
            new_word = input("Input a word (<e> exit to Menu): ")
            if new_word == "e":
                break
            if has_invalid_letter(new_word):
                print("Some of the letters you introduced are not in Yelu alphabet")
            else:
                root_string = get_root_string(new_word)
                if root_string:
                    print("Root: {}. Root meanings: {}".format(list(root_string), get_root_meanings(root_string)))
                    if root_string not in d:
                        d[root_string] = dict()
                    if new_word not in d[root_string]:
                        meaning = input("Now introduce the english meaning of <{}> (<e> exit to Menu): ".format(new_word))
                        if meaning == "e":
                            break
                        temp = d[root_string]
                        temp[new_word] = meaning
                        d[root_string] = temp
                        print("Done. Word was added.")
                    else:
                        print("The word already exists with the meaning:\n- {}\n".format(d[root_string][new_word]))
                        overwrite = input("Do you want to overwrite it? (y/n) ")
                        if overwrite == "y":
                            meaning = input("Now introduce the english meaning of <{}> (<e> exit to Menu): ".format(new_word))
                            if meaning == "e":
                                break
                            temp = d[root_string]
                            temp[new_word] = meaning
                            d[root_string] = temp
                            print("Done. Word was added.")
                        else:
                            print("word was not added")
                else:
                    print("You introduced an empty word or a word without consonants")

    if option == "2":
        word_to_delete = input("What word to delete (<e> exit to Menu): ")
        if word_to_delete == "e":
            pass
        else:
            input("This is a beta feature, to be improved... ")
            root_string = get_root_string(word_to_delete)
            temp = d[root_string]
            del temp[word_to_delete]
            d[root_string] = temp

    if option == "3":
        print("search...")
        input()

    if option == "4":
        print("search...")
        input()

    if option == "5":
        l = input("Write a radical and will show all words that contain it (Empty: Show all words)  ")
        if l:
            if l[0] in CONSONANTS:
                empty = True
                for i in d:
                    if l[0] in i:
                        empty = False
                        print("\n--> {} {}".format(i, get_root_meanings(i)))
                        for e in d[i]:
                            print("{} : {}".format(e, d[i][e]))
                if empty:
                    print("There is no words beginning with that letter")

            else:
                print("That letter is not in Yelu Alphabet or it is a vowel")
        else:

            empty = True
            for i in d:
                empty = False
                print("\n--> {} {}".format(i, get_root_meanings(i)))
                for e in d[i]:
                    print("{} : {}".format(e, d[i][e]))
            if empty:
                print("Dictionary is empty")
        input()

    if option == "e":
        print("Exiting...")
        break
d.close()
