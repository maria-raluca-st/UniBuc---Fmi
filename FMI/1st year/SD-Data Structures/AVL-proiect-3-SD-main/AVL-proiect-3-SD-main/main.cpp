#include<bits/stdc++.h>
using namespace std;


struct Node
{
    //public:
    int key;
    Node *left;
    Node *right;
    int height;
};

///FUNCTIE PT INALTIMEA ARBORELUI
int height(Node *N)
{
    if (N == NULL)
        return 0;
    return N->height;
}


///functie de nod nou
Node* newNode(int key)
{
    Node* node = new Node();
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;

    return node;
}
///functie pt rotatie dreapta a subarborelui cu radacina in y care returneaza noua radacina
Node *rightRotate(Node *y)
{
    Node *x = y->left;
    Node *T2 = x->right; ///T2 este subarborele drept cu radacina in x

    ///Rotatia propriu-zisa
    x->right = y;
    y->left = T2;

    ///Actualizam inaltimea nodurilor cu formula: inaltimea este maximul inaltimilor fiilor +1
    x->height = max(height(x->left),height(x->right)) + 1;
    y->height = max(height(y->left),height(y->right)) + 1;


    ///x devine tatal lui y
    return x;
}

///functie pt rotatie stanga a subarborelui cu radacina in x care returneaza noua radacina(basically inversa functiei anterioare)
Node *leftRotate(Node *x)
{
    Node *y = x->right;
    Node *T2 = y->left; ///T2 este subarborele stang cu radacina in y

    ///Rotatia propriu-zisa
    y->left = x;
    x->right = T2;

    ///Actualizam inaltimea nodurilor cu formula: inaltimea este maximul inaltimilor fiilor +1
    x->height = max(height(x->left),height(x->right)) + 1;
    y->height = max(height(y->left),height(y->right)) + 1;

    ///y devine tatal lui x
    return y;
}

///Aflam factorul de echilibru(balance factor) al nodului N
int BF(Node *N)
{
    if (N == NULL)
        return 0;

    return height(N->left) - height(N->right);
}


