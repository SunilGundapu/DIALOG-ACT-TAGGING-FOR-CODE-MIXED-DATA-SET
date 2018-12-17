def main():
       f = open("output.txt","r+")
       data = f.readlines()
       test = []
       pred = []
       count=0
       for i in range(0, len(data)):
              m = data[i].strip().split("\t")
              if(len(m)==6):
                     test.append(m[4])
                     pred.append(m[5])
              if(m[4]==m[5]):
                     count+=1
       print(count)


main()
