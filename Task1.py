name = input('Enter the students name: ')

dictionary = {'Mike':98,'Nick':43,'Rico':100,'Alice':87}

if name in dictionary:
    print("{}'s marks: {}".format(name,dictionary[name]))
else:
    print('{} is not found in the records.'.format(name))
