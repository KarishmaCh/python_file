#copy img
def copy_img():
	read_file=open('tom_jerry.png','rb')
	bytes=read_file.read()

	write_file=open('newimg.png','wb')

	write_file=file.write(bytes)

	read_file.close()
	write_file.close()

	print('file is close')

if __name__ == '__main__':
		copy_img()