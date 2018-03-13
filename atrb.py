import zipfile
for k in range(2):
    txt = open('{id}.txt'.format(id=k),'r')
    main = open('main.txt','r')
    main_out = []
    txt_out = []
    res = []
    main_out = main.read()
    txt_out = txt.read()
    res = main_out + txt_out
    with open('sm{id}.txt'.format(id=k),'a') as resf:
        resf.write(res)
        res_zip = zipfile.ZipFile('{id}.zip'.format(id=k), 'w')
        res_zip.write('sm{id}.txt'.format(id=k), compress_type=zipfile.ZIP_DEFLATED)
    res_zip.close()
    txt.close()
    main.close()