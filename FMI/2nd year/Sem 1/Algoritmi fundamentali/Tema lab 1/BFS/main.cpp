#include <bits/stdc++.h>

using namespace std;

ifstream in ("bfs.in");
ofstream out ("bfs.out");



int n, m, s , L=1;
vector <int> LA[100005]; ///lista de adiacenta
int  Coada[100005], Dmin[100005];



void BFS(int nod_start)
{

    memset(Dmin, -1, sizeof(Dmin));  /// Toate nodurile sunt nevizitate
    Dmin[nod_start] = 0; ///plecam din nodul de start
    Coada[L] = nod_start; ///nod de start introdus in coada
    for (int i = 1; i <= L; i++)	///parcurgem toate nodurile din coada
    {
        for (int j = 0; j < LA[Coada[i]].size(); j++)	/// vecinii nodului curent
            if (Dmin[LA[Coada[i]][j]] == -1) ///verificam daca sunt nevizitati
            {
                L++;
                Coada[L] = LA[Coada[i]][j]; ///adaugare vecin nevizitat in coada
                Dmin[Coada[L]] = Dmin[Coada[i]] + 1; ///se calc distanta
            }
    }
}


int main()
{


    in>>n>>m>>s;
    for (int i = 1; i <= m; i++)
    {
        int a, b;
        in>>a>>b;
        LA[a].push_back(b);
    }
    BFS(s);
    for (int i = 1; i <= n; i++)
        out<<Dmin[i]<<" ";


    return 0;

}
