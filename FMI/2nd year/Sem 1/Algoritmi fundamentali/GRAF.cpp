/*
BFS
https://infoarena.ro/job_detail/2795637

DFS
https://infoarena.ro/job_detail/2796109

CTC
https://infoarena.ro/job_detail/2796319?action=view-source

CB
https://infoarena.ro/job_detail/2798041?action=view-source


// SORTARET
https://infoarena.ro/job_detail/2795685?action=view-source


// MUCHIE CRITICA
https://leetcode.com/submissions/detail/585789643/

// DARB
https://infoarena.ro/problema/darb

//Roy Floyd
https://www.infoarena.ro/job_detail/2815607

*/


#include <bits/stdc++.h>

using namespace std;



ifstream in("grafuri.in");
ofstream out("grafuri.out");

#define maxi 100001
#define INF 0x3f3f3f3f

class Graf
{

    int n, m;  //n = nr. noduri , m =nr. muchii
    vector<int> *LA; // lista de adiacenta

public:

    Graf();
    ~Graf();

    ///BFS
    // void citireBFS();
    // void BFS(int nod_start);
    // void afisareBFS();
    void BFS_infoarena();

    ///DFS
    //void citireDFS();
    void DFS(int s, int vizitat[maxi]);
    void afisareDFS();
    void DFS_infoarena();

    ///CTC - Kosaraju
    void citireCTC();
    void DFS1(int nod, int vizitat[maxi], vector <int>& S);
    void DFS2(int nod, int vizitat2[maxi],vector <int> LAT[], int& CT_ctc, vector <int> *CTC);
    void afisareCTC();
    void CTC_infoarena1();


    ///Biconex
    void dfsbiconex(int curent, int precedent, int vizitat[maxi],vector <set <int>>& componente,stack<pair<int, int>>& stivaCB,int& moment,int minim[maxi],vector<int>& discovery);
    void afisareCB();

    ///SORTARET
    void citireSortareTopologica();
    void sortareTopologica();

    ///HAVEL HAKIMI
    void HavelHakimi();

    ///MUCHIE CRITICA
    void dfsMC(int nod, int prev, int& moment, int minim[maxi], int discovery[maxi]);
    void afisareMC();

    ///ROY FLOYD
    void RoyFloyd();

    ///DARB
    void DFS_Darb(int curr,int drum[maxi],int& dmax, int& nodmax);
    int Darb_infoarena();

    ///Djikstra
    void Dijkstra(int nod_start, int dmin[], int viz[],vector<pair<int,int>> la[50005]);
    int Dijkstra_infoarena();

    ///Bellman Ford
    void BF(int nod_start, int dmin[], int viz[],vector<pair<int,int>> la[50005],bool negativ);
    int BF_infoarena();

    ///Paduri de multimi disjuncte
    int find_root(int node , int parent[]);
    void union_k(int x,int y , int parent[] , int dim[]);
    void Disjoint_infoarena();

    ///APM
    int kruskall(vector<pair<int,pair<int,int>>>& edges, int parent[] , int dim[],vector<pair<int,int>>& res);
    void Apm_infoarena();

};

///CONSTRUCTOR

Graf::Graf()
{
    n = m  = 0;
    LA = new vector<int>[maxi];
}

///DESTRUCTOR

Graf::~Graf()
{
    delete[] LA;
}



/// BFS

void Graf :: BFS_infoarena()
{
    int Dmin[maxi] = {0};
    int nod_start;
    queue<int> coada;
    in >> n >> m >> nod_start;
    for (int i = 1; i <= m; i++)
    {
        int a,b;
        in >> a >> b;
        LA[a].push_back(b);
    }
    memset(Dmin, -1, sizeof(Dmin));
    Dmin[nod_start] = 0;
    coada.push(nod_start);

    while(!coada.empty())
    {
        nod_start = coada.front();
        coada.pop();
        for (int j = 0; j < LA[nod_start].size(); j++)
        {
            if (Dmin[LA[nod_start][j]] == -1)
            {
                coada.push(LA[nod_start][j]);
                Dmin[LA[nod_start][j]] = Dmin[nod_start] + 1;

            }
        }
    }
    for (int i = 1; i <= n; i++)
        out<<Dmin[i]<<" ";
}


