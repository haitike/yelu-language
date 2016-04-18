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

        no_vowel_word = new_word
        for vowel in VOWELS:
            no_vowel_word = no_vowel_word.replace(vowel,"")

        invalid_letter = False
        for letter in no_vowel_word:
            if letter not in CONSONANTS:
                invalid_letter = True

        if invalid_letter:
            print("Some of the letters you introduced are not in Yelu alphabet")
        else:
            print("done. <{}> was introduced. Root: <{}>".format(new_word,no_vowel_word))

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