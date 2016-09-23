#!/usr/bin/python
import csv,sys
import re
from collections import OrderedDict

def read_data_frm_file(file_name):	#read data from csv file and store it in a list
	f=open(file_name,'rU')
	reader=csv.reader(f)
	data=[]
	for rows in reader:
		data.append(rows)
	return data

def distinctMany(columnNames,tableNames):	# prints distinct tuple of given columns
#	printHeader(columnNames,tableNames,dictionary)
	print "Output :"
	string=""
	for attr in columnNames:
#		for tab in tableNames:
		if attr in dictionary[tableNames]:
			if not string == "":
				string+=','
			string+=tableNames+'.'+attr
	print string
	temp = []
	check = 0
	tName = tableNames + '.csv'
	tableNames=tableNames.split(' ')
	with open(tName,'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			for col in columnNames:
				x = row[dictionary[tableNames[0]].index(col)]
				if x not in temp:
					temp.append(x)
					check =1
					print x,
			if check == 1 :
				check = 0
				print


def printoutput(file_data,attr_names,table_names):	#print output in desired format
#	print attr_names
	print "Output :"
	string=""
	for attr in attr_names:
		for tab in table_names:
			if attr in dictionary[tab]:
				if not string == "":
					string+=','
				string+=tab+'.'+attr
	print string
#	print dictionary[table_names[0]]
	for data in file_data:
		for attr in attr_names:
			print data[dictionary[table_names[0]].index(attr)],
		print
			
def getdistinctele(colList,columnname,tablename):	# get distinct elements of column in table
#	print "Output :"
	string=""
	string+=tablename+'.'+columnname
	print string
	colList = list(OrderedDict.fromkeys(colList))
	for col in range(len(colList)):
		print colList[col]


def func(funcname,columnname,tablename):	# this is an aggregate function applied on a column
	# only one column is taken into consideration
#	print "in func"
#	print columnname
#	print type(columnname)
	if columnname=='*':
		sys.exit('error:Invalid syntax')
	if columnname not in dictionary[tablename]:
		sys.exit('column not found in table')
	file_name=""
	file_name+=tablename+'.csv'
	filedata=read_data_frm_file(file_name)
	colList = []
	for data in filedata:
		colList.append(int(data[dictionary[tablename].index(columnname)]))
	print "Output :"
	string=""
	string+=tablename+'.'+columnname
	if funcname.lower() == 'max':
		print max(colList)
	elif funcname.lower() == 'min':
		print min(colList)
	elif funcname.lower() == 'sum':
		print sum(colList)
	elif funcname.lower() == 'avg':
		print sum(colList)/len(colList)
	elif funcname.lower() == 'distinct':
		getdistinctele(colList,columnname,tablename)
	else :
		print "ERROR"
		print "Unknown function : ", '"' + func + '"'

def processWhereOrQuery(columnnames,table1,col1,val1,table2,col2,val2,flag1,flag2):
# this function executes or operator in the where part of the query 
	table1_name=table1+'.'+'csv'
	table2_name=table2+'.'+'csv'
	table1_data=read_data_frm_file(table1_name)
	table2_data=read_data_frm_file(table2_name)
#	print dictionary[table1].index(col1)
	print "Output:"
	string=""
	for col in columnnames:
		if col in dictionary[table1]:
			if not string == "":
				string+=','
			string+=table1+'.'+col
		else:
			if not string == "":
				string+=','
			string+=table2+'.'+col
	check=0
	for rows1 in table1_data:
#		print rows1
		for rows2 in table2_data:
#			print rows1[dictionary[table1].index(col1)]
			if flag1==0 and flag2==0: 
#				print "entered 1st case"
				if rows1[dictionary[table1].index(col1)]<val1 or rows2[dictionary[table2].index(col2)]<val2:
					for col in columnnames:
						if col in dictionary[table1]:
							print rows1[dictionary[table1].index(col)],
						else:
							print rows2[dictionary[table2].index(col)],
						check=1
					if check==1:
						check=0
						print
			elif  flag1==0 and flag2==1: 
#				print "entered 2nd case"
				if rows1[dictionary[table1].index(col1)]<val1 or rows2[dictionary[table2].index(col2)]>val2:
					for col in columnnames:
						if col in dictionary[table1]:
							print rows1[dictionary[table1].index(col)],
						else:
							print rows2[dictionary[table2].index(col)],
						check=1
					if check==1:
						check=0
						print
			elif flag1==1 and flag2==0:
#				print "entered 3rd case"
				if rows1[dictionary[table1].index(col1)]>val1 or rows2[dictionary[table2].index(col2)]<val2:
					for col in columnnames:
						if col in dictionary[table1]:
							print rows1[dictionary[table1].index(col)],
						else:
							print rows2[dictionary[table2].index(col)],
						check=1
					if check==1:
						check=0
						print 
			elif flag1==1 and flag2==1:
#					print "entered 4th case"
				if rows1[dictionary[table1].index(col1)]>val1 or rows2[dictionary[table2].index(col2)]>val2:
					for col in columnnames:
						if col in dictionary[table1]:
							print rows1[dictionary[table1].index(col)],
						else:
							print rows2[dictionary[table2].index(col)],
						check=1
					if check==1:
						check=0
						print

def processWhereAndQuery(columnnames,table1,col1,val1,table2,col2,val2,flag1,flag2):
# this function executes and operator in the where part of the query
	table1_name=table1+'.'+'csv'
	table2_name=table2+'.'+'csv'
	table1_data=read_data_frm_file(table1_name)
	table2_data=read_data_frm_file(table2_name)
#	print dictionary[table1].index(col1)
	print "Output:"
	string=""
	for col in columnnames:
		if col in dictionary[table1]:
			if not string == "":
				string+=','
			string+=table1+'.'+col
		else:
			if not string == "":
				string+=','
			string+=table2+'.'+col
	check=0
	for rows1 in table1_data:
#		print rows1
		for rows2 in table2_data:
#			print rows1[dictionary[table1].index(col1)]
			if flag1==0 and flag2==0 and rows1[dictionary[table1].index(col1)]<val1 and rows2[dictionary[table2].index(col2)]<val2:
#				print "entered 1st case"
				for col in columnnames:
					if col in dictionary[table1]:
						print rows1[dictionary[table1].index(col)],
					else:
						print rows2[dictionary[table2].index(col)],
					check=1
				if check==1:
					print
					check=0
			elif  flag1==0 and flag2==1 and rows1[dictionary[table1].index(col1)]<val1 and rows2[dictionary[table2].index(col2)]>val2:
#				print "entered 2nd case"
				for col in columnnames:
					if col in dictionary[table1]:
						print rows1[dictionary[table1].index(col)],
					else:
						print rows2[dictionary[table2].index(col)],
					check=1
				if check==1:
					check=0
					print 
			elif flag1==1 and flag2==0 and rows1[dictionary[table1].index(col1)]>val1 and rows2[dictionary[table2].index(col2)]<val2:
#				print "entered 3rd case"
				for col in columnnames:
					if col in dictionary[table1]:
						print rows1[dictionary[table1].index(col)],
					else:
						print rows2[dictionary[table2].index(col)],
					check=1
				if check==1:
					check=0
					print 
			elif flag1==1 and flag2==1 and rows1[dictionary[table1].index(col1)]>val1 and rows2[dictionary[table2].index(col2)]>val2:
#					print "entered 4th case"
				for col in columnnames:
					if col in dictionary[table1]:
						print rows1[dictionary[table1].index(col)],
					else:
						print rows2[dictionary[table2].index(col)],
					check=1
				if check==1:
					check=0
					print

def processQuery(query):
	if 'from' in query:				# checking from in the query
		object1=query.split('from')
	else:
		print("Incorrect syntax")
	object1[0]=re.sub(' +',' ',object1[0]).strip()
	if 'select' not in object1[0].lower():		#checking for select in the query
		print('Incorrect syntax')
	obj1=object1[0][7:]
	obj1=re.sub(' +',' ',obj1).strip()
	object1[1]=re.sub(' +',' ',object1[1]).strip()
	obj2=object1[1].split('where')
	tablestr=obj2[0]
	tablestr=re.sub(' +',' ',tablestr).strip()
	tablenames=tablestr.split(',')
	for i in tablenames:
		tablenames[tablenames.index(i)]=re.sub(' +',' ',i).strip()
		if i not in dictionary.keys():
			print "%s not found" % (i)			# if table not found then it exit
			del	tablenames[tablenames.index(i)]	
	columnnames=[]
	file_name=""
	if len(tablenames)==1 and len(obj2)==1:
#		print "entered"
		if '*' in object1[0]:				# selecting all columns of a table with no where clause
			columnnames=dictionary[tablestr]
#			print columnnames
			file_name+=tablestr+'.csv'
#			print file_name
			data=read_data_frm_file(file_name)
			printoutput(data,columnnames,tablenames)
		elif '(' not in obj1 and ')' not in obj1:		# selecting listed columns of a table with no where clause
			columnstr=obj1
			columnstr=re.sub(' +',' ',columnstr).strip()
			columnnames=columnstr.split(',')
			for col in columnnames:
				if col not in dictionary[tablenames[0]]:
					print "%s column not found in table" %col
					del columnnames[columnnames.index(col)]
#			print columnnames
			file_name+=tablestr+'.csv'
			data=read_data_frm_file(file_name)
			if len(columnnames)>=1:
				printoutput(data,columnnames,tablenames)
		elif '(' in obj1 and ')' in obj1:			# aggregate function is extracted along with attribute name of a table
#			print "entered"
#			count=0
			funcname=""
			colname=""
			columnstr=obj1
#			print type(columnstr)
			columnstr=re.sub(' +',' ',columnstr).strip()			
			columnnames=columnstr.split(' ')
#			print columnnames
			for col in columnnames:
				if '(' in col and ')' in col:
					a1 = col.split('(');
					funcname = (re.sub(' +',' ',a1[0])).strip()
					colname = (re.sub(' +',' ',a1[1].split(')')[0])).strip()
#					print funcname
#					print colname
					colname=colname.split(',')
#					print len(colname)
#					print colname
					if len(colname)==1:
						colname=''.join(colname)
						func(funcname,colname,tablenames[0])
					else:
#						print "entered"
						distinctMany(colname,tablenames[0])		# multiple distinct columns are executed
					return
	elif len(tablenames)>1 and len(obj2)==1:
#		print "entered"
		data=join(tablenames)
		check=0
		columnnames=obj1.split(',')
		print len(tablenames[0])
		for rows in data:
#			print len(rows)
			for col in columnnames:
				if col in dictionary[tablenames[0]]:
#					print "entered 1st case"
					print rows[dictionary[tablenames[0]].index(col)],
					check=1
				else:
#					print "entered 2nd case"
#					print len(tablenames[0])+dictionary[tablenames[1]].index(col)
					print rows[len(dictionary[tablenames[0]])+dictionary[tablenames[1]].index(col)],
					check=1
			if check==1:
				check=0
				print
	elif len(obj2)>1:		# condition for existence of where clause in the query
		if len(tablenames)>1:
			string=""
			data=join(tablenames)	# if more than one table present then join it
			if '*' in object1[0]:	# if all attributes are asked to be displayed
				for table in tablenames:
					columnnames=dictionary[table]
					for col in columnnames:
						if not string == "":
							string+=','
						string+=table+'.'+col
				print string
			else:
				columnnames=obj1.split(',')		# only limited attribute are asked to display
				for col in columnnames:
					print col
					if col in dictionary[tablenames[0]] or col in dictionary[tablenames[1]]:
						if not string == "":
						 	string+=','
						if col in dictionary[tablenames[0]]:
							string+=tablenames[0]+'.'+col
						if col in dictionary[tablenames[1]]:
							string+=tablenames[1]+'.'+col
					else:
						print('column not found in the table') 	
				print string
			obj2[1]=re.sub(' +',' ',obj2[1]).strip()
			if 'and' not in obj2[1].lower() and 'or' not in obj2[1].lower():	# joining condition of two tables
				obj2[1]=re.sub(' +',' ',obj2[1]).strip()
#				print obj2[1]
				where_query=obj2[1].split('=')
#				print where_query
				where_query[0]=re.sub(' +',' ',where_query[0]).strip()
				query1=where_query[0].split('.')
				t1=query1[0]
				if t1 not in dictionary:
					print('table not found')
				c1=query1[1]
				if c1 not in dictionary[t1]:
					print('column not found in table')
				where_query[1]=re.sub(' +',' ',where_query[1]).strip()
				query2=where_query[1].split('.')
				t2=query2[0]
				if t2 not in dictionary:
					print('table not found')
				c2=query2[1]
				if c2 not in dictionary[t2]:
					print('column not found in the table')
				tablename=t1+c1+t2+c2
				dictionary[tablename]=[]
				dictionary[tablename].extend(dictionary[t1])
				dictionary[tablename].extend(dictionary[t2])
#				print dictionary[tablename]
#				print tablename
#				print type(t1)
				temp=[]
				check=0
				for rows in data:
					if '*' in object1[0]:
						if rows[dictionary[t1].index(c1)] == rows[dictionary[t2].index(c2)+len(dictionary[t1])]: 
							if rows not in temp:
								temp.append(rows)
								print rows,
								check=1
					elif '*' not in object1[0]:
						if rows[dictionary[t1].index(c1)] == rows[dictionary[t2].index(c2)+len(dictionary[t1])]:
							x=[]
							for col in columnnames:
								if col in dictionary[t1]:
									x.append(rows[dictionary[t1].index(col)])
								else:
									x.append(rows[dictionary[t2].index(col)+len(dictionary[t1])])
							if x not in temp:
								temp.append(x)
								print x
								check=1
					if check==1:
						check=0
						print
			else:											# and and or operator present in the where part of the query with multiple tables 
				obj2[1]=re.sub(' +',' ',obj2[1]).strip()
				if 'and' in obj2[1]:
					queries=obj2[1].split(' and ')
					queries[0]=re.sub(' +',' ',queries[0]).strip()
					queries[1]=re.sub(' +',' ',queries[1]).strip()
					flag1=0
					flag2=0
# but attributes are compared with numerical value					
					if '>' in queries[0]:
#						print "entered 1st case"
						flag1=1
						query1=queries[0].split('>')
						val1=query1[1]
						query1[0]=re.sub(' +',' ',query1[0]).strip()
						query1=query1[0].split('.')
						table1=query1[0]
						col1=query1[1]
						if col1 not in dictionary[table1]:
							print('column not found in table')
						if table1 not in dictionary:
							print('table not found')
					if '>' in queries[1]:
#						print "entered 2nd case"
						flag2=1
						query2=queries[1].split('>')
						val2=query2[1]
						query2[0]=re.sub(' +',' ',query2[0]).strip()
						query2=query2[0].split('.')
						table2=query2[0]
						col2=query2[1]
						if col2 not in dictionary[table2]:
							print('column not found in table')
						if table2 not in dictionary:
							print('table not found')
					if '<' in queries[0]:
#						print "entered 3rd case"
						query1=queries[0].split('<')
						val1=query1[1]
						query1[0]=re.sub(' +',' ',query1[0]).strip()
						query1=query1[0].split('.')
						table1=query1[0]
						col1=query1[1]
						if col1 not in dictionary[table1]:
							print('column not found in table')
						if table1 not in dictionary:
							print('table not found')
					if '<' in queries[1]:
#						print "entered 4th case"
						query2=queries[1].split('<')
						val2=query2[1]
						query2[0]=re.sub(' +',' ',query2[0]).strip()
						query2=query2[0].split('.')
						table2=query2[0]
						col2=query2[1]
						if col2 not in dictionary[table2]:
							print('column not found in table')
						if table2 not in dictionary:
							print('table not found')
						table2=query2[0]
						col2=query2[1]
					processWhereAndQuery(columnnames,table1,col1,val1,table2,col2,val2,flag1,flag2)
				else:
					queries=obj2[1].split(' or ')
					queries[0]=re.sub(' +',' ',queries[0]).strip()
					queries[1]=re.sub(' +',' ',queries[1]).strip()
					flag1=0
					flag2=0
					if '>' in queries[0]:
#						print "entered 1st case"
						flag1=1
						query1=queries[0].split('>')
						val1=query1[1]
						query1[0]=re.sub(' +',' ',query1[0]).strip()
						query1=query1[0].split('.')
						table1=query1[0]
						col1=query1[1]
						if col1 not in dictionary[table1]:
							print('column not found in table')
						if table1 not in dictionary:
							print('table not found')
					if '>' in queries[1]:
#						print "entered 2nd case"
						flag2=1
						query2=queries[1].split('>')
						val2=query2[1]
						query2[0]=re.sub(' +',' ',query2[0]).strip()
						query2=query2[0].split('.')
						table2=query2[0]
						col2=query2[1]
						if col2 not in dictionary[table2]:
							print('column not found in table')
						if table2 not in dictionary:
							print('table not found')
					if '<' in queries[0]:
#						print "entered 3rd case"
						query1=queries[0].split('<')
						val1=query1[1]
						query1[0]=re.sub(' +',' ',query1[0]).strip()
						query1=query1[0].split('.')
						table1=query1[0]
						col1=query1[1]
						if col1 not in dictionary[table1]:
							print('column not found in table')
						if table1 not in dictionary:
							print('table not found')
					if '<' in queries[1]:
#						print "entered 4th case"
						query2=queries[1].split('<')
						val2=query2[1]
						query2[0]=re.sub(' +',' ',query2[0]).strip()
						query2=query2[0].split('.')
						table2=query2[0]
						col2=query2[1]
						if col2 not in dictionary[table2]:
							print('column not found in table')
						if table2 not in dictionary:
							print('table not found')
						table2=query2[0]
						col2=query2[1]
					processWhereOrQuery(columnnames,table1,col1,val1,table2,col2,val2,flag1,flag2)


		else:								# and and or operator in where part of the query with only one table
			columnnames=obj1.split(',')
			print "Output :"
			string=""
			for col in columnnames:
				if col in dictionary[tablenames[0]]:
					if not string == "":
						string+=','
					string+=tablenames[0]+'.'+col
			print string
			file_name=tablenames[0]+'.csv'
			data=read_data_frm_file(file_name)
			obj2[1]=re.sub(' +',' ',obj2[1]).strip()
			if 'and' not in obj2[1] and 'or' not in obj2[1]:
				queries=obj2[1].split('=')
				val1=queries[1]
				col1=queries[0]
				for rows in data:
					if rows[dictionary[tablenames[0]].index(col1)]==val1:
						for col in columnnames:
							print rows[dictionary[tablenames[0]].index(col)],
							check=1
						if check==1:
							check=0
							print
			elif 'and' in obj2[1]:
				queries=obj2[1].split(' and ')
				queries[0]=re.sub(' +',' ',queries[0]).strip()
				queries[1]=re.sub(' +',' ',queries[1]).strip()
				flag1=0
				flag2=0
				if '=' in queries[0] and '=' in queries[1]:
					query1=queries[0].split('=')
					val1=query1[1]
					col1=query1[0]
					query2=queries[1].split('=')
					val2=query2[1]
					col2=query2[0]
					for rows in data:
						if rows[dictionary[tablenames[0]].index(col1)]==val1 and rows[dictionary[tablenames[0]].index(col2)]==val2:
							for col in columnnames:
								print rows[dictionary[tablenames[0]].index(col)],
								check=1
							if check==1:
								check=0
								print
				else:
					if '>' in queries[0]:
#							print "entered 1st case"
						flag1=1
						query1=queries[0].split('>')
						val1=query1[1]
						col1=query1[0]
						if col1 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
					if '>' in queries[1]:
#							print "entered 2nd case"
						flag2=1
						query2=queries[1].split('>')
						val2=query2[1]
						col2=query2[0]
						if col2 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
					if '<' in queries[0]:
#							print "entered 3rd case"
						query1=queries[0].split('<')
						val1=query1[1]
						col1=query1[0]
						if col1 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
					if '<' in queries[1]:
#							print "entered 4th case"
						query2=queries[1].split('<')
						val2=query2[1]
						col2=query2[0]
						if col2 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
#					print col1,val1,col2,val2
					check=0
					for rows in data:
#						print rows
						if flag1==0 and flag1==0 and rows[dictionary[tablenames[0]].index(col1)]<val1 and rows[dictionary[tablenames[0]].index(col2)]<val2:
#							print "entered 1st case"
							for col in columnnames:
								print rows[dictionary[tablenames[0]].index(col)],
								check=1
							if check==1:
								check=0
								print
						elif flag1==0 and flag1==1 and rows[dictionary[tablenames[0]].index(col1)]<val1 and rows[dictionary[tablenames[0]].index(col2)]>val2:
#							print "entered 2nd case"
							for col in columnnames:
								print rows[dictionary[tablenames[0]].index(col)],
								check=1
							if check==1:
								check=0
								print
						elif flag1==1 and flag2==0 and rows[dictionary[tablenames[0]].index(col1)]>val1 and rows[dictionary[tablenames[0]].index(col2)]<val2:
#							print "entered 3rd case"
							for col in columnnames:
								print rows[dictionary[tablenames[0]].index(col)],
								check=1
							if check==1:
								check=0
								print
						elif flag1==1 and flag2==1 and rows[dictionary[tablenames[0]].index(col1)]>val1 and rows[dictionary[tablenames[0]].index(col2)]>val2:
#							print "entered 4th case"
							for col in columnnames:
								print rows[dictionary[tablenames[0]].index(col)],
								check=1
							if check==1:
								check=0
								print
			elif 'or' in obj2[1]:
#				print "entered"
				queries=obj2[1].split(' or ')
				queries[0]=re.sub(' +',' ',queries[0]).strip()
				queries[1]=re.sub(' +',' ',queries[1]).strip()
				flag1=0
				flag2=0
				if '=' in queries[0] and '=' in queries[1]:
					query1=queries[0].split('=')
					val1=query1[1]
					col1=query1[0]
					query2=queries[1].split('=')
					val2=query2[1]
					col2=query2[0]
					for rows in data:
						if rows[dictionary[tablenames[0]].index(col1)]==val1 or rows[dictionary[tablenames[0]].index(col2)]==val2:
							for col in columnnames:
								print rows[dictionary[tablenames[0]].index(col)],
								check=1
							if check==1:
								check=0
								print
				else:
					if '>' in queries[0]:
#							print "entered 1st case"
						flag1=1
						query1=queries[0].split('>')
						val1=query1[1]
						col1=query1[0]
						if col1 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
					if '>' in queries[1]:
#							print "entered 2nd case"
						flag2=1
						query2=queries[1].split('>')
						val2=query2[1]
						col2=query2[0]
						if col2 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
					if '<' in queries[0]:
#							print "entered 3rd case"
						query1=queries[0].split('<')
						val1=query1[1]
						col1=query1[0]
						if col1 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
					if '<' in queries[1]:
#							print "entered 4th case"
						query2=queries[1].split('<')
						val2=query2[1]
						col2=query2[0]
						if col2 not in dictionary[tablenames[0]]:
							print('column not found in table')
						if tablenames[0] not in dictionary:
							print('table not found')
#					print col1,val1,col2,val2
					check=0
					for rows in data:
#						print rows
						if flag1==0 and flag1==0: 
#							print "entered 1st case"
							if rows[dictionary[tablenames[0]].index(col1)]<val1 or rows[dictionary[tablenames[0]].index(col2)]<val2:
								for col in columnnames:
									print rows[dictionary[tablenames[0]].index(col)],
									check=1
								if check==1:
									check=0
									print
						elif flag1==0 and flag1==1: 
#							print "entered 2nd case"
							if rows[dictionary[tablenames[0]].index(col1)]<val1 or rows[dictionary[tablenames[0]].index(col2)]>val2:
								for col in columnnames:
									print rows[dictionary[tablenames[0]].index(col)],
									check=1
								if check==1:
									check=0
									print
						elif flag1==1 and flag2==0: 
#							print "entered 3rd case"
							if rows[dictionary[tablenames[0]].index(col1)]>val1 or rows[dictionary[tablenames[0]].index(col2)]<val2:
								for col in columnnames:
									print rows[dictionary[tablenames[0]].index(col)],
									check=1
								if check==1:
									check=0
									print
						elif flag1==1 and flag2==1: 
#							print "entered 4th case"
							if rows[dictionary[tablenames[0]].index(col1)]>val1 or rows[dictionary[tablenames[0]].index(col2)]>val2:
								for col in columnnames:
									print rows[dictionary[tablenames[0]].index(col)],
									check=1
								if check==1:
									check=0
									print		

def join(tablenames):			# this function executes joining of two tables
	file1=tablenames[0]+'.csv'
	file2=tablenames[1]+'.csv'
	file1_data=read_data_frm_file(file1)
	file2_data=read_data_frm_file(file2)
	temp=[]
	for data1 in file1_data:
		for data2 in file2_data:
				temp.append(data1+data2)
	return temp
				
if __name__ == "__main__":				# main function
	global dictionary
	dictionary=dict()
	attr_file=open('metadata.txt','rb')
	flag=0
	for line in attr_file:
		if line.strip() == "<begin_table>":
			flag=1
			continue
		if flag==1:
			tablename=line.strip()
			dictionary[tablename]=[]
			flag=0
			continue
		if line.strip()!= "<end_table>":
#			print line.strip()
			dictionary[tablename].append(line.strip())
#	for keys in dictionary.keys():
#		print dictionary[keys]
	print 'Type "quit"  to exit.'
	while(1):							# queries will be asked till quit is not entered
		query=raw_input('PROMPT> ')
		if query == 'quit':
			sys.exit()
#			query=str(sys.argv[1])
		processQuery(query)