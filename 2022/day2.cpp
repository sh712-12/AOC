#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream input (argv[1], ifstream::in);

    string s;
    int score1 = 0;
    int score2 = 0;
    map<string, int> scores1{{"A X", 4}, {"A Y", 8}, {"A Z", 3}, {"B X", 1}, {"B Y", 5}, {"B Z", 9}, {"C X", 7}, {"C Y", 2}, {"C Z", 6}};
    map<string, int> scores2{{"A X", 3}, {"A Y", 4}, {"A Z", 8}, {"B X", 1}, {"B Y", 5}, {"B Z", 9}, {"C X", 2}, {"C Y", 6}, {"C Z", 7}}; 
    while(getline(input, s))
    {
        cout << s << endl;
        score1 += scores1[s];
        score2 += scores2[s];
    }
    cout << "Part 1: " << score1 << endl;
    cout << "Part 2: " << score2 << endl;

    return 0;
}