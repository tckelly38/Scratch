#include <iostream>

using namespace std;

int main()
{
   char string1[30];
   char string2[30];
   char string3[30];
   char string4[30];

   cout << "Going to make the calls:\n"
        << " cin >> string1;\n"
        << " cin.getline(string2, 30, \',\');\n"
	<< " cin.get(string3, 30, \'e\');\n"
	<< " cin.get(string4, 30);\n\n";

   cout << "Now start typin\', Varmint!\n> ";

   cin >> string1;
   cin.getline(string2,30,',');
   cin.get(string3,30,'e');
   cin.get(string4,30);

   cout << "\n\nOutputs:\n";
   cout << "string1 = " << string1 << '\n';
   cout << "string2 = " << string2 << '\n';
   cout << "string3 = " << string3 << '\n';
   cout << "string4 = " << string4 << '\n';

   return 0;
}
