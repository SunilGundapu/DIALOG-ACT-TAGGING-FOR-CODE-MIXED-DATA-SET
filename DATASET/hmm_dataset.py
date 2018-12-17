def hmm():
    f = open("lang.txt","r")
    file_data=f.readlines()
    new = open("li.txt","w")
    tags = []
    for i in range(0,len(file_data)):
        m = file_data[i].strip().split()
        if(len(m)==2):
            if(m[1].startswith('t')):
                new.write(m[0]+" te"+"\n")
            elif(m[1].startswith('e')):
                new.write(m[0]+" en "+"\n")
            elif(m[1].startswith('u')):
                new.write(m[0]+" univ "+"\n")
            elif(m[1].startswith('n')):
                new.write(m[0]+" ne "+"\n")
            elif(m[1].startswith('a')):
                new.write(m[0]+" acro "+"\n")
        else:
            new.write("\n")

hmm()
