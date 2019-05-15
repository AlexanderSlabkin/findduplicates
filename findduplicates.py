import sys
import subprocess

def myls(path):
    buf = subprocess.check_output(['find', path, '-type', 'f']).decode('utf-8')
    filenames = buf.split('\n')[:-1]
    fullnames = []

    for ind, i in enumerate(filenames):
        fullnames.append(i)
        filenames[ind] =i[i.rfind('/')+1:]
    return filenames, fullnames

print()
filenames = []
#print(myls(sys.argv[1]))
for i in sys.argv[1:]:
    print(i)
    filenames.append(set(myls(i)[0]))
print(len(myls(sys.argv[1])[0]), len(set(myls(sys.argv[1])[0])))
intersection = filenames[0]
for i in filenames[1:]:
    intersection = intersetion & i

print(intersection)
