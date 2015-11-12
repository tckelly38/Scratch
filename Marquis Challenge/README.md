# Birthday Challenge
I was presented with this problem at Marquis Software, and my answer was chosen as the winning response

Solution for Birthday Challenge

**What is the probability that at least 6 out of 60 people have a birthday in the same 10 day period?**

Created by Tyler Kelly

Simplified and Commented by Steve Payne

There are a couple of ways to tackle the problem.  

#  Option 1: 
   
   The first method provides an exact solution using counting/probablity theory.  
   Probablity theory was deleloped by Blaise Pascal to determinte the odds at gambling tables.
   The book that describes this method, "A First Course in Probability", is on Steve's bookshelf;
   however, it will probably put you to sleep before you find the answer.

# Option 2:

   The second method provides an approximate answer.  It uses an empirical or 
   experimental methodology.  The Concept is to perform an experiment as follows: 
      Pick 60 random people in a mall, and ask their birthdays
      See if you get 6 birthdays in any 10 day period.
      If you get at least one ten day period that includes six birthdays, the experiment is a success.
      If not, the experiment is a failure.
      Do the experiment 100,000 times keeping track of the number of successes.
      Divide the number of successes by the number of experiments (100,000) to obtain the probability of success.
   The more times you perform the experiment the more accurate your results will be.

Option 1 is great for introverts because you don't need to talk to anyone; However, 
   it requires a course in probablity theory. option 2 is for extroverts because
   you will meet 6 million new friends and know their birthdays.

# Option 3:

   For the pragmatic, you can write a program to simulate the empirical method. 
   The commented program below shows how.  This method can be used to solve any
   counting problem.