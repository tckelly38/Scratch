import java.util.Random;

//Solution for Birthday Challenge
//Created by Tyler Kelly
//Simplified and Commented by Steve Payne

//There are a couple of ways to tackle the problem.  
// Option 1: 
//The first method provides an exact solution using counting/probablity theory.  
//Probablity theory was deleloped by Blaise Pascal to determinte the odds at gambling tables.
//The book that describes this method, "A First Course in Probability", is on Steve's bookshelf;
//however, it will probably put you to sleep before you find the answer.

//Option 2:
//The second method provides an approximate answer.  It uses an empirical or 
//experimental methodology.  The Concept is to perform an experiment as follows: 
//   Pick 60 random people in a mall, and ask their birthdays
//   See if you get 6 birthdays in any 10 day period.
//   If you get at least one ten day period that includes six birthdays, the experiment is a success.
//   If not, the experiment is a failure.
//   Do the experiment 100,000 times keeping track of the number of successes.
//   Divide the number of successes by the number of experiments (100,000) to obtain the probability of success.
//The more times you perform the experiment the more accurate your results will be.

//Option 1 is great for introverts because you don't need to talk to anyone; However, 
//it requires a course in probablity theory. option 2 is for extroverts because
//you will meet 6 million new friends and know their birthdays.

//Option 3:
//For the pragmatic, you can write a program to simulate the empirical method. 
//The commented program below shows how.  This method can be used to solve any
//counting problem.


public class BirthdayDriver {
	public static void main(String[] args) {
		int totalSuccesses = 0;
		Random randomNumberGenerator = new Random(); //set up the random number generator to pick random birthdays
		for (int experiment=0;experiment<100000;experiment++) {  //do the experiment 100,000 times
			//create an array to represent a year.  All 365 integers are zero. day[0] = Jan 1 and day[364] is Dec 31.
			int[] calendar = new int[365];
			//pick 60 random birthdays and put them on a calendar (some calendar days may have more than one birthday)
			for(int i =0; i < 60; i++)	{
				//pick a random # between 0 and 364 and increment that day in calendar (add a birthday)
				calendar[randomNumberGenerator.nextInt(365)]++;  
			}
			//Now that all birthdays are in the calendar, check to see if the calendar has 6 birthdays within any 10 day period.
			//loop through each group of ten sequential days
			//group 1 days: "0123456789", group 2 days: "23456789 and 10", group 3 days: "2345678 10 and 11", etc.
			for (int day=0;day<355;day++) {  //355 is the start of the last 10 day period
				int numberOfBirthdaysInTenDays = 0;
				//loop through a ten day sequence starting with day and ending with (day+9)
				for (int dayWithin=0;dayWithin<10;dayWithin++) {
					numberOfBirthdaysInTenDays += calendar[day+dayWithin];  //add number of birthdays to counter
				}
				//check to see if you get six birthdays in ten day grouping   
				if (numberOfBirthdaysInTenDays>=6) {
					totalSuccesses++;
					break;
					//You only need one set of ten days with six birthdays for a success so quit this experiment.
					//If you don't quit this experiment, your number of years with a success will be inflated 
					//because you could have more than one success in one year. 
				}
			}
		}
		
		System.out.println((totalSuccesses/(double)100000));  //# of successes divided by # of experiments
	}

}
