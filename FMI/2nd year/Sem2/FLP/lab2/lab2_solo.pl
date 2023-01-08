parent(om1, om2).
parent(om2, om3).

% ancestor_of / 2
ancestor_of(X, Y) :- parent(X, Y).
ancestor_of(X, Y) :- parent(Z, Y), ancestor_of(X, Z).

fibo(0, 1).
fibo(1, 1).
fibo(In, Out) :-
    Pre is In-1,
    Prepre is In-2,
    fibo(Pre, Res1),
    fibo(Prepre, Res2),
    Out is Res1+Res2.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

line(0, _) :- nl.
line(N, Ch) :-
    write(Ch),
    N1 is N-1,
    line(N1, Ch).

square(0, _, _) :- nl.
square(Rows, N, Ch) :-
    line(N, Ch),
    NewRows is Rows - 1,
    square(NewRows, N, Ch).

square(N, Ch) :-
    square(N, N, Ch).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

element_of([H|_], H).
element_of([_|T], El) :-
    element_of(T, El).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

concat_lists([], Out, Out).
concat_lists([H1 | L1], L2, [H1 | L3]) :-
    concat_lists(L1, L2, L3).

con([], L, L).
con([H1|L1], L2, [H1|Out]) :- 
    con(L1, L2, Out).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

len([], 0).
len([H|T], Out) :-
    len(T, S),
    Out is S + 1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

all_a([]).
all_a([H|T]) :- 
    H = a,
    all_a(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

trans_a_b([], []).
trans_a_b([a|L1], [b|L2]) :-
    trans_a_b(L1, L2).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% scalarMult(Sc, Ls, Out).

scalarMult(_, [], []).
scalarMult(Sc, [H|L1], [M|L2]) :-
    scalarMult(Sc, L1, L2),
    M is Sc * H.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dot([], [], 0).
dot([H1|L1], [H2|L2], S2) :-
    dot(L1, L2, S),
    P is H1 * H2,
    S2 is S + P.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

maxi(X, Y, Y) :-
    Y >= X.
maxi(X, Y, X) :-
    X > Y.

max([], 0).
max([H|Li], NewMax) :-
    max(Li, Mx),
    maxi(H, Mx, NewMax).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

reverse_of(List, ListResult) :-
reverse_of(List, [], ListResult).

reverse_of([], List, List).
reverse_of([H |T], ListAux, ListResult) :-
    reverse_of(T, [H | ListAux], ListResult).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

remove_duplicates([], []).
remove_duplicates([H|L1], L2) :-
    member(H, L1),
    remove_duplicates(L1, L2).

remove_duplicates([H|L1], [H|L2]) :-
    not(member(H, L1)),
    remove_duplicates(L1, L2).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% replace([1,2,3,4,3,5,6,3], 3, x, List).
% => [1, 2, x, 4, x, 5, 6, x]

replace([], _, _, []).

replace([X | T], X, Y, [Y | LR]) :-
    replace(T, X, Y, LR).

replace([Z | T], X, Y, [Z | LR]) :-
    replace(T, X, Y, LR).