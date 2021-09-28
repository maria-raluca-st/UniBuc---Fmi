#include <bits/stdc++.h>

using namespace std;



class Persoana
{
    static int nrpers;
    int id;
    string nume;
 public:
    Persoana();
    Persoana(int);
    Persoana(string);
    Persoana(int,string);
    Persoana(const Persoana&);
    ~Persoana();
    Persoana& operator= (Persoana&);
    virtual void afisare();
    static int afisarenumarpersoane()
    {
        return nrpers;
    };
    virtual string afisnume(){return nume;};

    friend istream& operator>>(istream &, Persoana&);
    friend ostream& operator<<(ostream &, Persoana&);
};

istream& operator>>(istream& in, Persoana& ob)
{
    in>>ob.id>>ob.nume;
    return in;
}

ostream& operator<<(ostream& out, Persoana& ob)
{
    out<<ob.id<<ob.nume;
    return out;
}


class Abonat: public Persoana
{
    static int nrabonati;
    string nr_telefon;
public:
    Abonat();
    Abonat(string);
    Abonat (const Abonat&);
    ~Abonat();
    Abonat& operator= (Abonat&);
    virtual void afisare();
    friend istream& operator>>(istream&, Abonat&);
    friend ostream& operator<<(ostream&, Abonat&);
};

istream& operator>> (istream &in, Abonat &ob)
{
    in>>ob.nr_telefon;
    return in;
}
ostream& operator<< (ostream &out, Abonat &ob)
{
    out<<ob.nr_telefon;
    return out;
}



class Abonat_Skype: public Abonat
{

    string id_skype;
public:
    Abonat_Skype();
    Abonat_Skype(string);
    Abonat_Skype (const Abonat_Skype&);
    ~Abonat_Skype();
    Abonat_Skype& operator= (Abonat_Skype&);
    virtual void afisare();
    friend istream& operator>>(istream&, Abonat_Skype&);
    friend ostream& operator<<(ostream&, Abonat_Skype&);
};

istream& operator>> (istream &in, Abonat_Skype &ob)
{
    in>>ob.id_skype;
    return in;
}

ostream& operator<< (ostream &out, Abonat_Skype &ob)
{
    out<<ob.id_skype;
    return out;
}

class Abonat_Skype_Romania: public Abonat_Skype
{

    string adresa_mail;
public:
    Abonat_Skype_Romania();
    Abonat_Skype_Romania(string);
    Abonat_Skype_Romania(const Abonat_Skype_Romania&);
    ~Abonat_Skype_Romania();
    Abonat_Skype_Romania& operator= (Abonat_Skype_Romania&);
    virtual void afisare();
    friend istream& operator>>(istream&, Abonat_Skype_Romania&);
    friend ostream& operator<<(ostream&, Abonat_Skype_Romania&);
};

istream& operator>> (istream &in, Abonat_Skype_Romania &ob)
{
    in>>ob.adresa_mail;
    return in;
}
ostream& operator<< (ostream &out, Abonat_Skype_Romania &ob)
{
    out<<ob.adresa_mail;
    return out;
}

class Abonat_Skype_Extern: public Abonat_Skype
{

    string tara;
public:
    Abonat_Skype_Extern();
    Abonat_Skype_Extern(string);
    Abonat_Skype_Extern (const Abonat_Skype_Extern&);
    ~Abonat_Skype_Extern();
    Abonat_Skype_Extern& operator= (Abonat_Skype_Extern&);
    virtual void afisare();
    friend istream& operator>>(istream&, Abonat_Skype_Extern&);
    friend ostream& operator<<(ostream&, Abonat_Skype_Extern&);
};

