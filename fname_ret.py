import os

"""
pass the parameter as in constructor

rootpath='' #string #root derectory to list all the files 
file_types=() #single string or tuple() #define file extention or file endings here

"""

class filname_ret:
    # initiating constructor
    def __init__(self, rootpath='', file_types=()):
        self.rootpath = rootpath
        self.file_types = file_types
        self.fileDirectory = []
        self.files = []
        try:
            if os.path.exists(self.rootpath) == True :
                print ('root directory is: ',self.rootpath)
                print ('Selected file types to add:  ',self.file_types)
                print ('Extention took as: ',type(self.file_types))

                # following codesblock lists all the subdirectories and and files.
                # 
                for root,d_names,f_names in os.walk(self.rootpath):
                    for f in f_names:
                        # if os.path.split(f)[1].lower().endswith(self.file_types) :
                        if f.lower().endswith(self.file_types) :
                            # print (f)
                            self.fileDirectory.append(os.path.join(root, f))
                            self.files.append(f)
                
                # return self.fileDirectory
            else:
                print ("Path or Files doesn't exist")
        except OSError as error:
            print(error)

    
    # def Cloning(li1):
    #     li_copy = li1[:]
    #     return li_copy

    """
    following function return the list in a list view

    """
    def showList( filname ):
        print('Showing all the files below: \n')
        for item in filname:
            print(item)
            # print(type(item))

    """
    constructor doesn't return any filetypethats why
    returns a list type variable 
    """
    def return_files_name ( self):
        return self.files
    def return_file_dir ( self):
        return self.fileDirectory
