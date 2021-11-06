#include <bits/stdc++.h>

using namespace std;

ifstream in ("vila2.in");
ofstream out("vila2.out");

int n,i,k,k1,f1=1,b1=0,f2=1,b2=0; // f=front,b=back, f>b=deque vid
int a[5000010],d[5000010],d2[5000010];
long long D,Dmax; //diferenta curenta, diferenta maxima

int main()
{
    in>>n>>k1;
    k=k1+1;
    for(i=1; i<=n; i++)
        in>>a[i]; //citim sirul dat
    for(i=1; i<=n; i++)
    {
        while (f1<=b1 && a[i]<=a[d[b1]])
            b1--;
        d[++b1] = i;  // Adaugam pozitia elementului curent in deque pt minim
        if (d[f1] == i-k) f1++;

        while (f2<=b2 && a[i]>=a[d2[b2]])
            b2--;
        d2[++b2] = i;  // Adaugam pozitia elementului curent in deque pt maxim
        if (d2[f2] == i-k) f2++;

        if (i >= k)
            {  D=a[d2[f2]]-a[d[f1]];

               if(D>Dmax)
                 Dmax=D;
            }
    }
    out<<Dmax;

    return 0;
}
