#include <bits/stdc++.h>

using namespace std;

ifstream in ("file.in");
ofstream out ("file.out");

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
        else if(v[frontstocare].frontcuv==sizeof(v[frontstocare].cuv))
        {
            for(int k=1; k<=f; k++)
            {
                if(v[frontstocare].stare==sf[k])
                {
                    ok=1;
                    out<<"DA"<<endl;
                    out<<"Traseu: ";
                    for(int z=1; z<=v[frontstocare].ldrum; z++)
                        out<<v[frontstocare].drum[z]<<" ";
                    out<<endl;

                }
            }
        }
        else
        {
            for(j = 1 ; j <= n ; j++)
            {
                if(v[frontstocare].cuv[v[frontstocare].frontcuv]==t[v[frontstocare].stare][j])
                {
                    backstocare++;
                    strcpy(v[backstocare].cuv,v[frontstocare].cuv);
                    v[backstocare].frontcuv=v[frontstocare].frontcuv+1;
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
    //memset(t,0,sizeof(t));

    //int n,m,i,j,init,f,a,b;
    in>>n>>m;
    //char t[n+5][n+5];

    for(i = 1 ; i <= m ; i++)
    {
        in>> a >> b >> tranz;
        t[a][b]=tranz;

    }
    in>>init;
    in>>f;
    //int sf[f+5];
    for(i=1; i<=f; i++)
    {
        in>>sf[i];
    }
    int nrstring;
    in>>nrstring;
    char cuvant[50];
    for(i=1; i<=nrstring; i++)
    {
        in>>cuvant;
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
