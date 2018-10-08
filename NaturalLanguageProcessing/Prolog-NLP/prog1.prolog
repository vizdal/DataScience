hare(roland).
turtle(franklin).
faster(X,Y):- hare(X), turtle(Y).

busy(X,D) :- taking_course(X,Y), has_lecture(Y,D).
taking_course(joe,nlp).
has_lecture(nlp,friday).

member(X, [X|_]).
member(X,[_|L]) :- member(X,L).
