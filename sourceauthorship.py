import os
import zipfile
import warnings  

warnings.filterwarnings('ignore')
directory_authors = 'authors'

#СЭМПЛ - Размер до сжатия (T) - архивация сэмпла - размер после сжатия C(T)
#H(T/Si) = (C(SiT)-C(T))/T, где Si - сжатый подклееваемый текст, T - образец
#СОУРС - Размер папки до сжатия S - архивация Si - размер после сжатия C(S)
#Сжатие результата конткатенации - C(SiT)

#Функция нахождения размера папки, содержащей файлы образца, до сжатия 
#то есть коэффициента T 
def getSampleFolderSize(sample_folder):
    total_size = os.path.getsize(sample_folder)
    for item in os.listdir(sample_folder):
        itempath = os.path.join(sample_folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getSampleFolderSize(itempath)
    return total_size
print  'Size of SAMPLE folder before compress: ' + str(getSampleFolderSize('sample_folder')) + ' b.'

#Конкатенация всех файлов папки SAMPLE
sample_project = os.listdir('sample_folder')
with open('sample_project.txt', 'w+') as outfile:
    for fname in sample_project:
        with open('sample_folder/' + fname) as infile:
            outfile.write(infile.read())

sample_project_size = os.path.getsize('sample_project.txt')
print 'Size of SAMPLE project before compress: ' + str(sample_project_size) + ' b.'
print ' '

#Архивация результирующего файла, содержащего все файлы образца; размер получившегося архива
#то есть коэффицента C(T)
            
sample_project_zip = zipfile.ZipFile('sample_project.zip','a')
sample_project_zip.write('sample_project.txt',compress_type = zipfile.ZIP_DEFLATED)
sample_project_zip_size = os.path.getsize('sample_project.zip')
print 'Size of SAMPLE project after compress: ' + str(sample_project_zip_size) + ' b.'
print ' '
print 'Contain sample: ' + str (sample_project_zip.namelist()) + '!!!!!'
print ' '

#Сжатие папок, сожержащих файлы авторских проектов
for filefolder in os.listdir(directory_authors): #перебираем папки автор 1..n
    folder_path = directory_authors+'/'+filefolder
    if os.path.isdir(folder_path): #если folder_path является директорией то печатаем.. 
        print 'Authors: ' + filefolder
        print ' '
        
        for filefolderdown in os.listdir(folder_path): 
            folderdown_path = folder_path + '/' +filefolderdown 
            if os.path.isdir(folderdown_path): 
                print 'Projects: ' + filefolderdown
                print os.listdir(folderdown_path)
                print ' '
                
#                source_folders = glob.glob(folderdown_path)
#                for source_folder in source_folders:
#                    print 'Project: ' + source_folder
#                    print ' '
#
#                    source_folder_zip = zipfile.ZipFile(source_folder + '.zip', 'w')
#                    source_folder_zip.write(source_folder, compress_type=zipfile.ZIP_DEFLATED)
#                    source_folder_zip.close()
#                source_folder_zip_size = os.path.getsize(source_folder + '.zip')
#                print 'Size of SOURCE folder after comress: ' + str(source_folder_zip_size)
#                print 'Contain source: ' + str (source_folder_zip.namelist())

                #result_size = size_of_sample + size_of_source
                #result_of_compress = (size_of_source - size_of_sample_zip)/size_of_sample