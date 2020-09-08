import nltk
import re
from colorama import Fore, Back, Style,init
from termcolor import colored, cprint 

# _________________  (colors)  ____________________
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

intro="""

   _____                              _____ _       _               
  / ____|                            / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                             | |                    
                                             |_|                    



"""




def encrypt(text, key):
    test_list = [] 
    alpha = 'a'
    for i in range(0, 26): 
        test_list.append(alpha) 
        alpha = chr(ord(alpha) + 1)  
    # print (test_list) 



    regex = r"[A-z]+"

    matches = re.findall(regex,text)
    # print(separator.join(matches))# abc  acb
    # print(matches)   #  ['abc', 'acb']


    
    # num = key % 26
    # one_word_result =[]
    final_text_result =[]

    for single_word in matches:
        one_word=''
        for char in single_word.lower():
            index = test_list.index(char)
            index += key
            # index = index % 26
            new_index = index % 26

            # new_index=num+index
            # one_word_result.append(test_list[new_index])
            one_word+=test_list[new_index]
        final_text_result.append(one_word)

    # return final_text_result   #[bcd, fgh]
        

    new_word=' '.join(final_text_result)
    return new_word #bcd fgh


# ________________________________________

def decrypt(text, key):
    test = [] 
    alpha = 'a'
    for i in range(0, 26): 
        test.append(alpha) 
        alpha = chr(ord(alpha) + 1)  
    test_list =test[::-1] 


    regex = r"[A-z]+"
    matches = re.findall(regex,text)
    

    final_text_result =[]
    for single_word in matches:
        one_word=''
        for char in single_word.lower():
            index = test_list.index(char)
            index += key
            new_index = index % 26
            one_word+=test_list[new_index]
        final_text_result.append(one_word)

    new_word=' '.join(final_text_result)
    return new_word 


 # ________________________________________
 #DEMO
nltk.download('words')

original_words_list = nltk.corpus.words.words()
words_list = [word.lower() for word in original_words_list]

 # ________________________________________

def count_words(sentence):
    sentence_words = sentence.split()
    en_word_count = 0

    for word in sentence_words:
        if word.lower() in words_list:
            en_word_count += 1

    return en_word_count

 # ________________________________________

def most_likely(sentences):
    _max = 0
    _max_sentence = ''

    for sentence in sentences:
        if count_words(sentence) > _max:
            _max_sentence = sentence
            _max = count_words(sentence)
    return _max_sentence




## ____________________________________________________

if __name__ == "__main__":
#   print(encrypt('It was the best of times, it was the worst of times.', 1))#ju xbt uif cftu pg ujnft ju xbt uif xpstu pg ujnft

  prCyan(intro)

  assert encrypt('abc', 1)=='bcd'
  prYellow(f"encrypt'abc'----> {encrypt('abc', 1)}")
  prPurple('='*50)
# ___________________________________
  assert encrypt('acb', 10)=='kml'
  prYellow(f"encrypt'acb'----> {encrypt('acb', 10)}")
  prPurple('='*50)
# ___________________________________

  assert decrypt('bcd', 1)=='abc'
  prGreen(f"decrypt'bca'----> {decrypt('bcd', 1)}")
  prPurple('='*50)
# ___________________________________

  assert encrypt('ABC::,   ,EfG::', 1)=="bcd fgh"
  prGreen(f"encrypt'ABC::,   ,EfG::'----> {encrypt('ABC::,   ,EfG::', 1)}")
  prPurple('='*50)
# ___________________________________

  assert decrypt('BcD::,   ,fGh::', 1)=="abc efg"
  prGreen(f"decrypt'BcD::,   ,fGh::''----> {decrypt('BcD::,   ,fGh::', 1)}")
  prPurple('='*50)

  # ++++++++++++++++++++++++++
  #prepare data for most_likely test
  sentence = 'It was the best of times, it was the worst of times.'
  test_sentences=[]
  for i in range(1,27):
        test_sentences.append(encrypt(sentence, i))
  print(test_sentences)

  for i in range(len(test_sentences)):
        print(count_words(test_sentences[i]))
  # ++++++++++++++++++++++++++

  assert most_likely(test_sentences)=="it was the best of times it was the worst of times"
  prCyan(f"most_likely ----> {most_likely(test_sentences)}")
  prPurple('='*50)
  prRed('All tests passed!!!!')