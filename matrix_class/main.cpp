#include <iostream>
#include <vector>
#include "matrix.h"

int main () {
    
    // assign a 7x5 matrix to the variable initial_grid
    // all values in the matrix are 0.4
	std::vector <std:: vector <float> > 
	    initial_grid (7, std::vector <float>(5, 0.4));

    // TODO: Use the initial grid variable to instantiate a matrix object
    // The matrix object should be called matrixa
    Matrix matrixa = Matrix(initial_grid);
    matrixa.matrix_print();
    // TODO: Use the matrix_print() method to print out matrixa
    std::cout << matrixa.getRows();
    std::cout << matrixa.getCols();
    Matrix transposea = matrixa.matrix_transpose();
    transposea.matrix_print();
    // TODO: Print out the number of rows in matrixa. You will need
    // to use the getRows() function and std::cout
    
    // TODO: Print out the number of columns in matrixa 
    
    // TODO: Take the transpose of matrixa and store the results in
    // a variable called transposea

    // TODO: Print out transposea

    // Now you will use another 7x5 matrix called matrixb to 
    // give the results of the matrix_addition function
    
    // 7x5 2-dimensional vector with values 0.2
	std::vector <std:: vector <float> > 
	    second_grid (7, std::vector <float>(5, 0.2));
    Matrix matrixb = Matrix(second_grid);
    Matrix result = matrixb.matrix_addition(matrixa);
    result.matrix_print();
    // TODO: Instantiate an object called matrixb. Use the second_grid
    // variable as the input to initialize matrixb
    return 0;
}