///DFS


void Graf::DFS(int nod,int vizitat[maxi])
{

    vizitat[nod] = 1;

    for (int i = 0; i < LA[nod].size(); i++)
        if (!vizitat[LA[nod][i]])
            DFS(LA[nod][i], vizitat);

}

void Graf :: DFS_infoarena()
{
    //citireDFS();
    int ct = 0;
    in >> n >> m;
    int vizitat[maxi] = {0};
    for (int i = 1; i <= m; i++)
    {
        int a,b;
        in >> a >> b;
        LA[a].push_back(b);
        LA[b].push_back(a);
    }


    for (int i = 1; i <= n; i++)
        if (vizitat[i] == 0)
        {
            DFS(i, vizitat);
            ct++;
        }
    out << ct;
}


///Componente Tare Conexe


void Graf::DFS1(int nod, int vizitat[maxi], vector <int>& S)
{
    vizitat[nod] = 1;
    for (int i = 0; i < LA[nod].size(); i++)
        if (!vizitat[LA[nod][i]])
        {
            DFS1(LA[nod][i], vizitat, S);
        }
    S.push_back(nod);
}


void Graf::DFS2(int nod, int vizitat2[maxi], vector <int> LAT[], int& CT_ctc, vector <int>* CTC)
{

    vizitat2[nod] = 1;
    //out<< nod <<" ";
    CTC[CT_ctc].push_back(nod);
    for (int i = 0; i < LAT[nod].size(); i++)
        if (!vizitat2[LAT[nod][i]])
        {
            DFS2(LAT[nod][i], vizitat2,LAT,CT_ctc,CTC);
        }
}


void Graf::CTC_infoarena1()
{
    vector <int> *CTC = new vector<int>[maxi];
    int CT_ctc = 0;
    int vizitat[maxi] = {0};
    int vizitat2[maxi] = {0};
    vector <int> S;
    vector <int>* LAT;
    LAT = new vector<int>[maxi];

    in >> n >> m;
    for (int i = 1; i <= m; i++)
    {
        int a,b;
        in >> a >> b;
        LA[a].push_back(b);
        LAT[b].push_back(a);
    }

    for(int i = 1; i <= n; i++)
    {
        if(vizitat[i] == 0)
        {
            DFS1(i, vizitat, S);
            // ct++;
        }
    }

    for( int i = S.size()-1 ; i >= 0 ; i--)
    {
        //out<<S[i]<<" ";
        int v = S[i];
        if(vizitat2[v] == 0)
        {
            DFS2(v, vizitat2,LAT,CT_ctc,CTC);
            //out<<'\n';
            CT_ctc++;
        }
    }
    out<<CT_ctc<<'\n';
    for( int i = 0 ; i < CT_ctc ; i ++)
    {
        for(int j = 0; j < CTC[i].size(); j++)
            out<<CTC[i][j]<<" ";
        out<<'\n';
    }

}




///Componente biconexe


void Graf::dfsbiconex(int nod_curent, int nod_precedent, int vizitat[maxi],vector <set <int>>& componente,stack<pair<int, int>>& stivaCB,int& moment,int minim[maxi],vector<int>& discovery)
{

    discovery[nod_curent] = moment;
    minim[nod_curent] = moment;
    vizitat[nod_curent] = 1;
    moment++;

    for(int i=0 ; i < LA[nod_curent].size() ; i++)
    {
        int nod_adiacent = LA[nod_curent][i];

        if (vizitat[nod_adiacent] == 0)
        {
            stivaCB.push(make_pair(nod_curent, nod_adiacent));
            dfsbiconex(nod_adiacent, nod_curent, vizitat,componente,stivaCB,moment,minim, discovery);

            if (minim[nod_curent] > minim[nod_adiacent])
                minim[nod_curent] = minim[nod_adiacent];

            if (minim[nod_adiacent] >= discovery[nod_curent]) ///comp. biconexa
            {
                set<int> noduri_cb; ///setul cu nodurile din componenta biconexa
                int nod1, nod2;
                do
                {
                    nod1 = stivaCB.top().first;
                    nod2 = stivaCB.top().second;
                    noduri_cb.insert(nod1);
                    noduri_cb.insert(nod2);
                    stivaCB.pop();
                }
                while (nod1 != nod_curent || nod2 != nod_adiacent);
                componente.push_back(noduri_cb);
            }
        }
        else
        {
            if (minim[nod_curent] > discovery[nod_adiacent])
            {
                minim[nod_curent] = discovery[nod_adiacent];
            }
        }
    }
}


