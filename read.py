import os
#plan for restructuring for inheritance for different file types
class CSVReader(object):
    def __init__(self, directory, filetype):
        self.directory = directory
        self.filetype = filetype
        self.fileHeaders = []
    def readFiles(self):
        for filename in os.listdir(str(self.directory)):
            if filename.endswith('.' + str(self.filetype)):
                file = open(str(self.directory) + filename, 'r')
                header_line = file.readline()
                #incomplete portion
                #purpose is to create a new file if the headers do not match for a csv
                file_number = 1
                if(len(self.header_line) > 0):
                    if header_line in self.fileHeaders:
                        file_number += 1
                ###################################################################
                of = open('output' + str(file_number) + '.txt', 'a')
                self.fileHeaders.append(header_line)
                for line in file.readlines():
                    of.write(line)
                file.close()
                of.close()

inUse = True

while inUse:
    #tested with local directories. File should be entered with a trailing / ex: csv/
    directory = raw_input("Which directory would you like to use? ")
    filetype = raw_input("Which file type would you like to use? ")

    reader = CSVReader(directory, filetype)
    reader.readFiles()
    inUse = False
