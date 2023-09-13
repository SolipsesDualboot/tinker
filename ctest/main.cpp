#include <iostream>
#include "sumoftwo.hh"

int wee = 0;
int woo = 0;
bool wuu;

int main()
{
    //while(wee = 0)
        //std::cin >> wee;
        //if(std::cin.fail())
        //{
            //wee = 1;
        //}
    std::cin >> wee;
    std::cin >> woo;
    sumoftwo(wee, woo, wuu);
    std::cout << wee;
}
