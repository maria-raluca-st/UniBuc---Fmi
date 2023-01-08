female(mary).
female(sandra).
female(juliet).
female(lisa).
male(peter).
male(paul).
male(dony).
male(bob).
male(harry).
male(petru).
parent(bob, lisa).
parent(bob, paul).
parent(bob, mary).
parent(juliet, lisa).
parent(juliet, paul).
parent(juliet, mary).
parent(peter, harry).
parent(lisa, harry).
parent(mary, dony).
parent(mary, sandra).

father_of(Father, Child) :- male(Father), parent(Father, Child).
mother_of(Mother, Child) :- female(Mother), parent(Mother, Child).

grandfather_of(Grandfather, Child) :- male(Grandfather), father_of(Grandfather, Father), father_of(Father, Child);
                                    male(Grandfather), father_of(Grandfather, Mother), mother_of(Mother, Child).

grandmother_of(Grandmother, Child) :- female(Grandmother), mother_of(Grandmother, Father), father_of(Father, Child);
                                    female(Grandmother), mother_of(Grandmother, Mother), mother_of(Mother, Child).

sister_of(Sister,Person) :- female(Sister), parent(P, Sister), parent(P, Person).

brother_of(Brother,Person) :- male(Brother), parent(P, Brother), parent(P, Person).

aunt_of(Aunt,Person) :- female(Aunt), sister_of(Aunt, Person2), parent(Person2, Person).

uncle_of(Uncle,Person) :- male(Uncle), brother_of(Uncle, Person2), parent(Person2, Person).


not_parent(X,Y) :- (male(X); female(X)), (male(Y); female(Y)), not(parent(X,Y)).

distance((X1, Y1), (X2, Y2), X) :- X is sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2).