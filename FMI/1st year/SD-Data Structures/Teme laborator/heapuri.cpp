#include <bits/stdc++.h>

using namespace std;

ifstream in ("heapuri.in");
ofstream out ("heapuri.out");


set<int> h; //min heap

int n,i,caz,x,j=1;
int p[200005];

int main()

{
    in>>n;
    for (i=1;i<=n;i++)
	{
        in >> caz;
        if(caz!=3)
           in>>x;

        if (caz==1)
        {

            h.insert(x);
            p[j]=x; //retinem ordinea inserarii cu ajutorul vectorului
            j++;

        }

        else if (caz==2)
        {
	        h.erase(p[x]);
        }
        else if (caz==3)
          out << *h.begin() << "\n"; //elem minim este pe prima poz in min heap

    }

    return 0;

}
