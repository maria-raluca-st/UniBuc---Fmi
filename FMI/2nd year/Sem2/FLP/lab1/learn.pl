happy(vincent).
listens2Music(butch).
playsAirGuitar(vincent):-
        listens2Music(vincent),
        happy(vincent).

loves(vincent,mia).
loves(marsellus,mia).
loves(pumpkin,honey_bunny).
loves(honey_bunny,pumpkin).

jealous(X,Y):-  loves(X,Z),  loves(Y,Z), Y \= X.