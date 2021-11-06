#include <bits/stdc++.h>

using namespace std;

ifstream in ("alibaba.in");
ofstream out ("alibaba.out");

int n,k,poz=1,poz1;
int v[10004];
int j,cmax,aux=0,aux2=0,i;
char c;

int main()
{  in>>n>>k;
   aux=n-k;
   for(i=1;i<=n;i++)
   {
       in>>c;
       v[i]=(int)(c-'0');

   }

   for(i=1;i<=aux;i++)
   {
       aux2=poz+k;
       cmax=0;
       for(j=poz; j<=aux2 && j<=n;j++)
       {
           if(v[j]>cmax)
           {
               cmax=v[j];
               poz1=j;
           }
       }
       out<<cmax;
       k=k-poz1+poz;
       poz=poz1+1;
   }


    return 0;
}
