file=open("whales.aln")
lines=file.readlines()

genomes={}
count=-1
current_key=""
for x in range(len(lines)):
	lines[x]=lines[x].rstrip("\n")
	if lines[x][0]==">":
		current_key=lines[x]
		genomes.setdefault(lines[x],"")
	else:
		genomes[current_key]+=lines[x]
print (genomes)