istream& operator>> (istream &in, Abonat_Skype_Extern &ob)
{
    in>>ob.tara;
    return in;
}
ostream& operator<< (ostream &out, Abonat_Skype_Extern &ob)
{
    out<<ob.tara;
    return out;
}
class Agenda: public Persoana
{
    vector<Persoana*>Contacte_Persoana;
    vector<Abonat*>Contacte_Abonat;
    vector<Abonat_Skype*>Contacte_Abonat_Skype;
    vector<Abonat_Skype*>Contacte_Abonat_Skype_Tip;

public:
    Agenda() {};
    Agenda(int);
    Agenda (const Agenda&);
    ~Agenda() {};
    Agenda& operator=(Agenda&);
    friend istream& operator>>(istream&, Agenda&);
    friend ostream& operator<<(ostream&, Agenda&);
    void Add_Persoana(Agenda &a);
    void Afisare_Persoana(int);
    void Add_Abonat(Agenda &a);
    void Afisare_Abonat(int);
    void Add_Abonat_Skype(Agenda &a);
    void Afisare_Abonat_Skype(int);
    void Add_Abonat_Skype_Romania(Agenda &a);
    void Afisare_Abonat_Skype_Romania(int);
    void Add_Abonat_Skype_Extern(Agenda &a);
    void Afisare_Abonat_Skype_Extern(int);
    Persoana*& operator[](string);
};

Agenda a;

int Persoana::nrpers;

void Agenda::Add_Persoana(Agenda &a)
{
    int id_p;
    string nume_p;
    cin>>id_p>>nume_p;
    Persoana *p = new Persoana(id_p,nume_p);
    a.Contacte_Persoana.push_back(p);
}

void Agenda::Afisare_Persoana(int x)
{
    Contacte_Persoana[x]->afisare();
}

void Agenda::Add_Abonat(Agenda &a)
{
    string s;
    cin>>s;
    Abonat *p = new Abonat(s);
    a.Contacte_Abonat.push_back(p);
}

void Agenda::Afisare_Abonat(int x)
{
    Contacte_Abonat[x]->afisare();
}

void Agenda::Add_Abonat_Skype(Agenda &a)
{
    string s;
    cin>>s;
    Abonat_Skype *p = new Abonat_Skype(s);
    a.Contacte_Abonat_Skype.push_back(p);
}

void Agenda::Afisare_Abonat_Skype(int x)
{
    Contacte_Abonat_Skype[x]->afisare();
}

void Agenda::Add_Abonat_Skype_Romania(Agenda &a)
{
    string s;
    cin>>s;
    Abonat_Skype *p = new Abonat_Skype_Romania(s);
    a.Contacte_Abonat_Skype_Tip.push_back(p);
}

void Agenda::Afisare_Abonat_Skype_Romania(int x)
{
    Contacte_Abonat_Skype_Tip[x]->afisare();
}

void Agenda::Add_Abonat_Skype_Extern(Agenda &a)
{
    string s;
    cin>>s;
    Abonat_Skype *p = new Abonat_Skype_Extern(s);
    a.Contacte_Abonat_Skype_Tip.push_back(p);
}

void Agenda::Afisare_Abonat_Skype_Extern(int x)
{
    Contacte_Abonat_Skype_Tip[x]->afisare();
}
Agenda::Agenda(int x)
{
    int numar=x;
}

Agenda::Agenda(const Agenda& ob)
{
    Contacte_Abonat=ob.Contacte_Abonat;
    Contacte_Abonat_Skype=ob.Contacte_Abonat_Skype;
    Contacte_Abonat_Skype_Tip=ob.Contacte_Abonat_Skype_Tip;
    Contacte_Persoana=ob.Contacte_Persoana;
}

Agenda& Agenda::operator= (Agenda& ob)
{
    if (this != &ob)
    {
        Contacte_Abonat=ob.Contacte_Abonat;
        Contacte_Abonat_Skype=ob.Contacte_Abonat_Skype;
        Contacte_Abonat_Skype_Tip=ob.Contacte_Abonat_Skype_Tip;
        Contacte_Persoana=ob.Contacte_Persoana;
    }
    return *this;
}

istream& operator>>(istream& in, Agenda& ob)
{
    int nr;
    cout<<"Cititi numarul de abonati : ";
    cin>>nr;
    for(int i=1; i<=nr; i++)
    {
        cout<<"Abonatul "<<i<<": "<<endl;
        cout<<"Persoana (id, nume): ";
        a.Agenda::Add_Persoana(a);
        cout<<"Abonat (Numar Telefon): ";
        a.Agenda::Add_Abonat(a);
        cout<<"Abonat Skype (ID Skype): ";
        a.Agenda::Add_Abonat_Skype(a);
        cout<<"Tipul abonatului?"<<endl;
        cout<<"1. Romania"<<endl;
        cout<<"2. Extern"<<endl;
        cout<<"Selectati tipul:"<<endl;
        int alegere;
        cin>>alegere;
        if(alegere==1)
        {
            cout<<"Introduceti adresa de mail a abonatului din Romania :";
            a.Agenda::Add_Abonat_Skype_Romania(a);
        }
        else if(alegere==2)
        {
            cout<<"Introduceti tara abonatului Skype : ";
            a.Agenda::Add_Abonat_Skype_Extern(a);
        }
        else
        {
            cout<<"Optiune invalida!";
        }
    }
}

