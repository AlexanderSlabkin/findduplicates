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
    FileNames.append(Files[0])
    UniqueNames.append(set(FileNames[0]))
    print(len(FileNames[0]), len(UniqueNames[0]))
    UniqueDuplicates = [x for x in UniqueNames[0] if FileNames[0].count(x) > 1]
    DuplicatesIndexes = [y for (y,x) in enumerate(FileNames[0]) if FileNames[0].count(x) > 1]
    FullNames.append(Files[1])
    DuplicatesFull = [FullNames[0][i] for i in DuplicatesIndexes]
print(f'Duplicates: {UniqueDuplicates}, lengths is {len(UniqueDuplicates)}')
print(f'Duplicates with paths: {DuplicatesFull}, lengths is {len(DuplicatesFull)}')
intersection = FileNames[0]
#print(filenames)
for i in FileNames[1:]:
    intersection = intersection & i

#print(intersection)
print('Done.')
