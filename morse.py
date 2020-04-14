morse_translator = {
    "A":"._",
    "B": "_...",
    "C": "_._.",
    "D":"_..",
    "E":".",
    "F":".._.",
    "G":"__.",
    "H":"....",
    "I":"..",
    "J":".___",
    "K":"_._",
    "L":"._.." ,
    "M":"__" ,
    "N":"_." ,
    "O":"___" ,
    "P":".__." ,
    "Q":"__._" ,
    "R":"._." ,
    "S":"..." ,
    "T":"_" ,
    "U":".._" ,
    "V":"..._" ,
    "W":".__" ,
    "X":"_.._" ,
    "Y":"_.__" ,
    "Z":"__.." ,
    "1":".____" ,
    "2":"..___" ,
    "3":"...__" ,
    "4":"...._" ,
    "5":"....." ,
    "6":"_...." ,
    "7":"__...",
    "8":"___.." ,
    "9":"____." ,
    "0":"_____",
    " ": " "
}
list_of_translator = morse_translator.items()
def convert_input_to_english(phrase):
    words = phrase.split("//")
    new_list=[]
    for word in words:
        new_list.append(" ")
        chars = word.split(" ")
        for char in chars:
            for tup in list_of_translator:
                if tup[1]==char:
                    new_list.append(tup[0])
                   
    new_str = "".join(new_list)
    print("calulating.....")
    print("calulating.....")
    print("calulating.....")
    print("here is your string in English!")
    print(new_str)

def convert_input_to_morse(phrase):
    upper_cased = phrase.upper()
    list_of_chars = upper_cased.split()
    new_list = []
    for word in list_of_chars:
        new_list.append('//')
        for char in word:
            for tup in list_of_translator:
                if tup[0]==char:
                    print(tup[1])
                    new_list.append(tup[1])
                    new_list.append(" ")
                   
    new_str = "".join(new_list)
    print("calulating.....")
    print("calulating.....")
    print("calulating.....")
    print("here is your string in morse code!")
    print(new_str)


which_one = input("Would like you to go from english to morse code? yes or no: ")
if which_one.lower() == "no":
    which_two = input("Would you like to go from morse code to english? yes or no: ")
    if which_two.lower() == "yes":
        print('run this function morse>english')
        user_input = input("Please enter in a word or a phrase and I will convert it to english! Rules: Add a space after each letter and then a '//' after each word.")
        convert_input_to_english(f"{user_input} //")

    elif which_two.lower() == "no":
        print('okay! Next time!')
        
elif which_one.lower()=="yes":
    user_input = input("Please enter in a word or a phrase and I will convert it to morse code! Rules: No symbols, besides periods.")
    convert_input_to_morse(user_input)
else: 
    print('Okay, maybe you added a weird space. Try again!')





