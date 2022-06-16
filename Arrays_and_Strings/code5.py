#Check whether two strings are anagram of each other

def anagram(str1,str2):
   if sorted(str1) == sorted(str2):
       print("Anagrams")
   else:
       print("Nah!")

str1 = "fire"
str2 = 'iref'
anagram(str1,str2)