import zipfile
import os 

for k in range(2):
    txt = open('{id}.txt'.format(id=k),'r')
    main = open('main.txt','r')
    
    main_out = []
    txt_out = []
    res = []
    
    main_out = main.read()
    txt_out = txt.read()
    
    main_zip = zipfile.ZipFile('main.zip', 'w')
    main_zip.write('main.txt', compress_type=zipfile.ZIP_DEFLATED)
    
    res = main_out + txt_out
    
    with open('sm{id}.txt'.format(id=k),'a') as resf:
        resf.write(res)
        res_zip = zipfile.ZipFile('{id}.zip'.format(id=k), 'w')
        res_zip.write('sm{id}.txt'.format(id=k), compress_type=zipfile.ZIP_DEFLATED)
    
    #t = os.path.getsize('main.txt')
    ct = os.path.getsize('main.zip')
    cts = os.path.getsize('{id}.zip'.format(id=k))
    
    #h = (cts-ct)/t
    
    #print h
    
    main_zip.close()    
    res_zip.close()
    txt.close()
    main.close()