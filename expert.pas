program SimpleExpertSystem;

uses crt;

var
  fever, cough, headache: char;

begin
  clrscr;
  writeln('--- Simple Disease Expert System ---');
  
  write('Do you have fever? (y/n): ');
  readln(fever);

  write('Do you have cough? (y/n): ');
  readln(cough);

  write('Do you have headache? (y/n): ');
  readln(headache);

  writeln;
  writeln('Diagnosis Result:');

  if (fever = 'y') and (cough = 'y') then
    writeln('You might have Flu.')
  else if (fever = 'y') and (headache = 'y') then
    writeln('You might have Malaria.')
  else if (cough = 'y') and (headache = 'y') then
    writeln('You might have Common Cold.')
  else
    writeln('No matching disease found.');

  readln;
end.
