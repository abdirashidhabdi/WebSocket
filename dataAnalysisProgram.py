#!/usr/bin/env python3
''' 
	Program name:	dataAnalysisProgram.py
	Developed by:	Abdirashid Abdi


''' 
import urllib.request
import csv
import json

def main():
	''' Call function to download the csv file from url '''
	downloadCsvFromUrl()
	
	''' Call the function that converts the csv file to a list of dictionaries '''
	listDict = csvToDictList()
	
	''' Call the function that stores the dictionary keys to list '''
	keysList = locationNames(listDict)
	print("There are ", len(keysList), " location names in the keysList which make up the total locations in the csv file.")
	
	''' Call the function that returns a tuple with lists of records for different locations '''
	footfallRecords = locationRecords(listDict, keysList)
	recordsList = []		# Empty list
	for i in footfallRecords:	# Loop through the tuple
		recordsList.append(i)	# Append to the list
	
	''' Dictionary with 23 key value pairs where: Key – is the location & Value – list with the average and the highest footfall for that location'''
	avMaxDict = {keysList[0]: [findAverage(recordsList[0]), findMaxValue(recordsList[0])], keysList[1]: [findAverage(recordsList[1]),findMaxValue(recordsList[1])], keysList[2]: [findAverage(recordsList[2]),findMaxValue(recordsList[2])], keysList[3]: [findAverage(recordsList[3]),findMaxValue(recordsList[3])], keysList[4]: [findAverage(recordsList[4]),findMaxValue(recordsList[4])], keysList[5]: [findAverage(recordsList[5]),findMaxValue(recordsList[5])], keysList[6]: [findAverage(recordsList[6]),findMaxValue(recordsList[6])], keysList[7]: [findAverage(recordsList[7]),findMaxValue(recordsList[7])], keysList[8]: [findAverage(recordsList[8]),findMaxValue(recordsList[8])], keysList[9]: [findAverage(recordsList[9]),findMaxValue(recordsList[9])], keysList[10]: [findAverage(recordsList[10]),findMaxValue(recordsList[10])], keysList[11]: [findAverage(recordsList[11]),findMaxValue(recordsList[11])], keysList[12]: [findAverage(recordsList[12]),findMaxValue(recordsList[12])], keysList[13]: [findAverage(recordsList[13]),findMaxValue(recordsList[13])], keysList[14]: [findAverage(recordsList[14]),findMaxValue(recordsList[14])], keysList[15]: [findAverage(recordsList[15]),findMaxValue(recordsList[15])], keysList[16]: [findAverage(recordsList[16]),findMaxValue(recordsList[16])], keysList[17]: [findAverage(recordsList[17]),findMaxValue(recordsList[17])], keysList[18]: [findAverage(recordsList[18]),findMaxValue(recordsList[18])], keysList[19]: [findAverage(recordsList[19]),findMaxValue(recordsList[19])], keysList[20]: [findAverage(recordsList[20]),findMaxValue(recordsList[20])], keysList[21]: [findAverage(recordsList[21]),findMaxValue(recordsList[21])], keysList[22]: [findAverage(recordsList[22]),findMaxValue(recordsList[22])]}
	
	''' Call the function to write the dictionary data out to a JSON file '''
	writeToJson(avMaxDict)
	
	''' Calculate & display the location with the highest recorded footfall '''
	highestFfRecord = max(avMaxDict, key= lambda dictKey0: avMaxDict[dictKey0][1])
	print("The location with the highest footfall recorded is: ", highestFfRecord)

	''' Calculate & display the location with the highest average recorded footfall'''
	highestAvFfRecord = max(avMaxDict, key= lambda dictKey: avMaxDict[dictKey]) 
	print("The location with the highest average footfall recorded is: ", highestAvFfRecord)

''' ################################################# END OF MAIN FUNCTION ########################################################### '''	

# Function to download the CSV file
def downloadCsvFromUrl():
	url = "https://data.smartdublin.ie/dataset/cc421859-1f4f-43f6-b349-f4ca0e1c60fa/resource/3048794e-16bd-4edb-9ba9-8018a6aadcdb/download/jansept-2020-footfall-counts.csv"
	# Try block
	try:
		response = urllib.request.urlopen(url)				# Open the url entered
		alldata = response.read().decode('utf-8')				# Read the source code of the website and decode it
		fptr = open("downloadedData.csv","w", encoding="utf-8")		# Open a new file named downloadedData.csv to write to
		fptr.write(alldata)							# Write the content of the source code into the file
		fptr.close()                                    			# Close the downloadedData.csv file
	# Except block
	except:
		print("Sorry! The csv file was not downloaded successfully!")	# Display this message on screen

# Function to convert CSV to lists of dictionaries
def csvToDictList():
	csvRead = open("downloadedData.csv","r")					# Open csv file for reading 
	csvToDict = csv.DictReader(csvRead)						# Convert csv data to dictionary
	listDict = list(csvToDict)							# Dictionary to list
	csvRead.close()								# Close csv file
	return listDict								# Return list of dictionaries

# Function to extract location names
def locationNames(listDict):	
	Dict1 = listDict[0]								# Store first dictionary data from the passed list of dictionaries
	
	keysList = []									# Empty list
	for key, value in Dict1.items():
		if key != 'Date & Time':						# Check if dictionary key is not equal to Date & Time
			keysList.append(key)						# Append to the list
	return keysList

