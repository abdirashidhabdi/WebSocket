#!/usr/bin/env python3
''' 
	Program name:	TCPClientProgram.py
	Developed by:	Abdirashid Abdi


''' 
import socket
import json

def main():
	# Call runclient function
	runClient()

def runClient():
	# Set up client socket to connect to server
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect the socket to port 5000 of the listening server
	sockAddr = ("localhost", 5000)
	clientSock.connect(sockAddr)
	# Message to be sent
	messageSent ="https://data.smartdublin.ie/dataset/cc421859-1f4f-43f6-b349-f4ca0e1c60fa/resource/3048794e-16bd-4edb-9ba9-8018a6aadcdb/download/jan-sept-2020-footfall-counts.csv"
	
	# Convert the message string to bytes
	messageBytes = messageSent.encode("utf-8")
	
	# Send data to server
	clientSock.send(messageBytes)
	
	# Receive data from server
	dataReceived = clientSock.recv(65535)
	jsonDataReceived = dataReceived.decode("utf-8")
	
	
	# Convert JSON to Dictionary
	jsonToDict = json.loads(jsonDataReceived)
	
	# Convert Dictionary to Json
	writeToJson(jsonToDict)
	
	# Calculate & display the location with the highest average recorded footfall
	highestAvFfRecord = max(jsonToDict, key= lambda dictKey: jsonToDict[dictKey]) 
	print("The location with the highest average footfall recorded is: ", highestAvFfRecord)
	
	# Calculate & display the location with the highest recorded footfall
	highestFfRecord = max(jsonToDict, key= lambda dictKey0: jsonToDict[dictKey0][1])
	print("The location with the highest footfall recorded is: ", highestFfRecord)
	
	# Close connection to the server
	clientSock.close()
	
def writeToJson(dataDict):
	with open("jsonFromClient.json", "w") as fptr:
		json.dump(dataDict, fptr)

if __name__ == "__main__":
	main()
