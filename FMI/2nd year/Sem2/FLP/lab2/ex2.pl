replace([], Src, Dst, []).
replace([Src|T], Src, Dst, [Dst|Out]) :- 
        replace(T, Src, Dst, Out).

replace([H|T], Src, Dst, [H|Out]) :- 
        replace(T, Src, Dst, Out).

a.
b :- a.