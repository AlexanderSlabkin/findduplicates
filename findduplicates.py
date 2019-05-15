import sys
import subprocess

def myls(path):
    buf = subprocess.check_output(['find', path, '-type', 'f']).decode('utf-8')
    fullnames = buf.split('\n')[:-1]
    filenames = []
    for index, i in enumerate(fullnames):
        filenames.append(i[i.rfind('/')+1:])
    return filenames, fullnames

FileNames = []
FullNames = []
UniqueNames = []
for i in sys.argv[1:]:
    Files = myls(i)
    print(Files[0])
    FileNames.append(Files[0])
    UniqueNames.append(FileNames[0])
    print(len(FileNames[0]), len(UniqueNames[0]))
    Duplicates = [x for x in UniqueNames[0] if FileNames[0].count(x) > 1]
    FullNames.append(Files[1])
print(len(myls(sys.argv[1])[0]), len(set(myls(sys.argv[1])[0])))
print(f'Duplicates: {Duplicates}')
intersection = FileNames[0]
#print(filenames)
for i in FileNames[1:]:
    intersection = intersection & i

#print(intersection)
print('Done.')
