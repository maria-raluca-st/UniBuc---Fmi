#include <bits/stdc++.h>

using namespace std;

ifstream in ("hashuri.in");
ofstream out ("hashuri.out");

#define HashNr 666013

int n,b; //b=bucket, op=operatia introdusa de la tastatura

vector<int> H[HashNr];


int f_hash(int x)
{
    b=x%HashNr;
    for(int i=0; i<H[b].size(); i++)
	     if(H[b][i]==x)
            return 1;

    return 0;
}

int main()
{
    in>>n;//n = nr op.
    for(int i=1; i<=n; i++)
    {   int op,nr,p;
        in>>op>>nr;
        if(op==1)
	    {
            b=nr%HashNr;
            if (f_hash(nr)!=1)
                H[b].push_back(nr);
        }
        if(op==2)
	    {
            b=nr%HashNr;
            int ok=0;
            for(int i=0; i<H[b].size(); i++)
            {
                if(H[b][i]==nr)
                {
                    ok=1;
                    p=i;
                }
            }
            if(ok==1)
                H[b].erase(H[b].begin()+p);
        }
        if(op==3)
            out<<f_hash(nr)<<"\n";

    }

    return 0;
}
