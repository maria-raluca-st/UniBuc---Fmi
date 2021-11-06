#include <bits/stdc++.h>

using namespace std;

ifstream in ("paranteze.in");
ofstream out ("paranteze.out");

int a[10000001],v[10000001];
int p,maxi,n;
char s[1000001];

int paranteza(char c)
{
    if(c=='(') return 1;
    if(c==')') return -1;

    if(c=='[') return 2;
    if(c==']') return -2;

    if(c=='{') return 3;
    if(c=='}') return -3;

}

int main()
{
    in>>n;
    in>>s;
    for(int i=0; i<n; i++)
    {

        p=paranteza(s[i]);
        if(p>0)
            a[++a[0]]=p;
        else if(p<0)
        {
            if(p+a[a[0]]==0)
            {
                v[a[0]-1]+=v[a[0]]+2;
                v[a[0]]=0;
                a[0]--;
                if(v[a[0]]>maxi)
                    maxi=v[a[0]];
            }
            else a[++a[0]]=p;
        }
    }
    out<<maxi;


    return 0;
}
