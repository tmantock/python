import os
#plan for restructuring for inheritance for different file types
class Write(object):
    def __init__(self, directory, filetype):
        self.directory = directory
        self.filetype = filetype
    def readToWriteFiles(self):
        for filename in os.listdir(str(self.directory)):
            if filename.endswith('.' + str(self.filetype)):
                file = open(str(self.directory) + filename, 'r')
                output_file = open('output.txt','a')
                for line in file.readlines():
                    output_file.write(line)
                file.close()
                output_file.close()

class WriteCSV(Write):
    new_files = {}
    file_loc = {}
    file_number = 0;
    numIters = 0
    def __init__(self, directory, filetwype):
        self.file_headers = set()
        Write.__init__(self, directory, filetype)
    def readToWriteFiles(self):
        for filename in os.listdir(str(self.directory)):
            if filename.endswith('.' + str(self.filetype)):
                file = open(str(self.directory) + filename, 'r')
                header_line = file.readline()
                if header_line in WriteCSV.new_files.values():
                    output_file = open(WriteCSV.file_loc[header_line], 'a')
                else:
                    output_filename = 'output' + str(WriteCSV.file_number) + '.csv'
                    WriteCSV.new_files[output_filename] = header_line
                    WriteCSV.file_loc[header_line] = output_filename
                    output_file = open(output_filename, 'a')
                    output_file.write(header_line)
                    WriteCSV.file_number += 1
                for line in file.readlines():
                    output_file.write(line)
                output_file.write('\n')
                file.close()
                output_file.close()
                print filename + " has printed to " + output_filename + "."
                WriteCSV.numIters += 1

inUse = True

while inUse:
    #tested with local directories. File should be entered with a trailing / ex: csv/
    directory = raw_input("Which directory would you like to use? ")
    filetype = raw_input("Which file type would you like to use? ")

    if filetype == 'csv':
        writer = WriteCSV(directory, filetype)
        writer.readToWriteFiles()
    else:
        writer = Write(directory, filetype)
        writer.readToWriteFiles()
    inUse = False
