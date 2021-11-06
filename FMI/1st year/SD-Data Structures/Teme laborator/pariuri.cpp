#include <bits/stdc++.h>

using namespace std;

ifstream in("pariuri.in");
ofstream out("pariuri.out");

unordered_map<int, int> suma_bani;

int main()
{   int N,M,timp, bani;
    in>>N;
    for(int i=1;i<=N;i++)
	{
        in>>M;
        for(int j=1;j<=M;j++)
        {
            in>>timp>>bani;
            suma_bani[timp] += bani;
        }
    }
    out<<suma_bani.size()<<endl;
    for(auto& it: suma_bani)
        out<<it.first<<" "<<it.second<<" ";
}
