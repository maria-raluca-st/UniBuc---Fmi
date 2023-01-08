% Crossword puzzle

word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(enhance,e,n,h,a,n,c,e).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).

% Definit¸i un predicat crosswd/6 care calculeaz˘a toate variantele ˆın care
% putet¸i completa grila. Primele trei argumente trebuie s˘a fie cuvintele pe
% vertical˘a, de la stˆanga la dreapta, (V1,V2,V3), iar urm˘atoarele trei
% argumente trebuie s˘a fie cuvintele pe orizontal˘a, de sus ˆın jos (H1,H2,H3).

crosswd(V1, V2, V3, H1, H2, H3) :-
    word(V1, _, L1, _, L4, _, L7, _),
    word(V2, _, L2, _, L5, _, L8, _),
    word(V3, _, L3, _, L6, _, L9, _),
    word(H1, _, L1, _, L2, _, L3, _),
    word(H2, _, L4, _, L5, _, L6, _),
    word(H3, _, L7, _, L8, _, L9, _).

% crosswd(A1, B2, C3, D, E, F).