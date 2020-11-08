#This program calculates the total amount of airline tickets paid by Correios, a brazilian state-owned mail delivery company,
#to some of their employees
import requests, os, bs4, re, pyexcel_ods

"""DOWNLOAD FILES"""
url = "https://www.correios.com.br/acesso-a-informacao/despesas-1/arquivos"
os.makedirs('C:\\Users\\Gui\\Desktop\\MyPythonScripts\\ods_files', exist_ok=True)
res = requests.get(url) #Request for page using request module
res.raise_for_status() #Check for errors
soup = bs4.BeautifulSoup(res.text, "html.parser") #Parse page using beautiful soup module
links = soup.find_all(href=re.compile("passagens-aereas")) #Find all hrefs with name "passagens-aereas"
fileNameRegex = re.compile(r'passagens-[^/]*') #Build regex for naming downloaded files correctly
for link in links:
	res = requests.get(link["href"])
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	files = soup.find_all(href=re.compile("/at_download/file")) #Find downlaodable links
	if files:
		print("Downloading: ",end="")
		print(files[0]["href"])
		res = requests.get(files[0]["href"]) #Download files
		res.raise_for_status()
		fileName = fileNameRegex.search(files[0]["href"])
		excelFile = open("C:\\Users\\Gui\\Desktop\\MyPythonScripts\\ods_files\\" + fileName.group() + ".ods", "wb") #Create a file to store what we've downloaded
		for chunk in res.iter_content(100000): #As we're downloading .ods files we need to read in bytes and save in bytes chunk by chunk
			excelFile.write(chunk)
		excelFile.close() #Close the builded file

"""SUM THE TOTAL PAID"""   
files = os.listdir("C:\\Users\\Gui\\Desktop\\MyPythonScripts\\ods_files") #List all files in the directory
total = 0 #Sum of all files
for file in files:
	data = pyexcel_ods.get_data("C:\\Users\\Gui\\Desktop\\MyPythonScripts\\ods_files\\" + file) #Open .ods file
	key = data.keys()
	key = list(key)
	sheet = data[key[0]] #Get sheet by key
	sheet = sheet[1:] #Ignore the first line of the file
	fileTotal = 0 #Sum of current file
	for line in sheet:
		if line:
			fileTotal += float(line[4])
	print("Total in " + str(file) + " is " + str(fileTotal)) #Give feedback
	total += fileTotal
print("Total amount is: " + str(total)) #Print result