///Functie recursiva de inserare in subarborele cu radacina in node , care returneaza noua radacina
Node* insertion(Node* node, int key1)
{
    if (node == NULL)
        return (newNode(key1));

    ///Daca cheia pe care vrem sa o inseram este mai mica decat cea anterioara o inseram in stanga
    if (key1 < node->key)
        node->left = insertion(node->left, key1);

    ///Altfel o inseram in dreapta
    else if (key1 > node->key)
        node->right = insertion(node->right, key1);

    ///Nu putem insera chei egale
    else
        return node;

    ///Actualizam inaltimea nodului
    node->height = max(height(node->left),height(node->right))+1;


    ///Aflam BF(balance factor) pt nodul tata ca sa vedem daca arborele a ramas sau nu balanced
    int balance = BF(node);

    ///Rotatiile(in caz ca nu a ramas balanced)

    ///Stanga Stanga
    if (balance > 1 && key1 < node->left->key)
        return rightRotate(node);

    ///Dreapta Dreapta
    if (balance < -1 && key1 > node->right->key)
        return leftRotate(node);

    ///Stanga Dreapta
    if (balance > 1 && key1 > node->left->key)
    {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    ///Dreapta Stanga
    if (balance < -1 && key1 < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

Node * minValueNode(Node* node)
{
    Node* current = node;

    ///mergem cat de mult in stanga putem ca sa aflam val. minima din arbore
    while (current->left != NULL)
        current = current->left;

    return current;
}


void findPreSuc(Node* root, Node*& pre, Node*& suc, int key2)
{

    if (root == NULL)
        return ;

    ///Daca cheia este in radacina
    if (root->key == key2)
    {
        ///Valoarea maxima din subarborele stang este predecesorul cautat
        if (root->left != NULL)
        {
            Node* tmp = root->left;
            while (tmp->right)
                tmp = tmp->right;
            pre = tmp ;
        }

        ///Valoarea minima din subarborele drept este succesorul cautat
        if (root->right != NULL)
        {
            Node* tmp = root->right ;
            while (tmp->left)
                tmp = tmp->left ;
            suc = tmp ;
        }
        return ;
    }

    ///Daca cheia nu este radacina si este mai mica, ne ducem in subarborele stang
    if (key2 < root->key)
    {
        suc = root ;
        findPreSuc(root->left, pre, suc, key2) ;
    }
    ///Altfel ne ducem in subarborele drept
    else
    {
        pre = root ;
        findPreSuc(root->right, pre, suc, key2) ;
    }
}

bool ok=0;
bool cautare(Node* root, int key3)
{

    if(root!=NULL)
    {   ///Daca gasim key in radacina am terminat
        if (root->key == key3)
           ok=1;
        ///Daca e mai mare , cautam in dreapta , altfel in stanga
        else if (root->key < key3)
           cautare(root->right, key3);
        else
           cautare(root->left, key3);

    }
    return ok;
}


///Functie recursiva de stergere a unui nod care returneaza radacina subarborelui modificat
Node* deleteNode(Node* root,int key4)
{

    if (root == NULL)
        return root;

    ///Daca cheia pe care vrem s o stergem e mai mica decat cheia din tata, atunci se afla in subarborele stang
    if ( key4 < root->key )
        root->left = deleteNode(root->left, key4);

    ///Altfel o cautam in subarborele drept
    else if( key4 > root->key )
        root->right = deleteNode(root->right, key4);

    ///Altfel am gasit o si este nodul pe care vrem sa l stergem
    else
    {
        /// nod cu maxim un fiu
        if( (root->left == NULL) || (root->right == NULL) )
        {

             Node *temp; ///fiul
             if(root->left == NULL)
               temp = root->right;
             else if (root->right == NULL)
               temp = root->right;

            /// daca este frunza(nodul pe care trb sa l stergem)
            if (temp == NULL)
            {
                temp = root;
                root = NULL;
            }
            else
            *root = *temp; ///Copiem fiul

        }
        ///altfel nodul are 2 fii
        else
        {

            /// Ii gasim succesorul din subarborele drept
            Node* temp = minValueNode(root->right);

            ///Copiem cheia din succesor in nodul cu cheia pe care vrem s o stergem
            root->key = temp->key;

            ///Stergem succesorul
            root->right = deleteNode(root->right,temp->key);
        }
    }


    if (root == NULL)
       return root;

    ///Actualizam inaltimea nodului
    root->height = max(height(root->left),height(root->right)) + 1;

    ///Aflam BF ca sa determinam daca nodul este sau nu balanced
    int balance = BF(root);

    ///Daca nu este balanced ne aflam in unul din cele 4 cazuri

    /// Stanga Stanga
    if (balance > 1 && BF(root->left) >= 0)
        return rightRotate(root);

    ///Stanga Dreapta
    if (balance > 1 && BF(root->left) < 0)
    {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    ///Dreapta Dreapta
    if (balance < -1 && BF(root->right) <= 0)
        return leftRotate(root);

    /// Dreapta Stanga
    if (balance < -1 && BF(root->right) > 0)
    {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}
///Afisarea elementelor in ordine crescatoare - SRD
void InOrder(Node *root)
{
    if(root!=NULL)
    {
        InOrder(root->left);
        cout << root->key << " ";
        InOrder(root->right);
    }
}


int main()
{
    Node *root = NULL,* pre = NULL, *suc = NULL;
    int n,x,ok2=1;
    while(ok2 == 1)
    {   cout<<"Meniu"<<endl;
        cout<<"1.Inserare in AVL"<<endl;
        cout<<"2.Stergere nod cu valoarea x din AVL"<<endl;
        cout<<"3.Cautare x in AVL"<<endl;
        cout<<"4.Cautarea predecesorului si a succesorului valorii x din AVL"<<endl;
        cout<<"5.Afisarea elementelor din AVL in ordine crescatoare"<<endl;
        cout<<"6.Iesire din meniu"<<endl;
        cout<<"Raspuns : ";
        int a;
        cin>>a;
        if(a == 1)
        {
            cout<<"Care este valoarea lui x?"<<endl<<"Raspuns : ";
            cin>>x;
            root=insertion(root,x);

        }
        if(a == 2)
        {
           cout<<"Care este valoarea lui x?"<<endl<<"Raspuns : ";
           cin>>x;
           root = deleteNode(root, x);
        }
        if(a == 3)
        {
            cout<<"Care este valoarea lui x?"<<endl<<"Raspuns : ";
            cin>>x;
            ok=0;
            if(cautare(root,x) == 1)
            cout<<"Element gasit in AVL!"<<endl;
            else cout<<"Elementul nu este in AVL"<<endl;

        }
        if(a == 4)
        {
            cout<<"Care este valoarea lui x?"<<endl<<"Raspuns : ";
            cin>>x;
            findPreSuc(root, pre,suc, x);
            cout<<"Predecesorul este "<<pre->key<<" si succesorul este "<<suc->key<<'\n';
            pre = NULL;
            suc = NULL;

        }
        if(a == 5)
        {
            cout<<"Elementele din AVL sunt : ";
            InOrder(root);
            cout<<endl;
        }
        if(a==6)
        {
            cout<<"O zi buna!"<<endl;
            ok2=0;
        }
    }

    return 0;
}
