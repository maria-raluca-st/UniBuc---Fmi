#include <bits/stdc++.h>

using namespace std;

int n;

class NrComplex
{
    double re,im;
public:
    NrComplex();
    NrComplex(NrComplex &z);
    NrComplex(double re, double im);
    ~NrComplex();

    void set(double re, double im);
    void setRe(double re);
    void setIm(double im);

    //getter
    double getRe();
    double getIm();


    //modulul
    double calcModul();

    //adunare
    NrComplex operator+(NrComplex);
    //inmultire
    NrComplex operator*(NrComplex);
    //impartire
    NrComplex operator/(NrComplex);


    friend std::ostream& operator<<(std::ostream& os,NrComplex &z);
    friend std::istream& operator>>(std::istream& is,NrComplex &z);
    friend bool sortaremodule(NrComplex &a, NrComplex &b);


    friend class Vector_Complex;
};

class Vector_Complex
{
    int nrelem;
    NrComplex v[1000];
public:
    Vector_Complex();
    Vector_Complex(NrComplex &z, int nrelem);
    Vector_Complex(Vector_Complex &vec);
    ~Vector_Complex();

    friend std::istream& operator>>(std::istream& is, Vector_Complex &vec);
    friend std::ostream& operator<<(std::ostream& os, Vector_Complex &vec);


    void sumaelemente();
    void sortaremodul();
    void vectormodule();

};

NrComplex a,s;
NrComplex copiev[1000];
float Module[1000];

Vector_Complex::Vector_Complex(NrComplex &z, int nrelem)
{
    this->nrelem=nrelem;
    for(int i=1; i<=nrelem; i++)
    {
        this->v[i]=z;
        //cout<<v[i];
    }
};

Vector_Complex::Vector_Complex()
{
    this->nrelem=0;
};

Vector_Complex::Vector_Complex(Vector_Complex &vec)
{
    this->nrelem=vec.nrelem;
    for(int i=1; i<=nrelem; i++)
        this->v[i]=vec.v[i];
};

Vector_Complex::~Vector_Complex() {};


NrComplex::NrComplex()
{
    this->re = 0;
    this->im = 0;
};

NrComplex::NrComplex(double re, double im)
{
    this->re = re;
    this->im = im;
};

//constructor de copiere
NrComplex::NrComplex(NrComplex& r)
{
    this->re = r.re;
    this->im = r.im;
}
//destructor
NrComplex::~NrComplex() {};

double NrComplex::getRe()
{
    return this->re ;
}

double NrComplex::getIm()
{
    return this->im ;
}

void NrComplex::set(double re, double im)
{
    this->re = re;
    this->im = im;
}

void NrComplex::setRe(double re)
{
    this->re = re;
}

void NrComplex::setIm(double im)
{
    this->im = im;
}

double NrComplex::calcModul()
{
    double m;
    m = this->re*this->re + this->im*this->im;
    m=sqrt(m);
    return m;
}

NrComplex NrComplex::operator+(NrComplex op2)
{

    NrComplex tmp;
    tmp.re = this->re + op2.re;
    tmp.im = this->im + op2.im;

    //a + b

    return tmp;
}

NrComplex NrComplex::operator*(NrComplex op2)
{
    NrComplex tmp;
    tmp.re = this->re * op2.re - this->im * op2.im;
    tmp.im = this->re * op2.im + this->im * op2.re;
    return tmp;
}

NrComplex NrComplex::operator/(NrComplex op2)
{
    NrComplex tmp;
    double op2modul = op2.re * op2.re + op2.im* op2.im;
    tmp.re = (this->re * op2.re + this->im *op2.im)/op2modul;
    tmp.im = (this->re * op2.im - this->im *op2.re)/op2modul;
    return tmp;
}

std::ostream& operator<<(std::ostream& os, NrComplex& z)
{
    if(!z.getIm()) //z.getIm() == 0
        return os << z.getRe();

    //z.getIm() != 0

    if(z.getRe())
        os << z.getRe();

    if(z.getIm() >0)
        return os << '+' << z.getIm() << "*i";
    else
        return os << z.getIm() << "*i";

}

std::ostream& operator<<(std::ostream& os, Vector_Complex &vec)
{
    os<<vec.nrelem<<endl;
    for(int i=1; i<=vec.nrelem; i++)
        os<<vec.v[i]<<" ";
    return os;
}


std::istream& operator>>(std::istream& is, NrComplex& z)
{
    cout<<"Parte Reala: ";
    is>>z.re;
    cout<<"Parte Imaginara: ";
    is>>z.im;
    return is;
}

std::istream& operator>>(std::istream& is, Vector_Complex& vec)
{
    cout<<"Numar elemente: ";
    is>>vec.nrelem;
    cout<<"Elemente: "<<endl;
    for(int i=1; i<=vec.nrelem; i++)
        is>>vec.v[i];
    return is;
}

void Vector_Complex::sumaelemente()
{
    NrComplex s;
    for(int i=1; i<=nrelem; i++)
        s = s + v[i];
    cout<<s;
}

void Vector_Complex::sortaremodul()
{
    for(int i=1; i<=nrelem; i++)
        for(int j=i+1; j<=nrelem; j++)
            if(v[i].calcModul()>v[j].calcModul())
            {
                NrComplex temp;
                temp=v[j];
                v[j]=v[i];
                v[i]=temp;
            }

    cout<<"Sortare efectuata!";
}

void Vector_Complex::vectormodule()
{
    for(int i=1; i<=nrelem; i++)
    {
        Module[i]=v[i].calcModul();
        cout<<Module[i]<<" ";
    }
}

int main()
{
    Vector_Complex V;
    cin>>V;
    int meniu=1;
    while(meniu!=0)
    {
        cout<<endl;
        cout<<"MENIU APLICATIE"<<endl;
        cout<<"1. Afisare vector module"<<endl;
        cout<<"2. Vector sortat crescator dupa modulul elementelor"<<endl;
        cout<<"3. Suma elementelor vectorului"<<endl;
        cout<<"4. Afisare vector"<<endl;
        cout<<"0. Iesire"<<endl;
        cin>>meniu;
        if(meniu==1)
        {
            V.vectormodule();
        }
        else if(meniu==2)
        {
            V.sortaremodul();
        }
        else if(meniu==3)
        {
            V.sumaelemente();
        }
        else if(meniu==4)
        {
            cout<<V;
        }
        cout<<endl<<endl<<endl;
    }
    return 0;
}
