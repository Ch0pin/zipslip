from zipfile import ZipFile
from optparse import OptionParser

import sys

logo="""
        ,--.!,
     __/   -*-
   ,d08b.  '|`
   0088MM
   `9MMP'
"""

if __name__ == "__main__":
    print(logo)

    parser = OptionParser(usage="Usage: {} -f filename -e exploded_dir -n zip_name".format(sys.argv[0]))

    parser.add_option("-f","--file",dest="file",help="Filename to zip")
    parser.add_option("-e","--explode",dest="explode_dir",help="Explode destination")
    parser.add_option("-n","--name",dest="zip_name",help="Name of the zip file" )

    options, args = parser.parse_args()


    if not options.file or not options.explode_dir or not options.zip_name:
        print("Usage: {} -f filename -e exploded_dir -n zip_name".format(sys.argv[0]))
        sys.exit()
    else:
        explode_dir =  options.explode_dir
        file = options.file
        name = options.zip_name

        print('File {} will explode to {}'.format(file,explode_dir))

        with open(file, mode='rb') as file1: # b is important -> binary
            fileContent = file1.read()

        with ZipFile(name,'w') as zip:
            zip.writestr(explode_dir,fileContent)

        print('All files zipped successfully!')
