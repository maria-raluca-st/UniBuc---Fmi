#include <bits/stdc++.h>

using namespace std;

int n,min0=0,max0=9,i;
int v[10];
string s;

int main()
{ cin>>n;
  cin>>s;
  for(i=0;i<n;i++)
  {

      if(s[i]=='L')
      {
          while(v[min0])
          {
              min0++;


          }
          v[min0]=1;
      }
      else if(s[i]=='R')
      {
          while(v[max0])
          {
              max0--;


         }
           v[max0]=1;

      }
      else
      {
          v[int(s[i]-'0')]=0;
          min0=min(int(s[i]-'0'),min0);
          max0=max(int(s[i]-'0'),max0);
      }
}
for(i=0;i<=9;i++)
    cout<<v[i];

    return 0;
}
