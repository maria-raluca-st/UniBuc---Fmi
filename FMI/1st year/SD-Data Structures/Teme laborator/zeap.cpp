#include <bits/stdc++.h>

using namespace std;
ifstream in ("zeap.in");
ofstream out ("zeap.out");

bool compare(const pair<int,int> &a,const pair<int,int> &b)
{

    return a.second-a.first < b.second-b.first; /// sortam perechile dupa dif minima

}

set <int> Set;
string comanda;
priority_queue < pair<int,int> , vector<pair<int,int>> , decltype(&compare) > difs(compare);
set<int>::iterator first, last;

int main()
{
    while(in>>comanda)
    {
        if(comanda=="I") ///citim elementul, verificam daca este in set
        {
            int x;
            in>>x;
            auto element = Set.find(x);
            if(element == Set.end())  ///daca elementul nu este in set
            {
                Set.insert(x); ///atunci il inseram
                element = Set.find(x);
                if(element != Set.begin())
                {
                    auto ant=element;
                    ant--;
                    difs.push(make_pair(*element,*ant)); ///si punem diferenta dintre cele 2 pozitii vecine in pq
                }
                auto urm=element;
                urm++;
                if(urm != Set.end()) ///daca elem este in set
                {
                    difs.push(make_pair(*urm, *element));
                }
            }

        }
        if(comanda=="S") ///comanda de stergere stergem elementul  si adaugam noua diferenta
        {
            int x;
            in>>x;   ///citim elementul
            auto element=Set.find(x); ///cautam elementul
            if(element !=Set.end())  ///daca se gaseste in set
            {
                auto urm = element;
                urm++;
                if(element !=Set.begin() && urm !=Set.end())
                {
                    element--; ///elementul anterior
                    difs.push(make_pair(*urm,*element)); ///punem diferenta dintre urm elem dupa x si cel ant
                }
                Set.erase(x); ///stergem elementul
            }
            else out<<-1<<'\n'; ///altfel afisam -1

        }
        if(comanda=="C") /// comanda pt cautarea elementului in set
        {
            int x;
            in>>x;   ///citim elementul
            if(Set.find(x)!=Set.end()) ///daca il gasim afisam 1, altfel 0
                out<<1<<'\n';
            else out<<0<<'\n';
        }
        if(comanda=="MIN") ///comanda pt diferenta minima
        {
            if(Set.size()<2) ///daca avem  <2 elem nu outem afla dif  minima
                out<<-1<<'\n';
            else
            {
                while( Set.find(difs.top().first)==Set.end() || Set.find(difs.top().second)==Set.end()) ///daca elem nu mai sunt in set, eliminam diferentele din pq
                {
                    difs.pop();
                }
                out<<difs.top().first-difs.top().second<<'\n'; ///afisam cea mai mica dif dintre elem care sunt in set
            }
        }
        if(comanda=="MAX") ///comanda pt maxim
        {
            if(Set.size()<2) ///daca  nu mai avem 2 numere nu putem gasi dif maxima si afisam -1
                out<<-1<<'\n';
            else
            {   ///dif maxima va fi cea dintre primul elem si ultimul
                int poz1,poz2;
                first=Set.begin();
                last=Set.end();
                last--;
                out<<(*last-*first)<<'\n';
            }
        }
    }
    return 0;
}
