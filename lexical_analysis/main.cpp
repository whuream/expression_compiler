#include"s1.h"

#include<iostream>
#include<cstdlib>
#include<stdio.h>
#include<fstream>

using namespace std;

int main(int argc, char** argv)
{
    if(argc != 2 && argc != 3)
    {
        fprintf(stderr, "useage: %s <inputFile> [outputFile]", argv[0]);
        return -1;
    }
    else
    {
	    freopen(argv[1], "r", stdin);
    }

    //freopen("in.txt", "r", stdin);
    string text;
    while(!cin.eof())
    {
	    string tmp;
	    getline(cin, tmp);
	    text += tmp;
    }
    status ins(text);
    ins.process();
    if(ins.flag == 0)
    {
    	if(argc == 2)
    	{
    		ofstream o("a.txt");
            o<<ins.tmpout.str();
            cout<<"\nBuild succeed\nwrite file a.txt";
    	}
        else
        {
            ofstream o(argv[2]);
            o<<ins.tmpout.str();
            cout<<"\nBuild succeed\nwrite file "<<argv[2];
        }
    }
    else
    {
        cerr<<"\nBuild failed";
    }
    return 0;
}
