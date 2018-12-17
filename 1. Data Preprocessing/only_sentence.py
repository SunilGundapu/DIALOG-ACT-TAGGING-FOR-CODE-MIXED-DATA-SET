def main():
       file= open("new_annotation.txt","r")
       file1 = open("lang.txt","w+")
       file_data = file.readlines()
       for i in range(0, len(file_data)):
              m=file_data[i].split()
              m.pop(0)
              m.pop(-1)
              for i in range(0, len(m)):
                     file1.write(m[i])
                     file1.write("\n")
              file1.write("\n")
              
if __name__ == "__main__":
       main()
