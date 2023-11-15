import PySimpleGUI as sg
from zipcreator import make_archive


label1=sg.Text("select files to compress")
input1=sg.InputText()
choose_button1=sg.FilesBrowse("choose", key="files")

label2=sg.Text("select destination folder")
input2=sg.InputText()
choose_button2=sg.FolderBrowse("choose", key="folder")

compress_button=sg.Button("Compress")
window=sg.Window("files compressor", layout=[[label1,input1,choose_button1],
                                             [label2,input2,choose_button2],
                                             [compress_button]])

# Compress
# {0: 'C:/Users/ImranSajawal/proj/my_project/app1/trial/a.txt;C:/Users/ImranSajawal/proj/my_project/app1/trial/b.txt', 'choose': 'C:/Users/ImranSajawal/proj/my_project/app1/trial/a.txt;C:/Users/ImranSajawal/proj/my_project/app1/trial/b.txt', 1: 'C:/Users/ImranSajawal/proj/my_project/app1/trial', 'choose0': 'C:/Users/ImranSajawal/proj/my_project/app1/trial'}
# this will be the output if we choose a,b for files to compress and trial for compress file and since both inout1 and inout2 have same value as choose button it will have same value as in output.


while True:
        event,values= window.read()
        print(event)
        print(values)
        filepaths=values["files"].split(';')
        folderpath=values["folder"]
        make_archive(filepaths,folderpath)


window.close()