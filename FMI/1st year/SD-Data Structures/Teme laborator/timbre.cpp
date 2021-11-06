#include<bits/stdc++.h>

using namespace std;

ifstream in("timbre.in");
ofstream out("timbre.out");

priority_queue <int, vector<int>, greater<int>> heap1; //de min dupa cost
priority_queue <pair<int, int>> heap2; //de max dupa marg sup


int N,M,K,i,j,ct,mi,ci,Smin;

int main()
{
    in>>N>>M>>K;
    for (i=1;i<=M;i++)
    {
        in>>mi>>ci;
        heap2.push({mi, ci}); //retinem in heap2 pt a const. heap1
    }
    ct=N;
    while (ct>0)
	{
        while(heap2.size()!=0 && heap2.top().first >= ct)
        {
            heap1.push(heap2.top().second);
            heap2.pop();
        }
        Smin += heap1.top();
        ct -= K;
        heap1.pop();
    }
    out<<Smin;
    return 0;
}
