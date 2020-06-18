#python 3
#The Function i expected to return a STRING
#The Function accepts String sentence as parameter

def reverse_word_and_swap_case(sentence):
    word=sentence.swapcase().split() #swap_case
    word=list(reversed(word))  #reverse_word_order
    line=" ".join(word)
    print(line)

reverse_word_and_swap_case(input())
    
