import string
hplovecraft=open("/home/ziad/Docker/hplovecraft","r")
book1=hplovecraft.read().lower()
janeaustin=open("/home/ziad/Docker/janeaustin","r")
book2=janeaustin.read().lower()
file1=set(book1.translate(str.maketrans('', '', string.punctuation)).split())
file2=set(book2.translate(str.maketrans('', '', string.punctuation)).split())
inter=file1.intersection(file2)
pronouns={'i', 'you', 'he', 'she', 'it', 'we', 'they',	'mine', 'yours', 'his', 'ours', 'which', 'who', 'that','this', 'these', 'those','is','are','after', 'before', 'in','on','at','of','a','the',
'us','the'}
diffset= inter.difference(pronouns)
print("The intersection between the two books: \n ", inter)
print("And thier length: \n",len(inter))
print("The intersection between the two books without pronouns: \n",diffset)
print("And thier length: \n",len(diffset))
