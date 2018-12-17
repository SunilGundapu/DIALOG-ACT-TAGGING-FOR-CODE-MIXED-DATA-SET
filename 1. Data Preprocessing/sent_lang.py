def main():
       file1 = open("DATASET/output.txt","r")
       file = open("output.txt","w+")
       file_data1 = file1.readlines()
       for i in range(0, len(file_data1)):
              m=file_data1[i].split()
              if(len(m)>0):
                     file.write(m[0])
                     file.write("\\")
                     file.write(m[12]+" ")
              else:
                     file.write("\n")                     
       file.close()
       file1.close()
       file = open("output.txt","r")
       file1 = open("new_annotation.txt","r")
       file2 = open("final.txt","w+")
       file_data = file.readlines()
       file_data1 = file1.readlines()
       for i in range(0,len(file_data1)):
              m = file_data1[i].split()
              n = file_data[i].split("\n")
              file2.write(m[0]+"\t"+n[0]+"\t"+m[-1]+"\n")
       
if __name__=="__main__":
       main()
