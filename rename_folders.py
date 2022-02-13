import os
from natsort import natsorted

# Change this Path to where the video is located.
# path: format = r"the path"
path = r"C:\Users\Quentin\Documents\Subject_Videos\BIO"

root_dir = [root[0] for root in os.walk(path)]

# Folder edit --------------------------------------------- #

def editFolderName(namePath):
  folder_list = namePath
  folder_list = folder_list.upper()

  # Change this for Chemistry, Biology, Physics and others (Put in capital letters)
  folder_list = folder_list.replace('BIOLOGY', 'BIO')

  return folder_list


def renameFolder_true(source):
  for j in range(len(source)):
    some_list = editFolderName(source[j])
    os.rename(source[j], some_list)


renameFolder_true(root_dir)

# File edit -----------------------------------------------------#

def editName(namePath):
  video_file = namePath
  num = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
  video_file = video_file.upper()

  # Do not change these requirements.
  video_file = video_file.replace('Q', 'q')
  video_file = video_file.replace('QN', 'q')
  video_file = video_file.replace('MP4', 'mp4')

  # Change this for Chemistry, Biology, Physics and others (Put in capital letters)
  video_file = video_file.replace('BIOLOGY', 'BIO')

  # Do not change these requirements.
  xyz = video_file[3:7]
  video_file = video_file.replace(xyz, 'xyz')

  for e in num:
      video_file = video_file.replace(e, str(int(e)))

  video_file = video_file.replace('xyz', xyz)
  return video_file


def renameFile_true(source):
  for j in range(len(source)):
    some_list = editName(source[j])
    os.rename(source[j], some_list)


for k in range(1, len(root_dir)):
  os.chdir(root_dir[k])

  file_list = os.listdir()
  
  file_list = natsorted(file_list)

  renameFile_true(file_list)