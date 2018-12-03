import bs4 as bs
import urllib.request
import re
import os.path
import numpy as np
import os
import time
from os import listdir
from os.path import isfile, isdir, join
from pathlib import Path

DIR_PROJECT=Path(os.getcwd()).parent
DIR_INPUT=os.path.join(DIR_PROJECT,'Data','Input')
DIR_OUTPUT=os.path.join(DIR_PROJECT,'Data','Output')


InputFiles = listdir(DIR_INPUT)

print('get rs number from the input file')
for file in InputFiles:
    rsNumList = []
    FileFullPath = join(DIR_INPUT, file)
    # open input file.
    InFile = open(FileFullPath, 'r')
    # read data from the file.
    while True:
        line = InFile.readline()
        if not line:
            break
        else:
            # first, parse tab , and then remove '\n'
            rsNumList.append(line.split('\t')[1].split()[0])
    InFile.close()

#####################################################################

# the target website -> NCBI
WEBSITE_ADDRESS='https://www.ncbi.nlm.nih.gov/snp/'
# define the std of genome database
GENOME_STD="GRCh37"
# define the output file path
OutputFilePath=os.path.join(DIR_OUTPUT,"QueryResult_{0}.{1}".format(GENOME_STD,"tsv"))


for rsNum in rsNumList:
    try:
        sauce = urllib.request.urlopen("{0}{1}".format(WEBSITE_ADDRESS, rsNum)).read()
        # remember to install "lxml" for parse information
        soup = bs.BeautifulSoup(sauce, 'lxml')
        table = soup.find('table')
        table_rows = table.find_all('tr')
        regExform = r"{0}.*".format(GENOME_STD)
        regExform2 = r"({0}).[\w]+\s(.*)".format(GENOME_STD)

        data = []
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            for idx in range(int(row.__len__() / 2)):
                if (re.findall(regExform, row[2 * idx])):
                    for yy in re.findall(regExform, row[2 * idx]):
                        data.append(yy)
                    data.append(row[2 * idx + 1])
            for xx in data:
                print(xx+'\t',end="")
        print("")
    except:
        # fp.writelines("{0} not found data\n".format(num))
        print("{0} not found data".format(rsNum))


