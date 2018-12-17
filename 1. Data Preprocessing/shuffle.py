import random
def main():
       file = open("DATASET/total_data.txt","r")
       file1 = open("DATASET/sent_shuf.txt","w+")
       file_data = file.readlines()
       for i in range(0, len(file_data)):
              m = file_data[i].split()
              if(len(m)>0):
                     file1.write(m[0]+" "+m[1]+" "+m[2]+" "+"\t")
              else:
                     file1.write("\n")
       file.close()
       file1.close()
       with open("DATASET/sent_shuf.txt","r") as source:
              data = [ (random.random(), line) for line in source ]
       data.sort()
       with open("DATASET/shuflle.txt","w") as target:
              for _, line in data:
                     target.write( line )
       file = open("DATASET/shuflle.txt","r")
       file1 = open("DATASET/sent_shuf.txt","w")
       file_data = file.readlines()
       for i in range(0, len(file_data)):
              m = file_data[i].split("\t")
              for j in range(0, len(m)):
                     file1.write(m[j])
                     file1.write("\n")
              
if __name__=="__main__":
       main()
