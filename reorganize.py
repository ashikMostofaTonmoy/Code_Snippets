import pandas as pd 
import fname_ret as fnr
import shutil
import os

# root path of images
path= '/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/reorganized'

# destination path where files need to organized
destination='/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/reorganized_respect_to_oriantation/s'

# file type that need to select
files= fnr.filname_ret(rootpath=path, file_types=('.jpg') ).fileDirectory
# fnr.filname_ret.showList(files)
# print(type(files))



if os.path.exists(destination) == False :
    try:
        os.makedirs(destination, exist_ok=True)
    except OSError as error:
        print(error)
# textfile = open(os.path.join(destination,'filelist.txt' ), "w") 


tocheck=['_s_']
    
matching = [s for s in files if any(xs in s for xs in tocheck)] 
if any( matching ):
    for item in matching: 
        # dest = destination +'/'+ str(entry) # destination path
        if os.path.exists(destination) == False :
            try:
                os.makedirs(destination, exist_ok=True)
                # print(f"Directory doesn't exist. \nCreating Directory... {entry} " )
            except OSError as error:
                print(error)
        else:
            pass
            # print(f'Directory {entry} already exists... \nOverwriting data... ')
        try:
            shutil.copy2(item, destination)
            print("File copied successfully.")
        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

        # For other errors
        except:
            print("Error occurred while copying file.")