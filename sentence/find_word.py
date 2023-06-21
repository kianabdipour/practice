from custom_exseption import NoSentence


# This function get sentence and make a list of word that are in sentence.
def get_sentence():
    print("Please type a sentence.")
    input_sentence = input(": ")
    list_word = input_sentence.split(" ")
    return list_word


# This function get the word and check it is in sentence or not.
def get_and_find_word():
    print("If it's finish type (q).")
    list_word = get_sentence()

    print("\nOk, type word that you want.")
    input_word = input(": ")

    if ((input_word.lower() in list_word) or (input_word.upper() in list_word)) and (list_word != ["q"]):
        print("\nYes! i found this word.\n")

    elif list_word == ["q"]:
        pass

    else:
        print("\nOh! i couldn't found this word.\n")

    return list_word


# This function run the program and check the error
def run_and_check_error():
    list_word = get_and_find_word()
    while list_word != ["q"]:
        try:

            if len(list_word) == 1 and list_word != ["q"]:
                raise NoSentence("")

            else:
                pass

        except NoSentence:
            print("\nNoSentence_Error: You should type sentence not word.\n")
        list_word = get_and_find_word()


if __name__ == "__main__":
    run_and_check_error()

else:
    print("You should run this function in main file")
