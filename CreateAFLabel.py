# Imported Modules
import sys
import os
import datetime as DT
import argparse
import CopyFiles
import fileinput
import subprocess


def main():

    parser = argparse.ArgumentParser(description='Creates Arc Flash Labels')

    parser.add_argument('Threat', help='The Name of the Equipment')
    parser.add_argument('EquipName', help='The Name of the Equipment')
    parser.add_argument('Voltage', help='Voltage Level of Equipment')
    parser.add_argument('LD', help='Limited Distance')
    parser.add_argument('RD', help='Restricted Distance',)
    parser.add_argument('GC', help='Insulated Glove Requirement')
    parser.add_argument('IT', help='Insulated tool Requirement')
    parser.add_argument('Energy', help='Calculated AF Energy')
    parser.add_argument('AFAB', help='Arc Flach Approach Boundary (where energy is <1.2 cal/cm^2)')
    parser.add_argument('WD', help='working distance analysis was performed on')
    parser.add_argument('CL', help='Clothing Level Reqirement')
    parser.add_argument('FS', help='Face Shield Requirement')
    parser.add_argument('Date', help='Analysis Date')
    parser.add_argument('Working_Dir', help='working directory')

    args = parser.parse_args()

    Field_List = ['$Threat', '$EquipName', '$Voltage', '$LD', '$RD', '$GC', '$IT', '$Energy', '$AFAB', '$WD', '$CL', '$FS', '$Date']
    Field_Values = [args.Threat, args.EquipName, args.Voltage, args.LD, args.RD, args.GC, args.IT, args.Energy, args.AFAB, args.WD, args.CL, args.FS, args.Date]

    Labels_Path = '{!s}/Labels[{:%Y-%m-%d_%H%M%S}]'.format(args.Working_Dir, DT.datetime.now())
    #print Labels_Path


    #Copy Label Template
    CopyFiles.copyanything('c:\Users\Scott\Dropbox\Scripts\SVG\Arc Flash Label\Labels', Labels_Path)
    os.chdir(Labels_Path)

    FileToSearch = 'AF Label.svg'

    i=0
    for eField in Field_List:
        TempFile = open(FileToSearch, 'r+')
        for line in fileinput.input( FileToSearch ):
           #if TextToSearch in line :
                #print('Match Found')
            #else:
                #print('Match Not Found!!')
            TempFile.write( line.replace( eField, Field_Values[i] ) )
        TempFile.close()
        i = i + 1

    os.chdir(Labels_Path)
    #subprocess.call(["inkscape AF\ Label.svg --export-pdf=new.pdf"])


if __name__ == '__main__':
    main()
    sys.exit()
