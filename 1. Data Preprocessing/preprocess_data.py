import re,string
def main():
       file = open("DATASET/feature_data.txt","r")
       new_file = open("DATASET/new_one.txt", "w+")
       file_data = file.readlines()
       ext=" "
       punc = string.punctuation 
       count=0     
       for f in file_data:
              count=count+1
              k=str(f)
              index=f.split()
              if(k!="\n"):
                     new_file.write(index[0]+" "+index[6]+" "+index[-1]+"\n")
              elif(k=="\n"):
                     new_file.write("\n")
                                                             
if __name__=="__main__":
       main()
