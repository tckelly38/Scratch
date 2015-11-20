import java.util.Random;

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
