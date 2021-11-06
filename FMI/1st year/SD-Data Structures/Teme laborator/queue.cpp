#include <bits/stdc++.h>

using namespace std;

ifstream in ("queue.in");
ofstream out ("queue.out");


stack <int> s1,s2;
string c;
int n,i,j,put,wr,top;
bool ok;

int main()
{
    in>>n;
    for(i=1; i<=n; i++)
    {
        out<<i<<": ";
        in>>c;
        if(c[1]=='u')//pt push
        {
            ok=1;
            put=1;
            wr=0;
            for(j=c.size()-2; ok!=0; j--)
            {
                if(c[j]=='(')
                    ok=0;
                else
                {
                    wr+=put*(int(c[j])-48);//pt a afla numarul
                    put*=10;
                }
            }
            s1.push(wr);//adaugam numarul in prima stiva
            out<<"read("<<wr<<") push(1,"<<wr<<")\n";
        }
        else //pt pop
        {
            if(s2.size()>0)
            {
                top=s2.top();
                s2.pop();
                out<<"pop(2) write("<<top<<")\n";
            }
            else
            {
                while(s1.size()!=1)
                {
                    top=s1.top();
                    s2.push(top);
                    s1.pop();


                    out<<"pop(1) push(2,"<<top<<") ";
                }
                out<<"pop(1) write("<<s1.top()<<")\n";
                s1.pop();

            }
        }
    }

    return 0;
}