void Graf::afisareCB()
{
    stack<pair<int, int>> stivaCB;
    int minim[maxi] = {0};
    vector<int> discovery(n+1);
    //stack<pair<int, int>> stivaCB;
    int vizitat[maxi] = {0};
    int moment = 1;
    //cout<<111;
    //int discovery[maxi] = {0}, minim[maxi] = {0};
    //cout<<2222;
    in >> n >> m;
    vector <set <int>> componente;
    for (int i = 1; i <= m; i++)
    {
        int a,b;
        in >> a >> b;
        LA[a].push_back(b);
        LA[b].push_back(a);
    }
    dfsbiconex(1, 0, vizitat,componente,stivaCB, moment,minim, discovery);
    out<< componente.size() <<'\n';

    set<int>::iterator it;

    for (auto &i: componente)
    {
        for (it = i.begin(); it != i.end(); it++)
        {
            out << *it << " ";
        }
        out << "\n";
    }

}

///SORTARET


void Graf::sortareTopologica()
{
    in >> n >> m;
    vector <int> S;
    for (int i = 1; i <= m; i++)
    {
        int a,b;
        in >> a >> b;
        LA[a].push_back(b);
    }

    int vizitat[maxi] = {0};
    for(int i=1; i<=n; i++)
    {
        if(vizitat[i]==0)
            DFS1(i,vizitat,S);
    }
    for( int i=S.size() -1; i>=0; i--)
        out<<S[i]<<" ";
}

///Havel Hakimi

void Graf::HavelHakimi()
{
    vector<int> arr;
    in>>n;
    for(int i = 0 ; i < n ; i++)
    {
        int elem;
        in>>elem;
        arr.push_back(elem);

    }

    while (1)
    {

        sort(arr.begin(), arr.end());
        if (arr[arr.size()-1] == 0)
        {
            ///daca toate elem sunt 0 , rasp este da
            out<<"DA";
            break;
        }

        int v = arr[0];
        arr.erase(arr.begin());


        if (v > arr.size())
        {
            out<<"NU";
            break;
        }

        for (int i = 0; i < v; i++)
        {
            arr[i]--;
            if (arr[i] < 0)
            {
                out<<"NU";
                break;

            }
        }
    }

}

///MUCHIE CRITICA


void Graf::dfsMC(int nod, int prev,int& moment, int minim[maxi], int discovery[maxi])
{
    discovery[nod] = minim[nod] = moment++;
    for (int i = 0; i < LA[nod].size(); i++)
    {
        int next = LA[nod][i];
        if (discovery[next] == 0)
        {
            dfsMC(next, nod, moment, minim, discovery);
            minim[nod] = min(minim[nod], minim[next]);
            if (minim[next] > discovery[nod])
            {
                //ans.push_back({nod, next});
                out<<nod<<" "<<next<<endl;
            }
        }
        else if (next != prev)
            minim[nod] = min(minim[nod], discovery[next]);
    }
}

void Graf::afisareMC()
{
    int moment = 1;
    in >> n >> m;
    int vizitat[maxi] = {0};
    int minim[maxi] = {0};
    int discovery[maxi] = {0};
    for (int i = 1; i <= m; i++)
    {
        int a,b;
        in >> a >> b;
        LA[a].push_back(b);
        LA[b].push_back(a);
    }
    dfsMC(0, -1, moment, minim, discovery);
    //return ans;

}

