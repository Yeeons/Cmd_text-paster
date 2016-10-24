# end needs to skip to the end - currently only continues.
# dictionaries don't keep order, but the count does give us a way to fix this - need to fix.
# numbering needs some thought in the future.

import json

# file name section
def file():
	file_name = ''
	while file_name == '':
		file_name = raw_input('file name? ')
	return file_name

dict = {}
count = 0

# heading function
def heading():
	while True:
		content_heading = raw_input('Type of content (1 for heading, 2 for subhead and 3 for body)? ')
		
		try:
			content_heading = int(content_heading)
			
		except:
			if not content_heading:
				print 'Nothing has been entered!'
			if content_heading == 'end':
				with open(file() + '.txt', 'a') as outfile:
					json.dump(dict, outfile, indent=4)
					dict.clear()
					count = 0
					print 'Complete\n'
			if content_heading == 'quit':
				exit()		
			else:	
				print 'Not a number'
			continue
		
		if 1 <= content_heading <= 3:
			if content_heading == 1:
				content_heading = 'Heading'
			if content_heading == 2:
				content_heading = 'Subhead'
			if content_heading == 3:
				content_heading = 'Body'		
		
		else:
			print 'number out of range'
			continue

		return content_heading


# content function
def content():
	content = raw_input('Enter in content: ')
	return content


#needs a end function for heading.
while True:
	count = count + 1
	heading_f = heading() + '_' + str(count)
	content_f = content()
	dict[heading_f] = content_f
	print dict
