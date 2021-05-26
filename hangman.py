# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

#%%
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guess=[]
    for char in secret_word:
        if char in letters_guessed:
            guess.append(char)
            if len(guess)==len(secret_word):
                return True
        else:
            return False
        
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
# print(is_word_guessed('paloma', ['a','a','l','l','m','p']))
#%%
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    letters=[]
    for char in secret_word:
        if char in letters_guessed:
            letters.append(char)
        else:
            letters.append("_ ")
        
    letters_join="".join(letters)
    return letters_join 
# d=get_guessed_word("paloma",['i','i','l','l','m','p'])
# print(d)
#%%    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remain=list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in remain:
            remain.remove(char)
    return "".join(remain)

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print (get_available_letters(letters_guessed)) 

#%%
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[]
    guesses_remaining=6
    warnings=0
    alphabet=get_available_letters([])
   
    print("bienvenido al juego de ahorcado")
    print("Estoy pensando en una palabra de %s letras"%(len(secret_word)))
    
    
    while guesses_remaining>0:
        print('-------------------------')
        print("Tienes %s intentos"%guesses_remaining)
        usser_input_raw=input('Ingrese una letra:')
        usser_input=str.lower(usser_input_raw)
        if usser_input in letters_guessed:
            warnings+=1
            print('letra ya elegida')
            print('Tienes %s warnings'%warnings)
            print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
        else:
            if usser_input in alphabet:
                letters_guessed.append(usser_input)
                if usser_input in 'aeiou':
                    
                    if usser_input in secret_word:
                        print('buenaaaa:',get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word, letters_guessed):
                            print("Felicidades ganaste el juego")
                            break
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                        
                    else:
                        guesses_remaining-=2
                        print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                    
                else:
                    if usser_input in secret_word:
                        print('buenaaaa:',get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word, letters_guessed):
                            print("Felicidades ganaste el juego")
                            break
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                    else:
                        guesses_remaining-=1
                        print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                
            else:
                warnings+=1
                
                print('No es una letra valida, Tienes %s warnings'%warnings)
                print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))

        if warnings ==3:
            guesses_remaining-=1
            warnings=0
       
        else: pass
        
        
    
    if guesses_remaining==0:
        print("no tienes mas intentos")
        print("la respuesta era:",secret_word)
        
    else:
        unique_letters=[]
        
        for char in secret_word:
            if char in unique_letters:
                pass
            else:
                unique_letters.append(char)
        
                
        score=guesses_remaining*len(unique_letters)
        print('tu puntaje es =',score)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
# hangman("holaaa")

#%%

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i=0
    new_word=my_word.replace(" ","")
    alphabet=get_available_letters([])
    
    if len(new_word)==len(other_word):
        for char in new_word:
            i+=1
            if char in alphabet:
                if char in other_word[i-1]: #revisa letra por letra
                    pass
                else: return False
    else: return False
    
    if i==len(other_word):
        return True
    
# d=match_with_gaps("h _ _d", "head")
# print(d)

#%%
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    posible_matches=[]
    for word in wordlist:
        if match_with_gaps(my_word, word):
            posible_matches.append(word)
    
    if posible_matches==[]:
        print('no se encontraron coincidencias')
    
    else: 
        print(posible_matches)
                
# test=show_possible_matches("h _ _w")           
#%%


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed=[]
    guesses_remaining=6
    warnings=0
    alphabet=get_available_letters([])
    pistas_disponibles=0
   
    print("bienvenido al juego de ahorcado")
    print("Estoy pensando en una palabra de %s letras"%(len(secret_word)))
    
    
    while guesses_remaining>0:
        print('-------------------------')
        print("Tienes %s intentos"%guesses_remaining)
        usser_input_raw=input('Ingrese una letra:')
        usser_input=str.lower(usser_input_raw)
        if usser_input in letters_guessed:
            warnings+=1
            print('letra ya elegida')
            print('Tienes %s warnings'%warnings)
            print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
        else:
            if usser_input in alphabet:
                letters_guessed.append(usser_input)
                if usser_input in 'aeiou':
                    
                    if usser_input in secret_word:
                        print('buenaaaa:',get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word, letters_guessed):
                            print("Felicidades ganaste el juego")
                            break
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                        
                    else:
                        guesses_remaining-=2
                        print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                    
                else:
                    if usser_input in secret_word:
                        print('buenaaaa:',get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word, letters_guessed):
                            print("Felicidades ganaste el juego")
                            break
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                    else:
                        guesses_remaining-=1
                        print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                
            else:
                if usser_input=='*':
                    pistas_disponibles+=1
                    if pistas_disponibles<2:
                        print('buscando posibles coincidencias......') 
                        show_possible_matches(get_guessed_word(secret_word,letters_guessed))
                        print('-------------------')
                        print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                    else:
                        print('ya no cuentas con mas comodines')
                        print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))
                        print('Tienes estas letras disponibles:',get_available_letters(letters_guessed))
                else:
                    warnings+=1
                    print('No es una letra valida, Tienes %s warnings'%warnings)
                    print('intenta de nuevo:',get_guessed_word(secret_word,letters_guessed))

        if warnings ==3:
            guesses_remaining-=1
            warnings=0
       
        else: pass
        
        
    
    if guesses_remaining==0:
        print("no tienes mas intentos")
        print("la respuesta era:",secret_word)
        
    else:
        unique_letters=[]
        
        for char in secret_word:
            if char in unique_letters:
                pass
            else:
                unique_letters.append(char)
        
                
        score=guesses_remaining*len(unique_letters)
        print('tu puntaje es =',score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
