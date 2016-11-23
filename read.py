import os

class Write(object):
    def __init__(self, directory, filetype):
        self.directory = directory
        self.filetype = filetype
    def readToWriteFiles(self):
        #iterate over each file in the directory
        for filename in os.listdir(str(self.directory)):
            #check if the file is the proper file type
            if filename.endswith('.' + str(self.filetype)):
                #open the file
                file = open(str(self.directory) + filename, 'r')
                #create an output file
                output_file = open('output.txt','a')
                #iterate over each line in the file
                for line in file.readlines():
                    #copy the lines from the reading file to the output file
                    output_file.write(line)
                #write a new line at the end of the last line of the file for future concatenation
                output_file.write('\n')
                #close each file
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


def main():
    inUse = True

    while inUse:
        #tested with local directories. File should be entered with a trailing / ex: csv/
        directory = raw_input("Which directory would you like to use? ")
        filetype = raw_input("Which file type would you like to use? ")

        if filetype == 'csv':
            writer = WriteCSV(directory, filetype)
            writer.readToWriteFiles()
        elif filetype.lower().startswith('e') or directory.lower().starswith('e'):
            inUse = False
        else:
            writer = Write(directory, filetype)
            writer.readToWriteFiles()
        inUse = False

if __name__ == '__main__':
    main()
