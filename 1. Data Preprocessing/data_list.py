def main():
       file = open("DATASET/words1.txt","r")
       file1 = open("DATASET/lang.txt","r")
       file_data1 = file1.readlines()
       file_data = file.readlines()
       words = []
       labels = []
       train_words = []
       test_words = []
       for i in range(0, len(file_data)):
              m=file_data[i].split()
              if(len(m)>0):
                     a = []
                     b = []
                     a.append(m[0])
                     b.append(m[1])
                     words.append(a)
                     labels.append(b)
                     train_words.append(a)
       for i in range(0, len(file_data1)):
              m=file_data1[i].split()
              a=[]
              a.append(m[0])
              words.append(a)
              test_words.append(a)
       
if __name__=="__main__":
       main()
