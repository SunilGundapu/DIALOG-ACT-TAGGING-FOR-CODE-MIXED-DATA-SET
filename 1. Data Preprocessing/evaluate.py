def main():
        file = open("DATASET/output.txt","r")
        #U_E = open("DATASET/ue.txt", "w+")
        #E_U = open("DATASET/eu.txt", "w+")
        file_data = file.readlines()
        tp=0
        fn=0
        spaces=0
        ue=0
        eu=0
        total=len(file_data)-1
        for i in range(0, len(file_data)):
              x=file_data[i].split()
              if(len(x)!=0):
                     if(x[13]==x[14]):
                            tp+=1       
                     else:       
                            fn+=1       
              else:
                    spaces+=1
        total = total-spaces
        x = (tp/total)*100
        print("Total no of words in Testing Data: ", total+spaces)
        print("Positively Predicted: ", tp)
        print("Negatively Predicted: ", fn)
        print("Accuracy of CRF++ : ", x)
        
if __name__=="__main__":
       main()
