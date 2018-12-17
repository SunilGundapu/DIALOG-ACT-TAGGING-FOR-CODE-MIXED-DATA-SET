def main():
       file = open("DATASET/asklib_data.txt","r")
       file1 = open("DATASET/sent1.txt","w+")
       file_data = file.readlines()
       for i in range(0,len(file_data)):
              m = file_data[i].split()
              if(len(m)>0):
                     file1.write(m[0]+" ")
              else:
                     file1.write("\n")

if __name__=="__main__":
       main()
