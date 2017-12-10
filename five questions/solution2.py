



import itertools

def question2(s):
    max_palindrome = " "
    max_lenght = 0
    
    for start, stop in itertools.combinations(range(len(s)+1), 2):
        substring = s[start:stop]  
        
        if (len(substring) > max_lenght) and (substring == substring[::-1]):
            max_palindrome = substring
            max_lenght = len(substring)
            
    print  "The Longest Palindrome: ",max_palindrome 
    print  "The size of the Longest Palindrome: ", max_lenght 
    print  "                                       "
    return max_palindrome

#test    
question2("xabbaabbammmnnnnnnn") 
question2("juyyyyxmadamapppii")
question2("juyxttracecarrpppii")
 



  