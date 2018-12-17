def main():
       file=open("DATASET/words.txt","r")
       new_file = open("DATASET/features.txt", "w+")
       file_data = file.readlines()
       new_file.write("current prev next pos lang\n")
       for i in range(0,len(file_data)):
              if(i>0 and i<len(file_data)-1):             
                     x=file_data[i-1].split()
                     y=file_data[i].split()
                     z=file_data[i+1].split()
                     if(len(y)!=0):
                            new_file.write(y[0]+" ")
                            if(len(x)!=0):
                                   new_file.write(x[0]+" ")
                            else:
                                   new_file.write("null ")
                            if(len(z)!=0):
                                   new_file.write(z[0]+" ")
                            else:
                                   new_file.write("null ")
                            new_file.write(y[1]+" "+y[2]+" ")
                            new_file.write("\n")
                     else:
                            new_file.write("\n") 
              elif(i==0):
                     x=file_data[i].split()
                     y=file_data[i+1].split()
                     new_file.write(x[0]+" ")
                     new_file.write("null ")
                     if(len(y)!=0):
                            new_file.write(y[0]+" ")
                     else:
                            new_file.write("null ")  
                     new_file.write(x[1]+" "+x[2]+" ")    
                     new_file.write("\n")
              elif(i==len(file_data)-1):
                     x=file_data[i].split()
                     y=file_data[i-1].split()
                     new_file.write(x[0]+" ")
                     if(len(y)!=0):
                            new_file.write(y[0]+" ")
                     else:
                            new_file.write("null ")    
                     new_file.write("null ") 
                     new_file.write(x[1]+" "+x[2]+" ")
                     new_file.write("\n")  
if __name__=="__main__":
       main()
       

