import os 
import zipfile
def zip_extract(local_zip , extracted_path):   
    zip_ref = zipfile.ZipFile(local_zip, 'r')
    if os.path.exists(extracted_path) == False :
        try:
            os.makedirs(extracted_path, exist_ok=True)
            print("Directory doesn't exist. \nCreating Directory..." )
        except OSError as error:
            print(error)
    else:
        print('Directory already exists... \nOverwriting data... ')
    if os.path.exists(extracted_path):
        print('Extracting....')
        zip_ref.extractall(extracted_path)
        zip_ref.close()
        print('Extraction finished')

    else:
        print("directory isn't defined... \nPlease Specify the Derectory.")