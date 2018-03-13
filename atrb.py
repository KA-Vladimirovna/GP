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
    txt.close()
    main.close()