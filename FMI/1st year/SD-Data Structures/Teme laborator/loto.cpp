#include <bits/stdc++.h>
using namespace std;

ifstream in ("loto.in");
ofstream out ("loto.out");

struct Sum3
{

    int x,y,z;
    friend ostream& operator<<(ostream& out,const Sum3& a) {out<<a.x<<" "<<a.y<<" "<<a.z;}

};

unordered_map<int, Sum3> rez; //dictionar pt rezultat

int main()
{   int n,s,v[104],suma;
    in>>n>>s;
    for(int i=1; i<=n; i++)
         in>>v[i];
    for (int i=1; i<=n; i++)
    {  for(int j=i; j<=n; j++)
         { for(int k=j; k<=n; k++)
            {   Sum3 b;
                b.x=v[i];
                b.y=v[j];
                b.z=v[k];
                suma=v[i]+v[j]+v[k];
                rez[suma]=b;
                if(rez.find(s-suma)!=rez.end())
                {
                    out<<rez[suma]<<" "<<rez[s-suma];
                    return 0;

                }}}}

    out<<-1;
    return 0;

}
