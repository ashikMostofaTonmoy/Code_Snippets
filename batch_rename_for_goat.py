import pandas as pd
import fname_ret as fnr
import shutil
import os

# root path of images
# path = 'inputData/Batch 3.3 Images'
# path = 'C:/Users/User/Desktop/B3.6/B3.6 preprocess/Batch 3.6 Images (364)'
path = 'C:/Users/User/Desktop/Aug/goat/Batch 1.1 Images'



# destination path where files need to organized
# destination = 'C:/Users/User/Desktop/B3.6/B3.6 preprocess/Batch 3.6 Images (364)/reorganized'
# destination = 'D:dataset preprocess code/reorganized'
destination = 'C:/Users/User/Desktop/Aug/goat/final3'


# file type that need to select
files = fnr.filname_ret(rootpath=path, file_types=('.jpg')).fileDirectory
# fnr.filname_ret.showList(files)
# print(type(files))


# read the excel file
# df = pd.read_csv('inputData/b-3.2.csv', index_col=0)
df = pd.read_csv('d3.csv', index_col=0)
# df = pd.read_excel('/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/220212_bhalo_Acme AI_Jan-Feb 2022_Batch 2_Cattle Information.xlsx', header=2, index_col=2)
if os.path.exists(destination) == False:
    try:
        os.makedirs(destination, exist_ok=True)
    except OSError as error:
        print(error)
textfile = open(os.path.join(destination, 'filelist.txt'), "w")
logText = open(os.path.join(destination, 'log.txt'), "w")

breed_map= {
    'Deshi' : 1, 
    'Jamunapari' : 2,
    'Boer' : 3,
    'Totapuri' : 4,
    'Black Bengal' : 5,
    'Barbari' : 6,
    'Cross (Totapuri)' : 7,
    'Cross (Black Bengal)' : 8, 
    'Cross (Boer)' : 9,
    'Cross (Jamunapari)' : 10,
    'Cross (Barbari)' : 11,
    'Deshi (Black Bengal)': 12
    }

for entry in df.index:  # iterate through index file
    dest = os.path.join(destination, str(entry))  # destination path
    
    destpath = f"\nDestination path: {dest} "
    
    print(destpath)
    logText.write( destpath + "\n")
    if pd.isna(entry) == False:
        side = str(df.loc[entry, 'Top Image Reference'])

        weight = df.loc[entry, 'Weight']
        # age = df.loc[entry, 'Age']
        sex = df.loc[entry, 'Sex']
        tocheck = [side]
        breed =  df.loc[entry, 'Breed']
        # found_breed = breed_map[breed]

        matching = [s for s in files if any(xs in s for xs in tocheck)]
        dest = destination  # destination path
        if any(matching):
            for item in matching:
                # dest = destination +'/'+ str(entry) # destination path
                # if os.path.exists(dest) == False:
                #     try:
                #         os.makedirs(dest, exist_ok=True)
                #         directory_created = f"Directory doesn't exist. \nCreating Directory... {entry} "
                #         print(directory_created)
                #         logText.write(directory_created + "\n")
                #     except OSError as error:
                #         print(error)
                #         logText.write(error + "\n")
                # else:
                #     directory_exists = f'Directory {entry} already exists... \nOverwriting data... '
                #     print(directory_exists)
                #     logText.write(directory_exists + "\n")
                try:
                    shutil.copy2(item, dest)
                    success_copy = "File copied successfully."
                    print(success_copy)
                    logText.write(success_copy + "\n")
                # If source and destination are same
                except shutil.SameFileError:
                    same_name = "Source and destination represents the same file."
                    print(same_name)
                    logText.write(same_name + "\n")

                # If there is any permission issue
                except PermissionError:
                    permission = "Permission denied."
                    print(permission)
                    logText.write(permission + "\n")

                # For other errors
                except:
                    error_copy = "Error occurred while copying file."
                    print(error_copy)
                    logText.write(error_copy + "\n")
                logText.write("matchinh done" + "\n")
            
        try:
            logText.write("Enterring 1st operation block" + "\n")
            for root, d_names, f_names in os.walk(dest):
                # print(f"{entry} : { f_names }")
                # print ( type(f_names))
                for name in f_names:
                    # os.rename(old_name, new_name)
                    old_name = os.path.join(root, name)
                    prev_name = f"prev name: {old_name}"
                    logText.write( prev_name + "\n")
                    new_name = ''
                    if side in name:
                        new_name = f'{entry}_{weight:.0f}_{sex[0]}_{breed_map[breed]}.jpg'
                        # print(f" {entry} Side ref: {side} and image name is : {name} | newName : {new_name}  ")
                    # elif rear in name:
                    #     new_name = f'{entry}_r_{weight:.0f}_{sex[0]}.jpg'
                        # print(f" {entry} rear ref: {rear} and image name is : {name} | newName : {new_name}  ")
                    # print(f" {entry} ref image name is : {name} | newName : {new_name}  ")
                    new = os.path.join(root, new_name)
                    name_change = f"New name: {new}"
                    print(name_change)
                    logText.write(name_change + "\n")
                    # new_name= os.path.join(root, name_formate)
                    if os.path.isfile(new):
                        file_exist = "The file already exists in check block"
                        print(file_exist)
                        logText.write(file_exist + "\n")
                    else:
                        # Rename the file
                        
                        logText.write("Enterring rename operation block" + "\n")
                        try:
                            os.rename(old_name, new)
                            # writing names to the file
                            textfile.write(new_name + "\n")
                            success_rename = "Source is renamed to destination successfully." 
                            print(success_rename)
                            logText.write(success_rename + "\n")

                        except FileExistsError:
                            file_exist_disc = "File already Exists"
                            print(file_exist_disc)
                            logText.write(file_exist_disc + "\n")

                        # If Source is a file
                        # but destination is a directory
                        except IsADirectoryError:
                            is_directory_error = "Source is a file but destination is a directory."
                            print(is_directory_error)
                            logText.write(is_directory_error + "\n")

                        # If source is a directory
                        # but destination is a file
                        except NotADirectoryError:
                            not_directory_error = "Source is a directory but destination is a file."
                            print(not_directory_error)
                            logText.write(not_directory_error + "\n")

                        # For permission related errors
                        except PermissionError:
                            permission_error = "Operation not permitted."
                            print(permission_error)
                            logText.write(permission_error + "\n")

                        # For other errors
                        except OSError as error:
                            print(error)
                            logText.write(error + "\n")
        except:
            nothing_error = f"nothing happened"
            print(nothing_error)
            logText.write(nothing_error + "\n")
            pass
textfile.close()
logText.close()