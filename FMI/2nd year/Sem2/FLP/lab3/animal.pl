
% /* Animal  database */

animal(alligator). 
animal(tortue) .
animal(caribou).
animal(ours) .
animal(cheval) .
animal(vache) .
animal(lapin) .


% Folosit¸i predicatul name/2 care face conversia ˆıntre un atom ¸si lista
% caracterelor sale, reprezentate prin codurile ASCII. Verificat¸i:
% ?- name(alligator,L).
% ?- name(A, [97, 108, 108, 105, 103, 97, 116, 111, 114]).

mutant(X) :-
    animal(Y),
    animal(Z),
    Y \= Z,
    name(Y, NameY),
    name(Z, NameZ),
    append(Y1, Comm, NameY),
    append(Comm, Z2, NameZ),
    Comm \= [],
    append(NameY, Z2, NewName),
    name(X, NewName).