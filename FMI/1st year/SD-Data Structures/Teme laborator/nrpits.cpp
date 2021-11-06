#include <fstream>

using namespace std;

ifstream in("nrpits.in");
ofstream out("nrpits.out");

int v[1000004],stiva[1000004];
int n,p,i;
long long ct;

int main()

{
	in>>n;
	for(i=1;i<=n;i++)
	     in>>v[i];

    for(i=1;i<=n;i++)

    {

        while(p>0 & v[i]>=v[stiva[p]])
	    {

            p--;
	        ct++;
	    }
	    if(p==0 && i!=1)
	    {
	         ct--;
        }
	    p++;
	    stiva[p]=i;

    }
	out<<ct;

    return 0;

}
