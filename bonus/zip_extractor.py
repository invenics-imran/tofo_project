import zipfile

def extract_archive(archpath, dest_dir):
     with zipfile.ZipFile(archpath, 'r') as archive:
          archive.extractall(dest_dir) 

     



if __name__=="__main__":
     extract_archive("C:/Users/ImranSajawal/proj/my_project/app1/bonus/compressed.zip",
                      "C:/Users/ImranSajawal/proj/my_project/app1/bonus/file")
