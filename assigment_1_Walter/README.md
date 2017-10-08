# Assignment 1 Due 10/06 Friday, 11:59pm 


**Please read Code Grading Rubric (in Blackboard - Assignment) carefully before you start this assignment.**

1. (25 points) Factoring of integers. Write a program that asks the user for an integer and then prints out all its factors. For example, when the user enters 150, the program should print
    2
    3
    5
    5

2.  (25 points) Write a recursive function isPalindrome(string) that returns True if string is a palindrome, that is, a word that is the same when reversed. Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. Hint: A word is a palindrome if the frst and last letters match and the remainder is also a palindrome.

3. (30 points) The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four directions and stumbles to the next intersection, then again randomly picks one of four directions, and so on. You might think that on average the drunkard doesn’t move very far because the choices cancel each other out, but that is actually not the case.

	Write a function to calculate the distance after n intersections. 

4. (20 points) Use Turtle to draw the drunkard's walk in #3. 


5. (Optional, 20 points) The game of Nim. This is a well-known game with a number of variants. The following variant has an interesting winning strategy. Two players alternately take marbles from a pile. In each move, a player chooses how many marbles to take. The player must take at least one but at most half of the marbles. Then the other player takes a turn. The player who takes the last marble loses.

	Write a program in which the computer plays against a human opponent. Generate a random integer between 10 and 100 to denote the initial size of the pile. Generate a random integer between 0 and 1 to decide whether the computer or the human takes the frst turn. Generate a random integer between 0 and 1 to decide whether the computer plays smart or stupid. In stupid mode the computer simply takes a random legal value (between 1 and n/2) from the pile whenever it has a turn. In smart mode the computer takes off enough marbles to make the size of the pile a power of two minus 1—that is, 3, 7, 15, 31, or 63. That is always a legal move, except when the size of the pile is currently one less than a power of two. In that case, the computer makes a random legal move.

	You will note that the computer cannot be beaten in smart mode when it has the frst move, unless the pile size happens to be 15, 31, or 63. Of course, a human player who has the frst turn and knows the winning strategy can win against the computer.


