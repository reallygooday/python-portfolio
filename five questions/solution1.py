#Solution1
def question1(s, t):
   if any([t in s, t in s[::-1], t[::-1] in s, t[::-1] in s[::-1]]): 
      return True 
   else:
      return False
 	
#test	
print (question1("haha", "hi"))
print (question1("haha", "hh"))
print (question1("haha", "ahahahahahahah"))
print (question1("haha", "aha"))
print (question1("haha", "a"))
print (question1("udacity", "ad"))


