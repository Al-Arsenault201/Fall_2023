# in class coding from Wednesday, October 4

def reverse_word (word):
  # now the code. DON’T FORGET TO INDENT!!

  i = 0
  reversed_word = ''  #Do not use the function name here!!!!
  while i < len(word):
     reversed_word = reversed_word + word[-(i+1)]
     i += 1
  print (' The word ', word, ' reversed is ', reversed_word)

if __name__ == "__main__":
    print(reverse_word("happy happy happy"))