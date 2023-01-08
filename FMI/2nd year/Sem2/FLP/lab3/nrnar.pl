% successor([x,x,x],Result).
% Result = [x,x,x,x]

successor(Ls, [x|Ls]).

pred([], []).
pred([x|Ls], Ls).

% Definit¸i un predicat plus/3 care adun˘a dou˘a numere.
% plus([x, x], [x, x, x, x], Result).
% Result = [x, x, x, x, x, x]

% plus(N1, N2, Rez) :-
%     plus(N1, N2, 0, Rez).

% plus([], N2, I, Rez) :-
%     plus2(N2, I, Rez).
% plus(N1, N2, I, Rez) :-
%     pred(N1, N1Pre),
%     Inext is I+1,
%     plus(N1Pre, N2, Inext, Rez).

% plus2(Rez, 0, Rez).
% plus2(N1, I, Rez) :-
%     Iprev is I-1,
%     successor(N1, N1Succ),
%     plus2(N1Succ, Iprev, Rez).

plus([], L2, L2).
plus([H1 | L1], L2, [H1 | L3]) :-
plus(L1, L2, L3).

% v1
% plus([], Rez, Rez).
% plus(N1, N2, Rez) :-
%     successor(N2, SN2),
%     pred(N1, PN1),
%     plus(PN1, SN2, Rez).

% Definit¸i un predicat times/3 care ˆınmult¸e¸ste dou˘a numere
% times([x, x], [x, x, x, x], Result).
% Result = [x, x, x, x, x, x, x, x]

%  nu merge inca
% times(N1, N2, Rez) :-
%     times(N1, N2, [], Rez).

% times([], _, Rez, Rez).
% times(N1, N2, Aux, Rez) :-
%     pred(N1, Npred),
%     plus(N2, Aux, Aux),
%     times(Npred, N2, Aux, Rez).

times([], _, []).
times([H|T], L2, LR) :-
    times(T, L2, LTail),
    plus(L2, LTail, LR).

% Definit¸i un predicat element at/3 care, primind o list˘a ¸si un num˘ar
% natural n, ˆıntoarce al n-ulea element din list˘a.

% element_at([tiger, dog, teddy_bear, horse, cow], 3, X).
% X = teddy bear

element_at(Ls, N, Out) :-   
    element_at(Ls, 1, N, Out).

element_at([H|T], I, I, H).
element_at([H|T], I, N, Out) :-
    Inext is I+1,
    element_at(T, Inext, N, Out).

