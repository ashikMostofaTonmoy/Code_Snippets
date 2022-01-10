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
        self.fname = []
        try:
            if os.path.exists(self.rootpath) == True :
                print ('root directory is: ',self.rootpath)
                print ('Selected file types to add:  ',self.file_types)
                print ('Extention took as: ',type(self.file_types))

                # following codesblock lists all the subdirectories and and files.
                # 
                for root,d_names,f_names in os.walk(self.rootpath):
                    for f in f_names:
                        if os.path.splitext(f)[1].lower().endswith(self.file_types) :
                            self.fname.append(os.path.join(self.rootpath, f))
                
                # return self.fname
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
    def showFile( filname ):
        print('Showing all the files below: \n')
        for item in filname:
            print(item,'\n')

    """
    constructor doesn't return any filetypethats why
    returns a list type variable 
    """
    def return_files_name ( self):
        return self.fname
