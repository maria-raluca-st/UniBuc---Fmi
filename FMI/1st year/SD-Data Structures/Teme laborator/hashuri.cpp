#include <bits/stdc++.h>

using namespace std;

ifstream in ("hashuri.in");
ofstream out ("hashuri.out");

unordered_map<int, int> h;
int n,c;
long long x;

int main()

{
	in>>n;
	for(int i=1;i<=n;i++)
	{

        in>>c>>x;

        if(c == 1)
	    { h[x]=1; }
        else if(c == 2)
	    {  h.erase(x); }
        else if(c == 3)
	    {

            if(h.find(x) != h.end())
	              out<<1<<'\n';

            else
                out<<0<<'\n';

         }}

    return 0;

}
