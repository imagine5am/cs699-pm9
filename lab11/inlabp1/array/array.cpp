#include <iostream>
#include <stdlib.h>

using namespace std;

/// \file

/**
* \brief <i> Fills array with random integers
*	in range [20, 420) </i>
* \details Uses rand function to generate random number. 
* \param myArr Array containing random integers	
* \return 0 on success
*/
int fillArray(int myArr[7][7])                 
{
	for(int i=0;i<7;i++)
	{
		for(int j=0;j<7;j++)                    
		{
			myArr[i][j]=20+rand()%400;              
		}
	}
	return 0;
}

/**
* \brief <i> Prints the 2-D array in spiral format </i>
* \details Each row and column are printed in a way such that output  
* 	looks spiral representation of the original array
* \pre Array needs to be filled 
* \param myArr Array containing random integers	
*/
void printSpiral(int myArr[7][7])
{
	cout << "Array Spiral Function." << endl;
	
	/// Prints first column
	for(int j=0;j<1;j++)                           
    {                                              
        for(int i=0;i<7;i++)
        {
            cout<< myArr[i][j]<< "  ";
        }

    }
    cout << endl;

    for(int i=6;i<7;i++)                          
    {                                            
        for(int j=1;j<7;j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for(int j=6;j<7;j++)                          
    {                                             
        for(int i=5;i>=0;i--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=0;i<1;i++)                          
    {                                              
        for (int j=5;j>=1;j--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int j=1; j<2;j++)
    {                                             
        for (int i=1; i<6;i++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=5; i<6;i++)                        
    {
        for (int j=2; j<6; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int j=5; j<6; j++)                        
    {
        for (int i=4; i>0; i--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=1; i<2; i++)                        
    {
       for (int j=4; j>1; j--)
       {
           cout << myArr[i][j] << "  ";
       }
    }
    cout << endl;

    for (int j=2; j<3; j++)                        
    {
        for (int i=2; i<5; i++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=4; i<5; i++)                        
    {
        for (int j=3; j<5; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int j=4; j<5; j++)                        
    {
        for (int i=3; i>1; i--)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=2; i<3; i++)                        
    {
        for (int j=3; j<4; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
    cout << endl;

    for (int i=3; i<4; i++)                         
    {
        for (int j=3; j<4; j++)
        {
            cout << myArr[i][j] << "  ";
        }
    }
  cout << endl << endl;
}

/**
* \brief <i> Prints columns of 2-D array </i>
* \details Prints columns specified in range [s-1, e-1) in row format
* \pre Array needs to be filled
* \param myArr Array containing random integers	
* \param s Start index
* \param e End index 
*/
void printCol(int myArr[7][7], int s, int e)                     
{  
	cout << "Column Output" << endl;                
	for (int j=s-1; j<e-1; j++)
	{                                               
		for (int i=0; i<7; i++)
		{
			cout << myArr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl << endl;
}

/**
* \brief <i> Finds minimum number in the array </i>
* \details Goes through each element to find the minimum
* \pre Array needs to be filled
* \param myArr Array containing random integers	
* \returns An integen having minimum value
*/
int findMin (int myArr[7][7])
{
	int i,j;
	int min = myArr[0][0];

	for (i=0; i<7; i++)                             
	{
		for (j=0; j<7; j++)
		{
			if(myArr[i][j] < min)                   
			{                                       
				min = myArr[i][j];
			}                                       
		}                                           

	}
    return min;
}

/**
* \brief <i> Finds average of the elements in the array </i>
* \details Sums up each element in the array and divides
* 	by total number of elements in the array
* \pre Array needs to be filled
* \param myArr Array containing random integers	
* \returns An integer specifying average of elements
*/
int findAverage (int myArr[7][7])                  
{                                                   
	int i,j;
	int sum = 0;

	for (i=0; i<7; i++)                             
	{
	    for (j=0; j<7; j++)
	    {
	        sum = sum + myArr[i][j];
	    }

	}
    return sum/49;       
}

/** \brief  Prints array
* \details Prints array row by row
* \pre Array needs to be filled
* \param myArr Array containing random integers
*/ 
void printArray (int myArr[7][7])                     
{
    cout << "Normal Array Output" << endl;

    for (int i =0; i<7; i++)
    {
        for (int j=0; j<7; j++)
        {
            cout << myArr[i][j] << "  ";
        }
        cout << endl;
    }
    cout << endl;                                   
    cout << endl;
}

/** \brief <i> Main Method </i>
* \details This function is invoked when the program starts executing
*/
int main(){
	
	int myArr [7][7];
	fillArray(myArr);                               
	printArray(myArr);
	printSpiral(myArr);
	printCol(myArr, 2, 5);
	cout<<"Min:"<<findMin(myArr);
	cout<<" Average:"<<findAverage(myArr);
    cout<<endl;

	return 0;
}
 