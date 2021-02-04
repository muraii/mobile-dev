import appex, console

data = []
data.append(appex.get_attachments())
data.append(appex.get_file_paths())
data.append(appex.get_images())
data.append(appex.get_text())
data.append(appex.get_urls())
data.append(appex.get_web_page_info())

keys = [
	'attachments',
	'file paths',
	'images',
	'text',
	'urls',
	'web page'
	]

data_dict = dict(zip(keys, data))
for key in data_dict.keys():
	#print(key, type(data_dict[key]))
	if type(data_dict[key]) == type(dict()):
		for item in data_dict[key].keys():
			print(item, type(data_dict[key][item]))
	elif type(data_dict[key]) == type(list()):
		for part in data_dict[key]:
			print(type(part))
	else:
		print('fart')

#for datum in data:
	#print(type(datum))
	#console.alert("fart", str(type(datum)), "okay")
	#console.alert("fart", str(len(datum), "okay"))

