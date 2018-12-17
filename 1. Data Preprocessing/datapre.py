import nltk
def main():
       file = open("new_annotation.txt","r")
       file1=open("afterpre.txt","w+")
       file_data=file.readlines()
       temp="SYS:"
       for i in range(0,len(file_data)):
              m=file_data[i].split()
              if(len(m)>0 and (m[0]=="SYS:" or m[0]=="USER:") ):
                     temp =str(m[0])
              if(file_data[i].startswith("#")==False and len(m)>0 and m[0]!="SYS:" and m[0]!="USER:"):
                     file1.write(temp+"\t"+file_data[i])
              
if __name__=="__main__":
       main()
