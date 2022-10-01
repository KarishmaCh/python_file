#open and write in file demo.txt
def demo_data():
	with open('demo.txt','w') as f:
		print('file opened')
		f.write('gm')
		print('file writing is done 1')
	print('file close')

if __name__ == '__main__':
	demo_data()