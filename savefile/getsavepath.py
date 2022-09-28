import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def genfilepath(projectname,time):
    temptime = str(time).replace('-','_')
    temptime = temptime.replace('T','/')
    temptime = temptime.replace(':','_')
    outpath = ROOT_PATH+'/'+projectname+'/'+temptime+'.csv'
    makepath = os.path.split(outpath)
    if os.path.exists(makepath[0]):
        print('path safe')
    else:
        os.makedirs(makepath[0])
    return outpath


