#include <bits/stdc++.h>
using namespace std;

ifstream in ("muzica.in");
ofstream out ("muzica.out");

unordered_set<long long int > v(100005);
long long int a,b,c,d,e,ct,next_song,n,m,melodie;
/// ct=contor pentru nr de melodii comune
int main()
{
    in>>n>>m;
    in>>a>>b>>c>>d>>e;
    for(int i=1;i<=n;i++)
    {
        in>>melodie;
        v.insert(melodie);
    }
    for(int i=1;i<=m;i++)
    {
        if(v.find(a)!=v.end())
            {
                ct++;
                v.erase(a);
            }
        next_song=(c*b+d*a)%e;
        a = b;
        b = next_song;
    }
    out<<ct;
    return 0;
}
