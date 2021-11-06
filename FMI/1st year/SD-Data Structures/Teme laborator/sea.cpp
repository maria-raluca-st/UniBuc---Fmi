#include<bits/stdc++.h>

using namespace std;

ifstream in ("sea.in");
ofstream out ("sea.out");

struct vapor{

    double x,y,d;

}v[404];

bool sortare(vapor V1, vapor V2)
{
        return V1.x < V2.x;
}

int Fni,id,l;

int main()
{
    int n,m;
    in>>n>>m; // n=nr de vap, m=nr de faruri

	for(int i=0; i<n; i++)
	    in>>v[i].x>>v[i].y; // coordonatele fiecarui vapor

    sort(v, v + n, sortare); // sortam dupa Vx

    for(int j=0;j<m;j++)
	{   double Fxi;
	    in>>Fxi>>Fni;                           //coordonatele orizontale şi numerele asociate farurilor
        while(l < n && v[l].x < Fxi)
            l++;
        for(int k=0;k < l;k++)
        {
            v[k].d = (v[k].x-Fxi)*(v[k].x-Fxi)+v[k].y*v[k].y;
            id = k;

            while(v[id-1].d > v[id].d  && id > 0 )
	        {
                swap(v[id-1], v[id]);
                id--;
            }
        }
        out<<fixed<<setprecision(4)<<sqrt( v[Fni-1].d )<<'\n';
    }
    return 0;

}
