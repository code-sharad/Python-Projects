alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
mylist = []
cipher_text = []


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'encode':

        for i in start_text:
            x =+ alphabet.index(i) + shift_amount
            mylist.append(x)

        for x in mylist:
            cipher_text.append(alphabet[x])
        print(f"The encoded text is {''.join(cipher_text)} ")   #convert list to string

    elif cipher_direction == 'decode':

        for i in start_text:
            x =+ alphabet.index(i) - shift_amount
            mylist.append(x)

        for x in mylist:
            cipher_text.append(alphabet[x])
        print(f"The encoded text is {''.join(cipher_text)}")        


caesar(start_text=text, shift_amount=shift, cipher_direction=direction )
        


    

    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 