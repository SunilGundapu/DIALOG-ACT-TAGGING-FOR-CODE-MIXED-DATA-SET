import enchant
def main():
       file=open("DATASET/words.txt","r")
       file1=open("words1.txt","w+")
       file_data=file.readlines()
       d = enchant.Dict("en_US")
       for i in range(0,len(file_data)):
              m=file_data[i].split()
              if(len(m)>0):
                     if(d.check(m[0])==True):
                            file1.write(m[0]+"\t"+"en\n")
                     else:
                            file1.write(m[0]+"\t"+m[2]+"\n")
              else:
                     file1.write("\n")
if __name__=="__main__":
       main()
