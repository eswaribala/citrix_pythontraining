import os


FilePath=r"F:\yatrabakup\day6"

for dirpath,dirnames,filenames in os.walk(FilePath):
    #print(filenames)
    #print(dirnames)
    for dir in dirnames:
            print(dir)
            for dirpath,dirnames,fnames in os.walk(FilePath+"/"+dir):
                print(fnames)
                for filename in fnames:
                    print(filename)
                    (name,extn) = os.path.splitext(filename)
                    print(extn)

                    if(extn=='.txt'):
                        print(dir)
                        path=FilePath+"/"+dir+"/"+filename
                        print(path)
                        contents=open(path,mode='r')
                        for line in contents:
                            print(line)
                        print("-----------------------------------")

