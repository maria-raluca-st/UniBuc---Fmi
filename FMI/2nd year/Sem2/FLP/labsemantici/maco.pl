aexp(I) :- integer(I).
aexp(X) :- atom(X).
aexp(A1 * A2) :- aexp(A1), aexp(A2).
aexp(A1 + A2) :- aexp(A1), aexp(A2).
aexp(A1 - A2) :- aexp(A1), aexp(A2).

bexp(true).
bexp(false).
bexp(A1 <= A2) :- aexp(A1), aexp(A2).
bexp(A1 >= A2) :- aexp(A1), aexp(A2).
bexp(A1 == A2) :- aexp(A1), aexp(A2).
bexp(and(BE1, BE2)) :- bexp(BE1), bexp(BE2).
bexp(or(BE1, BE2)) :- bexp(BE1), bexp(BE2).
bexp(not(BE)) :- bexp(BE).

stmt(skip).
stmt(X = AE) :- atom(X), aexp(AE).
stmt(if(Be, St1, St2)) :- bexp(Be), stmt(St1), stmt(St2).
stmt(while(Be, St)) :- bexp(B1), stmt(St).
stmt(St1;St2) :-stmt(St1), stmt(St2).
stmt({St}) :- stmt(St).

program(St, AE) :- stmt(St), aexp(AE).

