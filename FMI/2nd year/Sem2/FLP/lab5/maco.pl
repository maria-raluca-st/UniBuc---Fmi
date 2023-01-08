% lab 5
% recapitulative
% numar_aparitii/3
% numar_aparitii(+List, +Elem, -NrApar).

numar_aparitii([], _, 0).
numar_aparitii([H|T], H, Inc) :-
    numar_aparitii(T, H, Ap),
    Inc is Ap + 1.
numar_aparitii([H|T], El, Ap) :-
    numar_aparitii(T, El, Ap).


% lista_cifre/2
% lista_cifre(+NumarNat, -ListaCifre).
% lista_cifre(2048, L).
% L = [2,0,4,8].

lista_cifre_aux(X, [X]) :-
    X < 10.
lista_cifre_aux(Nr, [C|T]) :-
    C is Nr mod 10,
    D is Nr div 10,
    lista_cifre_aux(D, T).

lista_cifre(Nr, Result) :-
    lista_cifre_aux(Nr, Result1),
    reverse(Result1, Result).



% sa se det lista permutarilor circulare ale unei liste
% [1,2,3] - [[1,2,3], [2,3,1], [3,1,2]]

permcirc([], []).
permcirc([H|T], L) :- 
    append(T, [H], L).

lpermcirc(L, L, [L]).
lpermcirc(L, M, [M|LP]) :- 
    permcirc(M, N),
    lpermcirc(L, N, LP).

listpermcirc(L, LP) :- 
    permcirc(L, M),
    lpermcirc(L, M, LP).


% predicatul elimina/3
% elimina(+List, +Elem, -ListFaraElem)

elimina([], _, []).
elimina([H|T], H, TR) :-
    elimina(T, H, TR).
elimina([H|T], Elem, [H|TR]) :-
    elimina(T, Elem, TR).



% multime/2
% multime(+Ls, -LsFaraDupes)

multime([], []).
multime([H|T], Out) :-
    member(H, T),
    multime(T, Out).
multime([H|T], [H|Out]) :-
    not(member(H, T)),
    multime(T, Out).


% emult/1
% verifica daca e multime

emult([]).
emult(L) :-
    multime(L, L1),
    length(L, N1),
    length(L1, N2),
    N1 =:= N2.

emult1([]).
emult1([H|T]) :- 
    emult(T),
    not(member(H, T)).



% intersectia/3
% intersectia(+M1, +M2, -MR)

intersectia([], _, []).
intersectia([H|T], L, R) :-
    not(member(H, L)),
    intersectia(T, L, R).
intersectia([H|T], L, [H|R]) :- 
    member(H, L),
    intersectia(T, L, R).



% diff/3
% diff(+M1, +M2, -MR).

diff([], _, []).
diff([H|T], L, [H|R]) :-
    not(member(H, L)),
    diff(T, L, R).
diff([H|T], L, R) :- 
    member(H, L),
    diff(T, L, R).



% prod_cartezian(+M1, +M2, -MProd).
% [1,2,3]  [4,5,6,7]
% [(1,4), (1,5), (1,6), (1,7), (2,4), (2,5), ...]

elem_prod_multime(_, [], []).
elem_prod_multime(X, [H|T], [(X, H)|R]) :-
    elem_prod_multime(X, T, R).

prod_cartezian([], _, []).
prod_cartezian([H|T], L, R) :-
    elem_prod_multime(H, L, R1),
    prod_cartezian(T, L, RTail),
    append(R1, RTail, R).


% 1
% sa se calc suma el intr-o lista

suma([], 0).
suma([H|T], SNext) :-
    suma(T, S),
    SNext is S + H.

% elimina prima aparitie a unui el intr-o lista

eli(_, [], []).
eli(H, [H|T], T).
eli(El, [H|T], [H|R]) :-
    eli(El, T, R).


% repr arborilor binari in prolog
% nil - arborele vid
% arb/3
% arb(+Radacina, +Stanga, +Dreapta)
% arb(2, arb(4, arb(2, nil, nil), arb(5, nil, nil)), nill).

% parcurgerile arborilor
% inordine, preordine, postordine
% SRD       RSD        SDR

% srd/2

srd(nil, []).
srd(arb(R, S, D), L) :-
    srd(S, Ls),
    srd(D, Ld),
    append(Ls, [R|Ld], L).

rsd(nil, []).
rsd(arb(R, S, D), L) :-
    rsd(S, Ls),
    rsd(D, Ld),
    append([R|Ls], Ld, L).

sdr(nil, []).
sdr(arb(R, S, D), L) :-
    sdr(S, Ls),
    sdr(D, Ld),
    append(Ls, Ld, LTemp),
    append(Ltemp, [R], L).

% sa se determine multimea frunzelor
% frunze/2
% frunze(+Arb, -LFrunze).

frunze(nil, []).
frunze(arb(F, nil, nil), [F]).
frunze(arb(R, S, D), L) :- 
    frunze(S, Ls),
    frunze(D, Ld),
    append(Ls, Ld, L).