# Function to store records to the relevant location
def locationRecords(listDict, keysList):	
	
	''' Empty lists '''
	location1 = []
	location2 = []
	location3 = []
	location4 = []
	location5 = []
	location6 = []
	location7 = []
	location8 = []
	location9 = []
	location10 = []
	location11 = []
	location12 = []
	location13 = []
	location14 = []
	location15 = []
	location16 = []
	location17 = []
	location18 = []
	location19 = []
	location20 = []
	location21 = []
	location22 = []
	location23 = []
	
	# Loop through lists of dictionaries
	for i in listDict:
		for key, val in i.items():
			if key == keysList[0]:						# Check if key is equal to what is in index 0 of keysList
				location1.append(val)					# If true, then append its value to location1 list
			elif key == keysList[1]:					# Check if key is equal to what is in index 1 of keysList
				location2.append(val)					# If true, then append its value to location2 list
			elif key == keysList[2]:					# Check if key is equal to what is in index 2 of keysList
				location3.append(val)					# If true, then append its value to location3 list
			elif key == keysList[3]:					# Check if key is equal to what is in index 3 of keysList
				location4.append(val)					# If true, then append its value to location4 list
			elif key == keysList[4]:					# Check if key is equal to what is in index 4 of keysList
				location5.append(val)					# If true, then append its value to location5 list
			elif key == keysList[5]:					# Check if key is equal to what is in index 5 of keysList
				location6.append(val)					# If true, then append its value to location6 list
			elif key == keysList[6]:					# Check if key is equal to what is in index 6 of keysList
				location7.append(val)					# If true, then append its value to location7 list
			elif key == keysList[7]:					# Check if key is equal to what is in index 7 of keysList
				location8.append(val)					# If true, then append its value to location8 list
			elif key == keysList[8]:					# Check if key is equal to what is in index 8 of keysList
				location9.append(val)					# If true, then append its value to location9 list
			elif key == keysList[9]:					# Check if key is equal to what is in index 9 of keysList
				location10.append(val)					# If true, then append its value to location10 list
			elif key == keysList[10]:					# Check if key is equal to what is in index 10 of keysList
				location11.append(val)					# If true, then append its value to location11 list
			elif key == keysList[11]:					# Check if key is equal to what is in index 11 of keysList
				location12.append(val)					# If true, then append its value to location12 list
			elif key == keysList[12]:					# Check if key is equal to what is in index 12 of keysList
				location13.append(val)					# If true, then append its value to location13 list
			elif key == keysList[13]:					# Check if key is equal to what is in index 13 of keysList
				location14.append(val)					# If true, then append its value to location14 list
			elif key == keysList[14]:					# Check if key is equal to what is in index 14 of keysList
				location15.append(val)					# If true, then append its value to location15 list
			elif key == keysList[15]:					# Check if key is equal to what is in index 15 of keysList
				location16.append(val)					# If true, then append its value to location16 list
			elif key == keysList[16]:					# Check if key is equal to what is in index 16 of keysList
				location17.append(val)					# If true, then append its value to location17 list
			elif key == keysList[17]:					# Check if key is equal to what is in index 17 of keysList
				location18.append(val)					# If true, then append its value to location18 list
			elif key == keysList[18]:					# Check if key is equal to what is in index 18 of keysList
				location19.append(val)					# If true, then append its value to location19 list
			elif key == keysList[19]:					# Check if key is equal to what is in index 19 of keysList
				location20.append(val)					# If true, then append its value to location20 list
			elif key == keysList[20]:					# Check if key is equal to what is in index 20 of keysList
				location21.append(val)					# If true, then append its value to location21 list
			elif key == keysList[21]:					# Check if key is equal to what is in index 21 of keysList
				location22.append(val)					# If true, then append its value to location22 list
			elif key == keysList[22]:					# Check if key is equal to what is in index 22 of keysList
				location23.append(val)					# If true, then append its value to location23 list
			else:
				pass							# Otherwise pass
	return (location1, location2, location3, location4, location5, location6, location7, location8, location9, location10, location11, location12, location13, location14, location15, location16, location17, location18, location19, location20, location21, location22, location23)

# Function to find average value
def findAverage(location):
	nonEmptyData = []								# Empty list
	for i in location:
		if i != '':								# Check if i is not empty
			nonEmptyData.append(int(i))					# If true, append it to list
	
	# Calculate average
	average = sum(nonEmptyData) / len(nonEmptyData) if nonEmptyData else 0
	return round(average, 2)

# Function to find maximum value
def findMaxValue(location):
	maxVal = 0									# Variable to store maximum value
	for item in location:
        	if item != '':								# Check if item is not empty
        		if int(item) > maxVal:						# Check if item is greater than what's in maxVal
            			maxVal = int(item)					# If true, then store item in maxVal
	return maxVal

# Function to write to json file
def writeToJson(dataDict):
	with open("avMaxJson.json", "w") as fptr:					# Open file for writing
		json.dump(dataDict, fptr)						# Write dictionary data out to a json file

if __name__ == "__main__":
	main()
