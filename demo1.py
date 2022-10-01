#properties of files
def getProperties():
	f=open('sample.txt','w')
	print(f'the name of the file is {f.name}')
	print(f'the name of the file is {f.mode}')

	print(f'is file readable ? {f.readable()}')

if __name__ == '__main__':
	getProperties()