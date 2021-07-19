	'''
	Implement Naive Bayes.
	
	'''
	import csv
	import random
	import math
	import sys

	def cal_p(sample,mean,variance):
		exponent=-((sample-mean)**2)/(2*variance)
		term1 = 1.0/math.sqrt(2 * math.pi*variance)
		term2 = math.exp(exponent)
		return term1 * term2

	ht_m = ht_f =0
	wt_m = wt_f  = 0
	fts_m = fts_f  = 0
	count_m = count_f  = 0

	f=open('data.csv','rb')	#open csv file in read mode
	reader = csv.reader(f)

	for row in reader:
		if row[0]!="Sex":
			if row[0]=='male':
				ht_m=ht_m+float(row[1])
				wt_m=wt_m+int(row[2])
				fts_m=fts_m+int(row[3])
				count_m =count_m+1


			elif row[0]=='female':
				ht_f=ht_f+float(row[1])
				wt_f=wt_f+int(row[2])
				fts_f=fts_f+int(row[3])
				count_f =count_f+1
	f.close()

	total_count=count_m + count_f 		#Total no of people
	pm=float(count_m)/total_count		#probablity of male sex 
	pf=float(count_f)/total_count		#probablity of female sex


	mean_ht_m=float(ht_m/count_m)		#calculate mean
	mean_ht_f=float(ht_f/count_f)


	mean_wt_m=float(wt_m/count_m)
	mean_wt_f=float(wt_f/count_f)


	mean_fts_m=float(fts_m/count_m)
	mean_fts_f=float(fts_f/count_f)


	ht_var_m = ht_var_f  = 0		#initialization
	wt_var_m = wt_var_f  = 0
	fts_var_m = fts_var_f = 0


	f=open('data.csv','rb')	#open csv file
	reader = csv.reader(f)

	for row in reader:
		if row[0]!="Sex":
			if row[0]=="male":
				ht_var_m=ht_var_m+(mean_ht_m-float(row[1]))**2
				wt_var_m=wt_var_m+(mean_wt_m-float(row[2]))**2
				fts_var_m=fts_var_m+(mean_fts_m-float(row[3]))**2
		

			elif row[0]=="female":
				ht_var_f=ht_var_f+(mean_ht_f-float(row[1]))**2
				wt_var_f=wt_var_f+(mean_wt_f-float(row[2]))**2
				fts_var_f=fts_var_f+(mean_fts_f-float(row[3]))**2
		
	f.close()

	ht_var_m = ht_var_m/(count_m -1)		#calculate variance
	ht_var_f = ht_var_f/(count_f -1)


	wt_var_m = wt_var_m/(count_m -1)
	wt_var_f = wt_var_f/(count_f -1)


	fts_var_m = fts_var_m/(count_m -1)
	fts_var_f = fts_var_f/(count_f -1)



	print "The csv file data is :\n"
	f=open('data.csv','rb')	#open csv file in read mode
	reader = csv.reader(f)

	for row in reader:
		print row
	print
	print "Enter Test Data: \n"		#take input from user
	sample_ht=float(raw_input("Enter Height : "))
	sample_wt=int(raw_input("Enter Weight : "))
	sample_fts=int(raw_input("Enter Foot Size : "))
	

	p_ht_m= cal_p(sample_ht, mean_ht_m, ht_var_m)		#calculate posterior probability of male
	p_wt_m= cal_p(sample_wt, mean_wt_m, wt_var_m)
	p_fts_m= cal_p(sample_fts, mean_fts_m, fts_var_m)
	posterior_m= pm * p_ht_m * p_wt_m * p_fts_m

	p_ht_f= cal_p(sample_ht, mean_ht_f, ht_var_f)	#calculate posterior probability of female
	p_wt_f= cal_p(sample_wt, mean_wt_f, wt_var_f)
	p_fts_f= cal_p(sample_fts, mean_fts_f, fts_var_f)
	posterior_f= pf * p_ht_f * p_wt_f * p_fts_f

	print 
	
	if posterior_m > posterior_f:
		print "The Person is a male\n "
		with open('data.csv','a') as data:
			data.write('%s,%i,%i,%i\n' %("Male",sample_ht,sample_wt,sample_fts))

	else:
		print "The Person is female \n "
		with open('data.csv','a') as data:
			data.write('%s,%i,%i,%i\n' %("Female", sample_ht,sample_wt,sample_fts))

	print "The appended data in csv file is :\n"
	f=open('data.csv','rb')	#open csv file in read mode
	reader = csv.reader(f)

	for row in reader:
		print row

	data.close()


	'''
	PROGRAM OUTPUT :

	[ccoew@localhost ~]$ python nvb.py
	The csv file data is :

	['Sex', 'Height', 'Weight', 'Foot Size']
	['male', '6', '180', '12']
	['male', '5.92', '190', '11']
	['male', '5.58', '170', '12']
	['male', '5.92', '165', '10']
	['female', '5', '100', '6']
	['female', '5.5', '150', '8']
	['female', '5.42', '130', '7\t']
	['female', '5.75', '150', '9']
	['Female', '6', '130', '8']
	['Female', '7', '140', '10']
	['Male', '6', '170', '10']
	['Female', '6', '130', '8']
	['Female', '7', '180', '9']
	['Male', '6', '180', '9']
	['Female', '6', '140', '9']
	['Male', '6', '180', '9']
	['Female', '5', '163', '6']

	Enter Test Data: 

	Enter Height : 5.92
	Enter Weight : 165
	Enter Foot Size : 10

	The Person is a male
	 
	The appended data in csv file is :

	['Sex', 'Height', 'Weight', 'Foot Size']
	['male', '6', '180', '12']
	['male', '5.92', '190', '11']
	['male', '5.58', '170', '12']
	['male', '5.92', '165', '10']
	['female', '5', '100', '6']
	['female', '5.5', '150', '8']
	['female', '5.42', '130', '7\t']
	['female', '5.75', '150', '9']
	['Female', '6', '130', '8']
	['Female', '7', '140', '10']
	['Male', '6', '170', '10']
	['Female', '6', '130', '8']
	['Female', '7', '180', '9']
	['Male', '6', '180', '9']
	['Female', '6', '140', '9']
	['Male', '6', '180', '9']
	['Female', '5', '163', '6']
	['Male', '5', '165', '10']
	[ccoew@localhost ~]$ 



	'''
