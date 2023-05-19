#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream input (argv[1], ifstream::in);
    string val;
    u_int64_t sum = 0;
    vector<u_int64_t> sums;
    while(getline(input, val))
    {
        
        if(!val.empty())
        {
            sum+=stoul(val);
        }
        else
        {
            sums.push_back(sum);
            sum = 0;
        }

    }
    sort(sums.begin(), sums.end(), greater<u_int64_t>());

    //part 1
    cout << "Part 1: " << sums[0] << endl;

    //part 2
    cout << "Part 2: " << sums[0]+sums[1]+sums[2] << endl;

}