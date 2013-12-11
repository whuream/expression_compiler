#include"s1.h"

status::status(string str)
{
    text = str;
    index_now = 0;
    index_seg = 0;
    current_char = text[index_now];
    text.push_back('\0');
    flag = 0;
}

bool status::isDigit(char ch)
{
    return (ch >= '0' && ch <= '9');
}

bool status::isSingle(char ch)
{
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^'\
        || ch == '(' || ch == ')' || ch == ',');
}

bool status::isLetter(char ch)
{
    return ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'));
}

bool status::isCount(int count)
{
    string tmp = text.substr(index_now, count);
    if (count == 4)
    {
        return (tmp == "asin" || tmp == "acos" || tmp == "atan");
    }
    else if(count == 3)
    {
        return (tmp == "sin" || tmp == "cos" || tmp == "tan" || tmp == "log");
    }
    else if(count == 2)
    {
        return (tmp == "PI" || tmp == "ln" || tmp =="lg");
    }
    else if(count == 1)
    {
        return (tmp == "e");
    }
    return 0;
}

int status::output()
{
    tmpout<<"\nflag = "<<flag;
    //printf("flag = %d", flag);
    list<node>::iterator it = out.begin();
    for(;it != out.end(); it ++)
    {
        tmpout<<"\nFind "<<it->data<<" in "<<it->begin<<" to "<<it->end<<" type: "<<it->type;
        //fprintf(tmpout, "\nFind %s in %d to %d typeid: %d",\
            it->data.c_str(), it->begin, it->end, it->type);
        if(it->type == 1)
        {
            tmpout<<" count: "<<it->countent;
            //fprintf(tmpout, " count: %lld", it->countent);
        }
    }
    return 0;
}

int status::process()
{
    while(s0() == 0);

    handleWord();
    return 0;
}

int status::handleWord()
{
    list<node>::iterator it = out.begin();
    for(; it != out.end(); it ++)
    {
        if(isDigit(it->data[0]))
        {
            it->type = 1;           //is a number
            it->countent = calCount(it->data);
        }
        else
        {
            it->type = 0;
            it->countent = 0;
        }
    }
    output();
    return 0;
}

long long int status::calCount(string str)
{
    long long int num = 0;
    stringstream tmp(str);
    tmp>>num;
    return num;
}

int status::segEnd()
{
    node tmp;
    tmp.begin = index_seg;
    tmp.end = index_now;
    tmp.data = text.substr(index_seg,index_now - index_seg);
    out.push_back(tmp);

    index_seg = index_now;
    current_char = text[index_seg];

    //fprintf(stdout, "\nFind %s in %d to %d", tmp.data.c_str(), tmp.begin, tmp.end);

    s0();

    return 0;
}

int status::segErr()
{
    flag = -1;
    fprintf(stderr, "\nCan't resolve symbol '%c' in %d", current_char, index_now);
    update();
    index_seg = index_now;
    current_char = text[index_seg];

    s0();

    return 0;
}

int status::update()
{
    index_now ++;
    current_char = text[index_now];
    return 0;
}

int status::s0()
{
    if(isDigit(current_char))
    {
        s1();
    }
    else if(isSingle(current_char))
    {
        s2();
    }
    else if(isLetter(current_char))
    {
        s3();
    }
    else if(current_char == '\0')
    {
        return -1;
    }
    else
    {
        segErr();
    }
    return 0;
}

int status::s1()
{
    update();
    if(isDigit(current_char))
    {
        s1();
    }
    else
    {
        segEnd();
    }
    return 0;
}

int status::s2()
{
    update();
    segEnd();
    return 0;
}

int status::s3()
{
    int count = 4;
    for(;count >= 1;count --)
    {
        if(isCount(count))
        {
            index_now += count - 1;
            current_char = text[index_now];
            update();
            segEnd();
            break;
        }
    }
    if(count == 0)
    {
        segErr();
    }
    return 0;
}

