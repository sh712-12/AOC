#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    vector<char> text;
    fstream file;   
    file.open("input.txt");
    while(getline(file, text,0))
    {
        cout << text[0];
    }
}