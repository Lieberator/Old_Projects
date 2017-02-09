#include <iostream>
#include <string>

using namespace std;

const int SIZE1 = 10;
const int SIZE2 = 8;
const int SIZE3 = 12;

class finalExam{

	char feData[SIZE3];

public:
	void display(string);
	void sequentialSearch(char);
	finalExam();


};

finalExam::finalExam()
{
	feData[0] = 'q';
	feData[1] = 'w';
	feData[2] = 'e';
	feData[3] = 'r';
	feData[4] = 't';
	feData[5] = 'y';
	feData[6] = 'u';
	feData[7] = 'i';
	feData[8] = 'o';
	feData[9] = 'p';
	feData[10] = 'a';
	feData[11] = 's';


}

void loadData(char datax[], int size) {
	static char values[] = { 'q', 'w', 'e', 'r', 't', 'y', 'u',
		'i', 'o', 'p', 'a', 's', 'd', 'e', 'f' };

	for (int i = 0; i<size; i++)
	{
		datax[i] = values[i];
	}

}

void finalExam::display(string out)
{
	cout << out << endl;
	for (int i = 0; i<SIZE3; i++)
	{
		if (i == SIZE3 - 1)
			cout << feData[i]<< endl;
		else
			cout << feData[i] << ", ";

		if (i == 4 || i == 9)
			cout << endl;
	}
}
void finalExam::sequentialSearch(char key)
{
	bool found = false;
	int numSearches = 0;
	cout << "Looking for [" << key << "] in class instance through sequential search..." << endl;

	do{
		if (feData[numSearches] == key){
			found = true;
			cout << "Found [" << key << "] in position " << numSearches << "!" << endl;
		}
		else
			numSearches++;

		if (numSearches == SIZE3)
			cout << "At end of list, did not find [" << key << "]." << endl;

	} while (found == false && numSearches <= SIZE3);




}
void display(string out, char datax[], int size)
{
	cout << out << endl;

	for (int i = 0; i<size; i++)
	{
		if (i == size - 1)
			cout << datax[i]<< endl;
		else
			cout << datax[i] << ", ";

		if (i == 4 || i == 9)
			cout << endl;
	}



}
void copyData(char datax[], char datac[], int size)
{

	for (int i = 0; i<size; i++)
	{
		datax[i] = datac[i];
	}

}

void sortDescending(char datax[], int size)
{
	bool swapped = false;
	char temp = ' ';

	do{
		swapped = false;
		for (int i = 0; i<size; i++){
			if (datax[i]<datax[i + 1])
			{
				temp = datax[i];
				datax[i] = datax[i + 1];
				datax[i + 1] = temp;
				swapped = true;
			}
		}
	} while (swapped == true);


}

int main() {
	// THE FOLLOWING PART IS WORTH 25% OF THE GRADE
	char data1[SIZE1];
	loadData(data1, SIZE1);
	display("Original data1:", data1, SIZE1);
	cout << endl << endl;

	// THE FOLLOWING PART IS WORTH 25% OF THE GRADE
	char data2[SIZE2];
	copyData(data2, data1, SIZE2); // copy first SIZE2 elements FROM data1 INTO data2
	display("Original data2:", data2, SIZE2);
	cout << endl << endl;

	// THE FOLLOWING PART IS WORTH 25% OF THE GRADE
	sortDescending(data1, SIZE1);
	display("Sorted data1 (descending):", data1, SIZE1);

	// THE FOLLOWING PART IS WORTH 25% OF THE GRADE
	finalExam fExam;
	fExam.display("Original list from finalExam class:");
	fExam.sequentialSearch('w');
	fExam.sequentialSearch('z');

}
