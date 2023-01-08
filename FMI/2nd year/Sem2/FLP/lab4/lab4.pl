%zebra puzzle
% avem 5 case cu 5 atribute fiecare
% numarul casei de la 1 la 5
% nationalitatea celui care locuieste in casa
% animalul de companie
% bautura preferata
% ce tigari fumeaza

% trb sa det ce nationalitate are posesorul zebrei, stiind un set de constrangeri
% avem

% casa(Numar, Nationalitate, Culoare, Animal, Bautura, Tigari).

la_dreapta(X, Y) :- X is Y+1.
la_stanga(X, Y) :- la_dreapta(Y, X).
langa(X, Y) :- la_dreapta(X, Y);la_stanga(X, Y).

%  nu merge ffs
solutie(Strada, PosesorZebra) :-
    Strada = [
        casa(1,_,_,_,_,_),
        casa(2,_,_,_,_,_),
        casa(3,_,_,_,_,_),
        casa(4,_,_,_,_,_),
        casa(5,_,_,_,_,_)
    ],
    member(casa(_, englez, rosie, _, _, _), Strada),
    member(casa(_, spaniol, _, caine, _, _), Strada),
    member(casa(_, _, verde, _, cafea, _), Strada),
    member(casa(_, ucrainean, _, _, ceai, _), Strada),
    member(casa(_, _, _, melci, _, old_gold), Strada),
    member(casa(C, norvegian, _, _, _, _), Strada),
    member(casa(D, _, albasta, _, _, _), Strada),
    langa(C, D),
    member(casa(_, _, galbena, _, _, kools), Strada),
    member(casa(3, _, _, _, lapte, _), Strada),
    member(casa(1, norvegian, _, _, _, _), Strada),
    member(casa(E, _, _, _, _, chesterfield), Strada),
    member(casa(F, _, _, _, _, _), Strada),
    langa(E, F),
    member(casa(G, _, _, _, _, kools), Strada),
    member(casa(H, _, _, cal, _, _), Strada),
    langa(G, H),
    member(casa(_, _, _, _, suc_portocale, lucky_strike), Strada),
    member(casa(_, japonez, _, _, _, parliaments), Strada),
    member(casa(A, _, verde, _, _, _), Strada),
    member(casa(B, _, bej, _, _, _), Strada),
    la_dreapta(A, B),
    member(casa(_, PosesorZebra, _, zebra, _, _), Strada).

% bogdan.macovei.fmi@gmail.com

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%  countdown
% fiind data o lista de litere, sa se gaseasca cel mai lung cuvant din limba engleza care se poate forma folosind toate (sau o parte) dintre aceste litere

% word/1 cuvintele din limba engleza
word(hello).
word(something).

:- include('words.pl').

% atom_chars/2
% atom_chars(Word, Letters) lista de litere a cuvantului Word in Letters
% atom_chars(hello, X).
% X = [h, e, l, l, o].

% select/3
% select(+Elem, +List, -ListR)
% elimina prima aparitie a lui Elem in List
% si intoarce rezultatul in ListR
% select(8, [1,3,8,5,8,9], LR).
% LR = [1,3,5,8,9].

% prima sol ar fi sa generam toate cuv posibile utilizand lista de litere primita

% alta varianta, verificam daca o lista de litere acopera o alta lista de litere

% cover([b,a,e,s,c], [c,a,b,l,e,s])
% [b | [a,e,s,c]] [c,a,b,l,e,s] => [c,a,l,e,s]
% [a,e,s,c] [c,a,l,e,s]

% returneaza true daca prima lista poate acoperi a doua lista
cover([], _).
cover([H|T], L) :-
    select(H, L, R),
    cover(T, R).

% Score = lungime
solution(ListLetters, Word, Score) :-
    word(Word),
    atom_chars(Word, Letters),
    length(Letters, Score),
    cover(Letters, ListLetters).

search_solution(_, 'no solution', 0).
search_solution(ListLetters, Word, X) :-
    solution(ListLetters, Word, X).
search_solution(ListLetters, Word, X) :-
    Y is X - 1,
    search_solution(ListLetters, Word, Y).

topsolution(ListLetters, Word) :-
    length(ListLetters, Score),
    search_solution(ListLetters, Word, Score).