import os
from natsort import natsorted

path = r"C:\Users\Quentin\Desktop\BOSS\sorted\BIO\BIO2002"

os.chdir(path)


def editName (namePath):
    bio_list = namePath
    num = ['01', '02', '03', '04', '05', '06', '07', '08', '09']

    for i in range(len(bio_list)):
        bio_list[i] = bio_list[i].replace('Q', 'q')
        bio_list[i] = bio_list[i].replace('qn', 'q')
        bio_list[i] = bio_list[i].replace('BIOLOGY', 'BIO')
        bio_list[i] = bio_list[i].replace('bio', 'BIO')

        xyz = bio_list[i][3:7]
        bio_list[i] = bio_list[i].replace(xyz, 'xyz')

        for e in num:
            bio_list[i] = bio_list[i].replace(e, str(int(e)))

        bio_list[i] = bio_list[i].replace('xyz', xyz)

    bio_list = natsorted(bio_list)
    return bio_list

def renameFile(source):
    for j in range(len(source)):
        source_upper = source[j].upper()
        os.rename(source[j], source_upper)

def renameFile_true(source, destination):
    for j in range(len(source)):
        os.rename(source[j], destination[j])
    

# name = [x[0] for x in os.walk(path)]
name = path

for k in range(1, 2):
    new_name = name
    os.chdir(new_name)

    bio_list = os.listdir()
    bio_list = natsorted(bio_list)
    bio_original = bio_list[:]


    bio_list_edit = editName(bio_list)

    for i in bio_list_edit:
        print(i)

    # renameFile(bio_original)  # Run this first

    bio_list_true = os.listdir()
    bio_list_true = natsorted(bio_list_true)
    # print("\n")
    # for i in bio_list_true:
    #     print(i)
    renameFile_true(bio_list_true, bio_list_edit) # Run this second
