file=open("whales.aln")
lines=file.readlines()

genomes={}
current_key=""
for x in range(len(lines)):
	lines[x]=lines[x].rstrip("\n")
	if lines[x][0]==">":
		current_key=lines[x]
		genomes.setdefault(lines[x],"")
	else:
		genomes[current_key]+=lines[x]
print (genomes)

def get_differences(origin,target):
	count=0
	for x in range(len(origin)):
		if origin[x]!=target[x]:
			count+=1
	return count

origin=genomes[">beluga-whale"]
differences=genomes
for x in range(len(genomes)):
	key=list(genomes.keys())[x]
	differences[key]=get_differences(origin,list(genomes.values())[x])
print (differences)