ostream& operator<<(ostream& os, Agenda& ob)
{
    for(int i=0; i<ob.Contacte_Persoana.size(); i++)
            {
                cout<<"Abonatul "<<i+1<<": "<<endl;
                a.Agenda::Afisare_Persoana(i);
                a.Agenda::Afisare_Abonat(i);
                a.Agenda::Afisare_Abonat_Skype(i);
                a.Agenda::Afisare_Abonat_Skype_Romania(i);
            }
}




Persoana::Persoana()
{
    id=0;
    nume="necunoscut";
    nrpers++;
}

Persoana::Persoana(int x)
{
    id=x;
    nume="necunoscut";
    nrpers++;
}

Persoana::Persoana(string s)
{
    id=0;
    nume=s;
    nrpers++;
}

Persoana::Persoana(int x, string s)
{
    id=x;
    nume=s;
    nrpers++;
}

Persoana::Persoana(const Persoana& ob)
{
    id=ob.id;
    nume=ob.nume;
    nrpers++;
}

Persoana::~Persoana() {}

Persoana& Persoana::operator= (Persoana& ob)
{
    if (this != &ob)
    {
        id = ob.id;
        nume = ob.nume;
    }
    return *this;
}

void Persoana::afisare()
{
    cout<<id<<" "<<nume<<endl;
}



Abonat::Abonat()
{
    nr_telefon="necunoscut";

}

Abonat::Abonat(string s)
{
    nr_telefon=s;

}

Abonat::Abonat(const Abonat&ob)
{
    nr_telefon=ob.nr_telefon;

}

Abonat::~Abonat() {}

Abonat& Abonat::operator=(Abonat &ob)
{
    if (this != &ob)
    {
        nr_telefon=ob.nr_telefon;
    }
    return *this;
}

void Abonat::afisare()
{
    cout<<nr_telefon<<endl;
}




Abonat_Skype::Abonat_Skype()
{
    id_skype="necunoscut";

}

Abonat_Skype::Abonat_Skype(string s)
{
    id_skype=s;

}

Abonat_Skype::Abonat_Skype(const Abonat_Skype &ob)
{
    id_skype=ob.id_skype;


}

Abonat_Skype::~Abonat_Skype() {}

Abonat_Skype& Abonat_Skype::operator=(Abonat_Skype &ob)
{
    if (this != &ob)
    {
        id_skype=ob.id_skype;
    }
    return *this;
}

void Abonat_Skype::afisare()
{
    cout<<id_skype<<endl;
}



Abonat_Skype_Romania::Abonat_Skype_Romania()
{
    adresa_mail="necunoscut";

}

Abonat_Skype_Romania::Abonat_Skype_Romania(string s)
{
    adresa_mail=s;

}

Abonat_Skype_Romania::Abonat_Skype_Romania(const Abonat_Skype_Romania &ob)
{
    adresa_mail=ob.adresa_mail;

}

Abonat_Skype_Romania::~Abonat_Skype_Romania() {}


Abonat_Skype_Romania& Abonat_Skype_Romania::operator=(Abonat_Skype_Romania &ob)
{
    if (this != &ob)
    {
        adresa_mail=ob.adresa_mail;
    }
    return *this;
}

void Abonat_Skype_Romania::afisare()
{
    cout<<adresa_mail<<endl;
}


Abonat_Skype_Extern::Abonat_Skype_Extern()
{
    tara="necunoscut";

}

Abonat_Skype_Extern::Abonat_Skype_Extern(string s)
{
    tara=s;

}

Abonat_Skype_Extern::Abonat_Skype_Extern(const Abonat_Skype_Extern &ob)
{
    tara=ob.tara;

}

Abonat_Skype_Extern::~Abonat_Skype_Extern() {}

