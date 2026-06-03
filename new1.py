import os

os.chdir("C:/Users/khush/OneDrive/Desktop/Coplur_5Sem/try")
#In try folder there are files named as file1.txt, file2.txt, file3.txt, file4.txt
i=1
for file in os.listdir():
    src=file
    dst="assign"+ str(i) + ".txt"
    os.rename(src,dst)
    i+=1
#After this code is executed, the files will be renamed as assign1.txt, assign2.txt, assign3.txt, assign4.txt

