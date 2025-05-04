print('--- Simple Disease Expert System ---')

fever = input('Do you have fever? (y/n): ').lower()
cough = input('Do you have cough? (y/n): ').lower()
headache = input('Do you have headache? (y/n): ').lower()

print('\nDiagnosis Result:')

if fever == 'y' and cough == 'y':
    print('You might have Flu.')
elif fever == 'y' and headache == 'y':
    print('You might have Malaria.')
elif cough == 'y' and headache == 'y':
    print('You might have Common Cold.')
else:
    print('No matching disease found.')