Abonat_Skype_Extern& Abonat_Skype_Extern::operator=(Abonat_Skype_Extern &ob)
{
    if (this != &ob)
    {
        tara=ob.tara;
    }
    return *this;
}

void Abonat_Skype_Extern::afisare()
{
    cout<<tara<<endl;
}

Persoana*& Agenda:: operator[](string index)
    {
        int poz=-1;
        for(int i=0; i<Contacte_Persoana.size(); i++)
        {
            if(Contacte_Persoana[i]->afisnume() == index)
                poz=i;
        }
        if(poz == -1)
        {
            cout<<"Persoana nu este abonata."<<endl;
        }
        else
        {
            a.Agenda::Afisare_Persoana(poz);
            a.Agenda::Afisare_Abonat(poz);
            a.Agenda::Afisare_Abonat_Skype(poz);
            a.Agenda::Afisare_Abonat_Skype_Romania(poz);
        }
    };

void cautare_nume(string s)
{
    a[s];
}
int main()
{

    int n;
    cout<<"Cititi numarul de abonati:";
    cin>>n;
    for(int i=1; i<=n; i++)
    {
        cout<<"Abonatul "<<i<<": ";
        cout<<"Persoana (id, nume): ";
        a.Agenda::Add_Persoana(a);
        cout<<"Abonat (Numar Telefon): ";
        a.Agenda::Add_Abonat(a);
        cout<<"Abonat Skype (ID Skype): ";
        a.Agenda::Add_Abonat_Skype(a);
        cout<<"Tipul abonatului?"<<endl;
        cout<<"1. Romania"<<endl;
        cout<<"2. Extern"<<endl;
        cout<<"Selectati tipul:"<<endl;
        int alegere;
        cin>>alegere;
        if(alegere==1)
        {
            cout<<"Introduceti adresa de mail a abonatului Skype Romania : ";
            a.Agenda::Add_Abonat_Skype_Romania(a);
        }
        else if(alegere==2)
        {
            cout<<"Introduceti tara abonatului Skype : ";
            a.Agenda::Add_Abonat_Skype_Extern(a);
        }
        else
        {
                cout<<"Optiune invalida."<<endl;
                break;
        }
    }

    int ok=1,M;
    while(ok==1)
    {
        cout<<"Meniu: "<<endl;
        cout<<"1.Adaugare abonat"<<endl;
        cout<<"2.Afisare lista"<<endl;
        cout<<"3.Cautare dupa nume"<<endl;
        cout<<"4.Iesire"<<endl;
        cin>>M;
        if(M == 1)
        {
            cout<<"Abonatul nou"<<": ";
            cout<<"Persoana (id, nume): ";
            a.Agenda::Add_Persoana(a);
            cout<<"Abonat (Numar Telefon): ";
            a.Agenda::Add_Abonat(a);
            cout<<"Abonat Skype (ID Skype): ";
            a.Agenda::Add_Abonat_Skype(a);
            cout<<"Tipul abonatului?"<<endl;
            cout<<"1. Romania"<<endl;
            cout<<"2. Extern"<<endl;
            cout<<"Selectati tipul:"<<endl;
            int alegere;
            cin>>alegere;
            if(alegere==1)
            {
                cout<<"Introduceti adresa de mail a abonatului Skype Romania : ";
                a.Agenda::Add_Abonat_Skype_Romania(a);
            }

            else if(alegere==2)
            {
                cout<<"Introduceti tara abonatului Skype : ";
                a.Agenda::Add_Abonat_Skype_Extern(a);
            }
            else
            {
                cout<<"Optiune invalida."<<endl;
                break;
            }
            n++;
        }
        else if(M == 2)
        {
            for(int i=0; i<n; i++)
            {
                cout<<"Abonatul "<<i+1<<": "<<endl;
                a.Agenda::Afisare_Persoana(i);
                a.Agenda::Afisare_Abonat(i);
                a.Agenda::Afisare_Abonat_Skype(i);
                a.Agenda::Afisare_Abonat_Skype_Romania(i);
            }
        }
        else if(M == 3)
        {
            cout<<"Nume abonat: ";
            string nume_cautare;
            cin>>nume_cautare;
            cautare_nume(nume_cautare);
        }
        else if(M == 4)
        {
            ok=0;
        }
        else
        {
            cout<<"Comanda incorecta.Try again!"<<endl;
        }
    }

    return 0;
}