///ROY FLOYD
void Graf::RoyFloyd()
{
    int m[101][101],a[101][101];
    int n;

    in>>n;
    for(int i = 1 ; i <= n ; i++)
    {
        for(int j = 1 ; j <= n ; j++)
        {
            in>>m[i][j];
            if(m[i][j] != 0)
                a[i][j]=m[i][j];
            else
                a[i][j] = INF;
        }
    }
    for(int k = 1 ; k <= n ; k++)
        for(int i = 1 ; i <=n ; i++)
            for(int j  = 1 ; j <=n ; j++)
                a[i][j] = min(a[i][j], a[i][k] + a[k][j]);

    for(int i = 1 ; i <= n ; i++)
    {
        for(int j = 1 ; j <= n ; j++)
        {
            if(i == j || a[i][j] == INF)
                a[i][j] = 0;
            out<<a[i][j]<<" ";
        }
        out<<"\n";
    }

}

///DARB
void Graf::DFS_Darb(int curr,int drum[maxi],int& dmax, int& nodmax)
{

    for(int i = 0; i < LA[curr].size(); i++)
    {
        if(!drum[LA[curr][i]])
        {
            drum[LA[curr][i]]=drum[curr] + 1;
            if(drum[LA[curr][i]] >= dmax)
            {
                dmax=drum[LA[curr][i]];
                nodmax = LA[curr][i];
            }
            DFS_Darb(LA[curr][i], drum, dmax, nodmax);
        }
    }
}


int Graf::Darb_infoarena()
{
    int n;
    in>>n;
    int drum[maxi];
    int dmax = 0, nodmax = 0;
    for(int i=1; i<=n-1; i++)
    {
        int a,b;
        in>>a>>b;
        LA[a].push_back(b);
        LA[b].push_back(a);
    }
    drum[1]=1;
    DFS_Darb(1, drum, dmax, nodmax);

    dmax = 0;
    memset(drum,0,sizeof(drum));

    drum[nodmax] = 1;
    DFS_Darb(nodmax, drum, dmax, nodmax);

    out <<dmax;
}


///Djikstra

void Graf::Dijkstra(int nod_start, int dmin[], int viz[],vector<pair<int,int>> la[50005])
{
    priority_queue<pair<int,int>> pq;



    dmin[nod_start]=0;
    pq.push({0,nod_start});

    while(pq.empty() != true)
    {
        int nod_curent = pq.top().second;
        pq.pop();
        if(viz[nod_curent] == 0)
        {
            viz[nod_curent] = 1;
            for(auto nod_vecin : la[nod_curent])
            {
                if(dmin[nod_vecin.first] > dmin[nod_curent]+nod_vecin.second)
                {
                    dmin[nod_vecin.first] = dmin[nod_curent] + nod_vecin.second;
                    pq.push({-dmin[nod_vecin.first],nod_vecin.first});
                }
            }
        }
    }
}

int Graf::Dijkstra_infoarena()
{
    int dmin[50005],viz[50005];
    //memset(dmin , 0, sizeof(dmin));
    memset(viz, 0,sizeof(viz));
    vector<pair<int,int>> la[50005];

    in>>n>>m;

    for(int i=1; i<=n; i++)
        dmin[i]=INT_MAX;

    for(int i=1; i<=m; i++)
    {
        int x,y,w;
        in>>x>>y>>w;
        la[x].push_back({y,w});
    }

    Dijkstra(1, dmin, viz, la);
    for(int i=2; i<=n; i++)
    {
        if(dmin[i] == INT_MAX)
            out<<0<<" ";
        else
            out<<dmin[i]<<" ";
    }

}

///Bellman Ford

void Graf::BF(int nod_start, int dmin[], int viz[],vector<pair<int,int>> la[50005],bool negativ)
{
    priority_queue<pair<int,int>> pq;



    dmin[nod_start]=0;
    pq.push({0,nod_start});

    while(pq.empty() != true)
    {
        int nod_curent = pq.top().second;
        pq.pop();
        if(viz[nod_curent] == 0)
        {
            viz[nod_curent] = 1;
            if(viz[nod_curent]>=n)
            {
                negativ=1;
                out<<"Ciclu negativ!";
                return;

            }
            for(auto nod_vecin : la[nod_curent])
            {
                if(dmin[nod_vecin.first] > dmin[nod_curent]+nod_vecin.second)
                {
                    dmin[nod_vecin.first] = dmin[nod_curent] + nod_vecin.second;
                    pq.push({-dmin[nod_vecin.first],nod_vecin.first});
                }
            }
        }
    }
}

