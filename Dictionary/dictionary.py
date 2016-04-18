CONS = { "b" : "" ,
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
VOW = {"a", "e", "i", "u", "\'"}

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