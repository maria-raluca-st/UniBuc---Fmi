#include <bits/stdc++.h>


using namespace std;

int main()
{ string s,t;
  int i;
  long long S1=0,S2=0;
  cin>>s>>t;
  for(i=0;i<s.lenght();i++)
    S1+=(int(s[i]-'a'));
  for(i=0;i<t.lenght();i++)
    S2+=((int)(t[i])-97);
  cout<<char(S2-S1+97);
    return 0;
}
