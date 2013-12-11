#include<string>
#include<list>
#include<sstream>

using namespace std;

#include<stdio.h>


class node
{
public:
    int begin;
    int end;
    string data;
    int type;
    long long int countent;
};

class status
{
public:
    int index_now;
    int index_seg;
    string text;
    char current_char;
    list<node> out;
    int flag;

    status(string str);
    bool isDigit(char ch);
    bool isSingle(char ch);
    bool isLetter(char ch);

    stringstream tmpout;

    bool isCount(int count);

    int segEnd();
    int segErr();
    int output();

    int update();

    int s0(); //begin
    int s1(); //digit
    int s2(); //single
    int s3(); //letter

    int handleWord();

    int process();

    long long int calCount(string str);

private:

};
