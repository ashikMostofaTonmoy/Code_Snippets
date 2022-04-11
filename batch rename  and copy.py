import pandas as pd 
import fname_ret as fnr
import shutil
import os

# root path of images
path= '/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images'

# destination path where files need to organized
destination='/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/reorganized'

# file type that need to select
files= fnr.filname_ret(rootpath=path, file_types=('.jpg') ).fileDirectory
# fnr.filname_ret.showList(files)
# print(type(files))


# read the excel file 
df= pd.read_excel('/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/b2_sanitized.xlsx', index_col=1)
# df= pd.read_excel('/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/220212_bhalo_Acme AI_Jan-Feb 2022_Batch 2_Cattle Information.xlsx', header=2 , index_col=2)
if os.path.exists(destination) == False :
    try:
        os.makedirs(destination, exist_ok=True)
    except OSError as error:
        print(error)
textfile = open(os.path.join(destination,'filelist.txt' ), "w") 


for entry in df.index: # iterate through index file
    dest = os.path.join(destination, str(entry) ) # destination path
    print(f"Destination path: {dest} ")
    if pd.isna(entry) == False:
        side = str(df.loc[entry, 'Side Image Reference'])
        rear= str(df.loc[entry, 'Rear Image Reference'])
        weight = float(df.loc[entry, 'Weight'])
        # age = df.loc[entry, 'Age']
        sex = df.loc[entry, 'Sex']
        tocheck=[side,rear]
    
        matching = [s for s in files if any(xs in s for xs in tocheck)] 
        if any( matching ):
            for item in matching: 
                # dest = destination +'/'+ str(entry) # destination path
                if os.path.exists(dest) == False :
                    try:
                        os.makedirs(dest, exist_ok=True)
                        print(f"Directory doesn't exist. \nCreating Directory... {entry} " )
                    except OSError as error:
                        print(error)
                else:
                    print(f'Directory {entry} already exists... \nOverwriting data... ')
                try:
                    shutil.copy2(item, dest)
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
        try :
            for root,d_names,f_names in os.walk(dest):
                # print(f"{entry} : { f_names }")
                # print ( type(f_names))
                for name in f_names:
                    # os.rename(old_name, new_name)
                    old_name= os.path.join(root, name)
                    new_name=''
                    if side in name:
                        new_name = f'{entry}_s_{weight:.0f}_{sex[0]}.jpg'
                        # print(f" {entry} Side ref: {side} and image name is : {name} | newName : {new_name}  ")
                    elif rear in name:
                        new_name = f'{entry}_r_{weight:.0f}_{sex[0]}.jpg'
                        # print(f" {entry} rear ref: {rear} and image name is : {name} | newName : {new_name}  ")
                    # print(f" {entry} ref image name is : {name} | newName : {new_name}  ")
                    new = os.path.join(root, new_name)

                    print (f" Old name :{old_name} | New name: {new} \n")
                    # new_name= os.path.join(root, name_formate)
                    if os.path.isfile(new):
                        print("The file already exists in check block")
                    else:
                        # Rename the file
                        try :
                            os.rename(old_name, new)
                            # writing names to the file
                            textfile.write(new_name + "\n")
                            print("Source is renamed to destination successfully.")

                        except FileExistsError:
                            print("File already Exists")
                        
                        # If Source is a file 
                        # but destination is a directory
                        except IsADirectoryError:
                            print("Source is a file but destination is a directory.")
                        
                        # If source is a directory
                        # but destination is a file
                        except NotADirectoryError:
                            print("Source is a directory but destination is a file.")
                        
                        # For permission related errors
                        except PermissionError:
                            print("Operation not permitted.")
                        
                        # For other errors
                        except OSError as error:
                            print(error)      
        except:
            print(f"nothing happened")
            pass
textfile.close()