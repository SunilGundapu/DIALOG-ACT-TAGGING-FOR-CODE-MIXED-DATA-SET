import re
def checkLower(s):
	p=0
	for c in s:
		if c.islower():
			p+=1
	if p==len(s):
		return True
	else:
		return False
def IsNumeral(s):
	if any(char.isdigit() for char in s):
		return True
	else:
		return False
			
def IsAnyUpper(s):
	for x in s:
		if(x.isupper()):
			return True
	else:
		return False

def IsFUpper(s):
	if(s[0].isupper()):	
		return True
	else:
		return False

def IsSymbol(s):
	if re.match('^[\w-]+$', s):
		return False
	else:
		return True
context_length=2
#words = open('context.txt','r').readlines()
#label= open("labels.txt","r").readlines()
p=0
with open("DATASET/sent_shuf.txt") as f,open("feature_data.txt","w") as fw:
	#fw.write("Word\tIsLowercase\tNumeral\tFUpper\tAnyUpper\tSymbol\tw[0:1]\tw[0:2]\tw[0:3]\tw[-1:]\tw[-2:]\tw[-3:]\tbf1\tbf2\taf1\taf2\n")
	for line in f:
		if(line=="\n"):
			fw.writelines("\n")
			p+=1
		else:
			i = line[:-1] 
			l=i.split()
			#print l[0]
			result=[]
			result.append(l[0])
			#result.append(" ")
			#result.append(l[1])
			result.append("\t")
			if (checkLower(l[0])):
				result.append("T"+"\t")
			else:
				result.append("F"+"\t")
			if(IsNumeral(l[0])):
				result.append("T"+"\t")
			else:
				result.append("F"+"\t")
			if(IsFUpper(l[0])):
				result.append("T"+"\t")
			else:
				result.append("F"+"\t")
			if(IsAnyUpper(l[0])):
				result.append("T"+"\t")
			else:
				result.append("F"+"\t")
			if(IsSymbol(l[0])):
					result.append("T"+"\t")
			else:
				result.append("F"+"\t")

			if(len(l[0])>=3):
				#print l[0][1]
				result.append(l[1]+"\t"+l[0][0:1]+'\t'+l[0][0:2]+'\t'+l[0][0:3]+'\t'+l[0][-1:]+'\t'+l[0][-2:]+'\t'+l[0][-3:]+'\t'+l[2])
			else: 
				#print "null"
				if(len(l[0])==2):
					result.append(l[1]+"\t"+l[0][0:1]+'\t'+l[0][0:2]+'\t'+"null"+'\t'+l[0][-1:]+'\t'+l[0][-2:]+'\t'+"null"+'\t'+l[2])
				else:
					result.append(l[1]+"\t"+l[0][0:1]+'\t'+"null"+'\t'+"null"+'\t'+l[0][-1:]+'\t'+"null"+'\t'+"null"+'\t'+l[2])		
			result.append("\n")
			fw.writelines(result)
			#fw.writelines(words[p][:-1]+"\t")
			#fw.write(label[p])
			p+=1
		
		
