% Maze

connected(1,2).
connected(3,4).
connected(5,6).
connected(7,8).
connected(9,10).
connected(12,13).
connected(13,14).
connected(15,16).
connected(17,18).
connected(19,20).
connected(4,1).
connected(6,3).
connected(4,7).
connected(6,11).
connected(14,9).
connected(11,15).
connected(16,12).
connected(14,17).
connected(16,19).


% Ad˘augat¸i un predicat path/2 care indic˘a dac˘a dintr-un punct putet¸i s˘a
% ajunget¸i ˆıntr-un alt punct (ˆın mai mult¸i pa¸si), legˆand conexiunile din baza
% de cuno¸stint¸e.

% path(X, Y) :-
%     connected(X, Y).
% path(X, Y) :-
%     connected(X, Z),
%     path(Z, Y).

%  nu stiu daca trb si asta neaparat
% path(X, Y) :-
%     connected(Z, Y),
%     path(X, Z).

% a Putet¸i ajunge din punctul 5 ˆın punctul 10?
% path(5, 10).

% ˆIn ce puncte putet¸i s˘a ajunget¸i plecˆand din 1?
% path(1, X).

% Din ce puncte putet¸i s˘a ajunget¸i ˆın punctul 13?
% path(X, 13).


% connected(1,2).
% connected(2,1).
% connected(1,3).
% connected(3,4).


path(X, Y) :-
    path(X, Y, []).

path(X, Y, _) :-
    connected(X, Y).
path(X, Y, _) :-
    connected(X, Z),
    not(member(Z, LS)),
    path(Z, Y, [Z|LS]).