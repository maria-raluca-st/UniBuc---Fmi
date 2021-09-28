#include <bits/stdc++.h>
#include <chrono>



using namespace std;
using namespace std::chrono;


ifstream in ("test.in");
ofstream out ("test.out");

void afisarevector(unsigned long long v[],unsigned long long n)
{
    unsigned long long i;
    for (i=1; i<=n; i++)
    {
        cout<<v[i]<<" ";
    }
}


void mergevector(unsigned long long v[],unsigned long long left,unsigned long long middle,unsigned long long right)
{
    unsigned long long i,j,k=left;
    unsigned long long n1 = middle - left + 1,n2 = right - middle;
    unsigned long long L[n1+5], R[n2+5];

    for (i = 1; i <=n1; i++)
        L[i] = v[left + i-1];
    for (j = 1; j <= n2; j++)
        R[j] =v[middle + j];

    i = 1;
    j = 1;


    while (i <= n1 && j <= n2)
    {
        if (L[i] <= R[j])
        {
            v[k] = L[i];
            i++;
        }
        else
        {
            v[k] = R[j];
            j++;
        }
        k++;
    }
    while (i <= n1)
    {
        v[k] = L[i];
        i++;
        k++;
    }

    while (j <= n2)
    {
        v[k] = R[j];
        j++;
        k++;
    }
}

void MergeSort(unsigned long long v[],unsigned long long left,unsigned long long right)
{
    /*if(left>=right)
        return;*/

    if(left<right)
    {
        long long middle =(left+right)/2;
        MergeSort(v,left,middle);
        MergeSort(v,middle+1,right);
        mergevector(v,left,middle,right);
    }
}

void BubbleSort(unsigned long long v[],unsigned long long n)
{
    unsigned long long i, j, a;
    bool ok=0;
    for (i=1; i<n; i++)
    {
        ok=0;
        for(j=1; j<=n-i; j++)
        {
            if (v[j] > v[j+1])
            {

                a=v[j];
                v[j]=v[j+1];
                v[j+1]=a;

                ok=1;
            }
        }

        if (ok==0)
            break;
    }
    //afisarevector(v,n);
    //afisare separat cu afisare vector
}
unsigned long long ct[100000000],output[100000000];
void CountSort(unsigned long long v[],unsigned long long n,unsigned long long maxi)
{
    unsigned long long i,j;

    for(i=1; i<=n; i++)
        ct[v[i]]++;

    for (i=0, j=1; i<=maxi; i++) {
    while(ct[i]>0)
    {
      v[j] = i;
      j++;
      ct[i]--;
       }
     }

    /*for(i=0; i<=maxi; i++)
        for(long long j=0; j<=ct[i]; j++)
            { v[contor]=i;
              contor++;
            }*/

    /*for(i=n;i>=1;i--)
    {
        output[ct[v[i]]] = v[i];
        ct[v[i]]--;
    }
    for(i=1;i<=n;i++)
    {
        v[i]=output[i];
    }*/


    //nu mai trb folosita functia afisarevector.

}

void InsertionSort(unsigned long long v[],unsigned long long n)
{
    unsigned long long key,i,j;
    for(i=2; i<=n; i++)
    {
        key=v[i];
        j=i-1;
        while(j>=1 && v[j]>key)
        {
            v[j+1]=v[j];
            j--;
        }
        v[j+1]=key;
    }
    //afisare separat cu afisarevector
}

void QuickSort(unsigned long long v[],unsigned long long left,unsigned long long right)
{
    unsigned long long i = left, j = right;
    unsigned long long mid = v[(left + right) / 2];

    while (i <= j)
    {
        while (v[i] < mid)
            i++;
        while (v[j] > mid)
            j--;
        if (i <= j)
        {
            swap(v[i], v[j]);
            i++;
            j--;
        }
    }
    if (left < j)
        QuickSort(v, left, j);
    if (i < right)
        QuickSort(v, i, right);
}

int test_sort(unsigned long long v[],unsigned long long n)
{
    unsigned long long i;
    bool ok=1;
    for(i=1; i<n; i++)
    {
        if(v[i]>v[i+1])
        {
            ok=0;
            break;
        }
    }
    return ok;
}

int main()
{
    unsigned long long nrteste,k,n,nrmax,i;
    in>>nrteste;
    for(k=1; k<=nrteste; k++)
    {
        in>>n>>nrmax;
        unsigned long long vrand[4*n],copvrand[4*n];//vector generat random+ copia sa
        for(i=1; i<=n; i++)
        {
            vrand[i]=(rand()%32000)*nrmax/32000+1;//umplem vectorul cu nr generat aleatoriu mai mici decat nrmax
            copvrand[i]=vrand[i];

        }
        /*for(i=1;i<=n;i++)
        {  if(i<=3*n/4)
            {
                vrand[i]=i;
                copvrand[i]=i;

            }
            else
            {
                vrand[i]=(rand()%32000)*nrmax/32000+1;//umplem vectorul cu nr generat aleatoriu mai mici decat nrmax
                copvrand[i]=vrand[i];
            }
        }*/
        auto start = high_resolution_clock::now();
        BubbleSort(copvrand,n);
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        if(test_sort(copvrand,n)==1 && n<=100000)
            out << "Time taken by Bubble Sort cu: "<<n<<" numere si maxim "<<nrmax<<" este: "<< duration.count() << " microseconds" << endl;
        else
            out<<"Sort failed!"<<endl;


        for(i=1; i<=n; i++)
            copvrand[i]=vrand[i];

        start = high_resolution_clock::now();
        CountSort(copvrand,n,nrmax);
        stop = high_resolution_clock::now();
        duration = duration_cast<microseconds>(stop - start);
        if(test_sort(copvrand,n)==1 && n<=100000 && nrmax<1000000)
            out << "Time taken by Count Sort cu : "<<n<<" numere si maxim "<<nrmax<<" este: "<< duration.count() << " microseconds" << endl;
        else
            out<<"Sort failed!"<<endl;

        for(i=1; i<=n; i++)
            copvrand[i]=vrand[i];

        start = high_resolution_clock::now();
        InsertionSort(copvrand,n);
        stop = high_resolution_clock::now();
        duration = duration_cast<microseconds>(stop - start);
        if(test_sort(copvrand,n)==1 && n<=100000)
            out << "Time taken by Insertion Sort cu: "<<n<<" numere si maxim "<<nrmax<<" este: "<< duration.count() << " microseconds" << endl;
        else
            out<<"Sort failed!"<<endl;

        for(i=1; i<=n; i++)
            copvrand[i]=vrand[i];

        start = high_resolution_clock::now();
        QuickSort(copvrand,1,n);
        stop = high_resolution_clock::now();
        duration = duration_cast<microseconds>(stop - start);
        if(test_sort(copvrand,n)==1 && n<=100000)
            out << "Time taken by Quick Sort cu: "<<n<<" numere si maxim "<<nrmax<<" este: "<< duration.count() << " microseconds" << endl;
        else
            out<<"Sort failed!"<<endl;

        for(i=1; i<=n; i++)
            copvrand[i]=vrand[i];

        start = high_resolution_clock::now();
        MergeSort(copvrand,1,n);
        stop = high_resolution_clock::now();
        duration = duration_cast<microseconds>(stop - start);
        if(test_sort(copvrand,n)==1 && n<=100000)
            out << "Time taken by Merge Sort cu: "<<n<<" numere si maxim "<<nrmax<<" este: "<< duration.count() << " microseconds" << endl;
        else
            out<<"Sort failed!"<<endl;

        out<<endl;

        memset(vrand,0,n);
        memset(copvrand,0,n);

    }

    return 0;
}
