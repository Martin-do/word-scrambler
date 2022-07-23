from itertools import count
import timeit

'''
    so this code works basically by iterating through each word in the dictionary
    of words, then loops through the letters in the input word and increases the count
    if there is a match, after looping through the letters, if the count == length of the input word
    it adds the word to a list
    
    definition of functions
        word_length() -- this gets the maximum number of letters we want the scrambler to output from the user
        choke_dict() -- this is used to limit the dictionary size to just the words with the max length
            we need from the thousands of words available
        word_histo() -- this returns a dictionary histogram of the letters in a given word, it is used to further
            scrutinize the outputed word to give us what is need
            e.g. input = decide -- output = edeed  xxxx, this is wrong cos we have 3 'e' in the output whereas 
            the input only has 2
        equal_or_less() -- this depends on the output from the 'word_histo', it returns 'True' if the histogram
            of the words is less than or equals to that of the input word, though there are exceptions if we need
            words with higher histogram value
            e.g. input = decide -- output = decided, we can see the letter 'd' appearing 3 times in the output and also
            a valid letter
        common_word() -- this is where the computation is done, loop through letters from words in dictionary of words
            check if there's match with the letters in the input and increment a counter
            if the counter at the end of the loop == to the length of the input(max_length), then
            append to the valid list and print it out to the user

    Note; when u use a max_length > length of input, the equal_or_less() func becomes obsolete (work in progress)
        -- to fix this i have to first output the lists with the normal length of the input words and lesser,
        then only output the list with words higher than the normal length --- sorted already😊😊
'''     

def main():

    words = open('words.txt', 'r')
    words = words.read()
    words = words.split('\n')

    # word_input = str(input('Enter your word: ')).lower()
    word_input = 'decide'
    # max_length = str(input("Enter max length of words you need or press 'd' for default length: "))
    max_length = 7

    word_input_ls = list(word_input)
    valid_words_list = []

    n = word_length(max_length, word_input)
    len_ls = choke_dict(words, n)              #contains list of words that have equal length wit the input
    # common_word(word_input_ls, len_ls, valid_words_list, word_input, n)

    total_words_found = 0
    
    if n > len(word_input):         ##this will allow repetition of letters
        b = n - len(word_input)         #this is for it to loop (max_length - wordlength) times
        for i in range(b):
            
            common_word(word_input_ls, len_ls, valid_words_list, word_input, n)
            total_words_found += len(valid_words_list)
            valid_words_list = []
            b -= 1
            n -= 1
    
        b = len(word_input)
        n = len(word_input)
        for i in range(b - 1):
            
            common_word(word_input_ls, len_ls, valid_words_list, word_input, n)
            total_words_found += len(valid_words_list)
            valid_words_list = []
            n -= 1
    else:
        # b = len(word_input)
        n = len(word_input)
        for i in range(n - 1):
            
            common_word(word_input_ls, len_ls, valid_words_list, word_input, n)
            total_words_found += len(valid_words_list)
            valid_words_list = []
            n -= 1
    print(' ======== ============ ')
    print(f'Total number of words returned is {total_words_found}')


# words = ['eddied', 'decide', 'deiced', 'deeded', 'triced', 'voiced', 'wicked', 'ice']



def word_length(a, w_input):

    if a == 'd':
        a = len(w_input)
        print('\nmaximun length of words to scramble is ' + str(a))
    else:
        a = int(a)
        print('\nmaximun length of words to scramble is ' + str(a))
    
    return a



def choke_dict(w, max_length):

    ls_1 = [ word for word in w if len(word) <= max_length ]         ##incremental
    
    return ls_1



def word_histo(word, w_input):
    ls1 = word
    dc = {}

    for i in w_input:
        dc[i] = 0

    for i in ls1:
        if i in dc:
            dc[i] += 1
        else:
            dc[i] = 0

    # print(dc)
    return dc

def equal_or_less_dict(w1, w2, i, n): ## w2 is the dictionary of the input word
    count = 0
    
    if n > len(i):
        for i in w1:
            if w1[i] <= w2[i] + 3:      ##incremental **  still needs checking
                count += 1
            else:
                count = 0

    elif n <= len(i):
        for i in w1:
            if w1[i] <= w2[i]:      ##incremental **  still needs checking
                count += 1
            else:
                count = 0
    else:
        count = 0

    if count == len(w2):
        return True
    else:
        count = 0
        return False
       

def common_word(w_input_ls, List1, List2, ww, max_length): ## args = word input list, list of words <= maxlength of words, list of valid words after func call, wordinput, maxlength expected
    count = 0
    pos = 0

    while pos < len(List1):

        for letter in List1[pos]:
            if letter in w_input_ls:
                count += 1
            else:
                
                count = 0
                break

        if count == max_length:          
            if equal_or_less_dict(word_histo(List1[pos], ww), word_histo(ww, ww), ww, max_length) == True:
                if len(List1[pos]) == max_length:
                    List2.append(List1[pos])
                    pos += 1
                    count = 0
                else:
                    List2.append(' ')
                    pos += 1
                    count += 1
                
        else:
            pos += 1
            count = 0

    print('\n =======  ======================== ')
    print(f'The {max_length} letter scrambled word is: ')
    print(List2)



# res = timeit.timeit(stmt='main()', globals=globals(), number=1)
# print(res)
main()