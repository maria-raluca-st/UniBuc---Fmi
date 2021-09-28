#include <bits/stdc++.h>

using namespace std;

ifstream in ("lfa.in");
ofstream out ("lfa.out");

char t[100][100];
int sf[100];
int n,m,i,j,init,f,a,b;
char tranz;
int frontstocare,backstocare;

struct stocare
{

    char cuv[50];

    int frontcuv,stare;
    int drum[100];
    int ldrum;


} v[1000];

void verifcuv()
{
    int ok=0,j;
    while(ok == 0)
    {

        if(frontstocare>backstocare)
        {

            ok=1;
            out<<"NU"<<endl;
        }
        else if(v[frontstocare].frontcuv==strlen(v[frontstocare].cuv))//verif. daca cuv este vid
        {

            for(int k=1; k<=f; k++)
            {
                if(v[frontstocare].stare==sf[k])//verif daca starea curenta este finala
                {
                    ok=1;
                    out<<"DA"<<endl; //daca este afisam da
                    out<<"Traseu: ";
                    for(int z=1; z<=v[frontstocare].ldrum; z++)
                        out<<v[frontstocare].drum[z]<<" "; //afisam traseul
                    out<<endl;

                }
            }
        }
        else
        {
            for(j = 0 ; j < n ; j++)
            {


                if(v[frontstocare].cuv[v[frontstocare].frontcuv]==t[v[frontstocare].stare][j])
                {


                    backstocare++;
                    strcpy(v[backstocare].cuv,v[frontstocare].cuv);
                    v[backstocare].frontcuv=v[frontstocare].frontcuv+1;
                    v[backstocare].stare=j;

                    for(int r=1; r<=v[frontstocare].ldrum; r++)
                    {
                        v[backstocare].drum[r]=v[frontstocare].drum[r];
                    }
                    v[backstocare].ldrum=v[frontstocare].ldrum+1;
                    v[backstocare].drum[v[backstocare].ldrum]=j;

                }
            }
        }
        frontstocare++;

    }
}



int main()

{
    in>>n>>m; // n=nr noduri , m=nr muchii
    for(i = 1 ; i <= m ; i++)
    {
        in>> a >> b >> tranz;
        t[a][b]=tranz; //punem in matrice litera corespunzatoare muchiei

    }

    in>>init; // init=nod stare initiala
    in>>f; // f=nr noduri finale

    for(i=1; i<=f; i++)
    {
        in>>sf[i]; //sf=nodurile finale
    }

    int nrstring;
    in>>nrstring; //nr cuvinte introduse pentru verificare

    char cuvant[50];
    for(i=1; i<=nrstring; i++)
    {
        in>>cuvant; //cuvinte introduse pt verificare
        strcpy(v[1].cuv,cuvant);
        v[1].frontcuv=0;
        v[1].stare=init;
        v[1].drum[1]=init;
        v[1].ldrum=1;
        frontstocare=1;
        backstocare=1;
        verifcuv();
    }

    return 0;
}
