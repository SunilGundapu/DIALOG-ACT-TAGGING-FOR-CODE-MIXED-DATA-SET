def main():       
       from indictrans import Transliterator
       trn = Transliterator(source='eng', target='tel', build_lookup=True)
       file = open("DATASET/datasetforfinal.txt","r")
       file_data = file.readlines()
       print(len(file_data))

if __name__ == "__main__":
       main()
