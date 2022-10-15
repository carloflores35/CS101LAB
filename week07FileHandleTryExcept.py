while True:
    try:
        mpg = int(input('Enter the minimum mpg ==> '))
        while mpg != range(0, 101):
            if mpg < 0:
                print('Fuel economy given must be greater than 0')
                mpg = int(input('Enter the minimum mpg ==>'))
            elif mpg > 100:
                print('Fuel economy must be less than 100')
                mpg = int(input('Enter the minimum mpg ==>'))
            else:
                break
        break
    except ValueError:
        print('You must enter a number for the fuel economy')
while True:
    try:    
        inputVehFile = input('Enter the name of the input vehicle file ==> ')
        openInVehFile = open(inputVehFile)
        break
    except FileNotFoundError:
        print('Could not open file', inputVehFile)
while True:
    try:    
        outputVehFile = input('Enter the name of the file to output to ==> ')
        openOutVehFile = open(outputVehFile, 'a')
        break
    except IOError:
        print('There is an IOError', outputVehFile)
skip_header = openInVehFile.readline()
for line in openInVehFile:
    lineParts = line.split('\t')
    mpgcolumn = lineParts[-3]
    try:
        if mpg <= int(mpgcolumn):
            print(f'{lineParts[0]:<5}{lineParts[1]:<20}{lineParts[2]:<45}{mpgcolumn:>10}', file = openOutVehFile)
    except ValueError:
        print(f'Could not convert value', lineParts[-3], 'for vehicle', lineParts[0], lineParts[1], lineParts[2])

openInVehFile.close()
openOutVehFile.close()
