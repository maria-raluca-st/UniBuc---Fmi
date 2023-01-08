born(jan, date(20,3,1977)).
born(jeroen, date(2,2,1992)).
born(joris, date(17,3,1995)).
born(jelle, date(1,1,2004)).
born(joan, date(24,12,0)).
born(joop, date(30,4,1989)).
born(jannecke, date(17,3,1993)).
born(jaap, date(16,11,1995)).

% Scriet¸i un predicat year/2 care gase¸ste toate persoanele n˘ascute
% ˆıntr-un anumit an.

year(An, Person) :-
    born(Person, date(_, _, An)).


% Scriet¸i un predicat before/2 care prime¸ste dou˘a date calendaristice ¸si
% care este adev˘arat dac˘a prima expresie reprezint˘a o dat˘a calendaristic˘a
% ˆınaintea datei reprezentate de a doua expresie (putet¸i presupune c˘a datele
% sunt corecte, e.g., nu putet¸i primi 31 Aprilie).

% before(date(31,1,1990), date(7,7,1990)).

lte(X, Y, X) :-
    X < Y.
lte(X, Y, Y) :-
    Y < X.

before(date(D1, M1, Y1), date(D2, M2, Y2)) :-
    Y1 < Y2.

before(date(D1, M1, Y1), date(D2, M2, Y2)) :-
    Y1 = Y2,
    M1 < M2.

before(date(D1, M1, Y1), date(D2, M2, Y2)) :-
    Y1 = Y2,
    M1 = M2,
    D1 < D2.


% Scriet¸i un predicat older/2 care este adev˘arat dac˘a persoana dat˘a ca
% prim argument este mai ˆın vˆarst˘a (strict) decˆat persoana dat˘a ca al doilea
% argument.

% older(jannecke,X).

older(P1, P2) :- 
    born(P1, D1),
    born(P2, D2),
    before(D1, D2).

