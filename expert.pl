% Simple Disease Expert System in Prolog

start :-
    write('--- Simple Disease Expert System ---'), nl,
    
    ask(fever),
    ask(cough),
    ask(headache),
    
    diagnose.

% Ask the user about a symptom
ask(Symptom) :-
    write('Do you have '), write(Symptom), write('? (y/n): '),
    read(Reply),
    (Reply = y -> assert(symptom(Symptom)) ; true).

% Diagnosis rules
diagnose :-
    symptom(fever),
    symptom(cough),
    write('You might have Flu.'), nl, !.

diagnose :-
    symptom(fever),
    symptom(headache),
    write('You might have Malaria.'), nl, !.

diagnose :-
    symptom(cough),
    symptom(headache),
    write('You might have Common Cold.'), nl, !.

diagnose :-
    write('No matching disease found.'), nl.

% To run: consult the file and type `start.` in the Prolog prompt.
