#trying conversion from xml to pandas dictionary
import os
import glob

# file = os.listdir("./xml/")
d = {}
eligibility = None
file = glob.glob("xml/*")
for i in range(len(file)):
    try:
        parsedXML = et.parse(file[i])
        if parsedXML is not None:
            for node in parsedXML.getroot():
                if node is not None:
                    if node.tag == "id_info":
                        for child in node:
                            if child is not None:
                                if child.tag == "nct_id":
                                    index = child.text
                    if node.tag == "eligibility":
                        if node[0][0] is not None and node[0][0].text is not None:
                            eligibility = node[0][0].text
#                             print index
#                             print node[0][0].text
                    if eligibility is not None:
                        d[index] = eligibility
    except:
        d[index] = "N/A"
        continue
mypath = "parsed_files/"
if not os.path.isdir(mypath):
   os.makedirs(mypath)
for key,value in d.items():
    fileName = mypath+key+".txt"
    print(os.path.abspath(fileName))
    f = open(fileName, "w")
    f.write(value)
    f.close()
