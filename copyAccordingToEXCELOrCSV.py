import pandas as pd 
import fname_ret as fnr
import shutil
import os

path= '/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images'
destination='/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/reorganized'

files= fnr.filname_ret(rootpath=path, file_types=('.jpg') ).fileDirectory
# fnr.filname_ret.showList(files)
# print(type(files))

df= pd.read_excel('/run/media/ashiktonmoy/New Volume/Projects/Cattletest_2/inputData/Batch 2 Images/b2_sanitized.xlsx', index_col=1)

for entry in df.index:
    dest = os.path.join(destination, str(entry) ) # destination path
    print(dest)
    if pd.isna(entry) == False:
        side = str(df.loc[entry, 'Side Image Reference'])
        rear= str(df.loc[entry, 'Rear Image Reference'])
        # weight = df.loc[entry, 'Weight'] 
        # length = df.loc[entry, 'Length'] 
        # girth =  df.loc[entry, 'Girth']
        tocheck=[side,rear]
        # new_name = f'{entry}_{side}_{weight}_{length}_{girth}'
        
        # print(f"{entry} |side image num: {side} | back img num: {rear}")
        # print (type(side))
        # matchers = ['abc','def']
        # matching = [s for s in my_list if any(xs in s for xs in tocheck)]
        # if any( item for items in files):
        #     pass
     
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
