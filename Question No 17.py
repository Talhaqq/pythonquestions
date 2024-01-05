"""Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet
ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote
sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually
ignored."""


def isPalindrome(s): 
	s1 = s.replace(' ', '') 
	s1 = s1.lower() 
	s2 = s1[::-1]; 
	return True if s1 == s2 else False
	
s = "Too hot to hoot"
if (isPalindrome(s)): 
	print ("Sentence is palindrome.") 
else: 
	print ("Sentence is not palindrome.") 