int Graf::BF_infoarena()
{
    int dmin[50005],viz[50005];
    bool negativ = 0;
    //memset(dmin , 0, sizeof(dmin));
    memset(viz, 0,sizeof(viz));
    vector<pair<int,int>> la[50005];

    in>>n>>m;

    for(int i=1; i<=n; i++)
        dmin[i]=INT_MAX;

    for(int i=1; i<=m; i++)
    {
        int x,y,w;
        in>>x>>y>>w;
        la[x].push_back({y,w});
    }

    BF(1, dmin, viz, la, negativ);
    if(!negativ)
    for(int i=2; i<=n; i++)
    {
        if(dmin[i] == INT_MAX)
            out<<0<<" ";
        else
            out<<dmin[i]<<" ";
    }

}

///Paduri de multimi disjuncte + APM

int Graf::find_root(int node , int parent[])
{
    while(node != parent[node])
        node=parent[node];

    return node;
}


void Graf::union_k(int x,int y , int parent[] , int dim[])
{
    int root_x=find_root(x ,parent);
    int root_y=find_root(y  , parent);

    if(dim[root_x]>=dim[root_y])
    {
        parent[root_y]=root_x;
        dim[root_x]+=dim[root_y];
    }
    else
    {
        parent[root_x] = root_y;
        dim[root_y] += dim[root_x];
    }
}

void Graf::Disjoint_infoarena()
{
    int parent[200005], dim[200005];
    in>>n>>m;

    for(int i=1; i<=n; ++i)
    {
        dim[i]=1;
        parent[i]=i;
    }
    for(int i=1; i<=m; i++)
    {
        int x,y,tip;
        in>>tip>>x>>y;
        //edges.push_back({w,{x,y}});
        if(tip == 1)
            union_k(x,y,parent, dim);
        else
        {
            if(find_root(x,parent) != find_root(y , parent))
            {
                out<<"NU"<<"\n";
            }
            else
                out<<"DA"<<"\n";
        }
    }


}

///Arbore partial de cost minim

int Graf::kruskall(vector<pair<int,pair<int,int>>>& edges, int parent[] , int dim[],vector<pair<int,int>>& res)
{

    int min_weight = 0;
    sort(edges.begin(), edges.end());


    for(auto edge : edges)
    {

        if(find_root(edge.second.first,parent) != find_root(edge.second.second,parent))
        {
            min_weight += edge.first;
            union_k(edge.second.first, edge.second.second, parent, dim);
            res.push_back({edge.second.second, edge.second.first});
        }
    }
    return min_weight;

}

void Graf::Apm_infoarena()
{
    in>>n>>m;
    vector<pair<int,pair<int,int>>> edges;
    vector<pair<int,int>> res;
    int parent[200005], dim[200005];

    for(int i=1; i<=n; ++i)
    {
        dim[i]=1;
        parent[i]=i;
    }
    for(int i=1; i<=m; i++)
    {
        int x,y,w;
        in>>x>>y>>w;
        edges.push_back({w,{x,y}});
    }
    out<<kruskall(edges, parent , dim , res)<<"\n";

    out<<res.size()<<"\n";
    for(int i=0; i<res.size(); i++)
       out<<res[i].first<<" "<<res[i].second<<"\n";

}


int main()
{
    Graf g1;

    //g1.BFS_infoarena();
    //g1.DFS_infoarena();
    //g1.CTC_infoarena1();
    //g1.afisareCB();
    //g1.sortareTopologica();
    //g1.HavelHakimi();
    //g1.afisareMC();
    //g1.RoyFloyd();
    //g1.Darb_infoarena();
    //g1.Dijkstra_infoarena();
    //g1.BF_infoarena();
    //g1.Disjoint_infoarena();
    //g1.Apm_infoarena();
    return 0;

}


