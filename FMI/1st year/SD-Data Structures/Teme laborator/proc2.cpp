#include <bits/stdc++.h>

using namespace std;

priority_queue<int> procesoare_disponibile; // procesoarele libere
priority_queue<pair<int,int>>procesoare_ocupate; // procesoarele ocupate ca perechi de timp total + procesor

ifstream in  ("proc2.in");
ofstream out ("proc2.out");


int main()
{    int N,M,si,di;
     in>>N>>M; // n=nr procesoare, m=nr taskuri
     for(int i=1;i<=N;i++)
        procesoare_disponibile.push(-i); //la inceput toate procesoarele sunt disponibile
                                        //le retinem ca nr negative pt ca ulterior folosim top in priority queue
     for(int i=1;i<=M;i++)
	 {
          in>>si>>di; //timp de inceput+durata pt fiecare task
          while( procesoare_ocupate.size()!=0 && -procesoare_ocupate.top().first<=si)
	      {   //verificam la fiecare pas daca procesoarele cu indice minim au terminat de executat taskurile
	          //daca au terminat le scoatem din procesoare_ocupate si le repunem in procesoare_disponibile
              procesoare_disponibile.push(procesoare_ocupate.top().second);
              procesoare_ocupate.pop();
          }
          procesoare_ocupate.push({-(si+di),procesoare_disponibile.top()});//la fiecare task actualizam procesoarele ocupate
          out<< -procesoare_disponibile.top()<<"\n";//afisam procesorul cu cel mai mic indice disponibil
          procesoare_disponibile.pop();
    }
 return 0;
}
