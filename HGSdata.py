# -*- coding: utf-8 -*-

# Created: October 23, 2017
# Author: Wesley Campbell

# A class for dealing with the breakthrough curve files produced after a 
#   model in HydroGeoSphere is successfully executed

class HGSdata(object):
    """A set of values defining the concentration breakthrough curve
    resulting from a successfully executed model in HydroGeoSphere, organized
    into a dictionary containing values of time, concentration, and x, y, and z
    coordinates."""
    
    def __init__(self):
        """Create an empty dictionary"""
        self.vals = {}
        
    def getConcData(self, folder_path, model_name, well_name):
        """Read the HydroGeosphere files, organize the data, and put it all
        into self.vals"""
        # Accepts strings for model_name and well_name
        
        # Put file names for all of the observation wells into a list
        if type(model_name) == str:
            pass
        else: 
            print('INVALID MODEL NAME! Enter a string.')
            
        if type(well_name) == str:
            pass
        else:
            print('INVALID WELL NAME! Enter a string.')
            
        # Read files and put them into a list
        while True:
            if folder_path == None:
                filename =  model_name + 'o.observation_well_conc.' +         \
                            well_name + '.Species001.dat'
                break
            elif type(folder_path) == str:
                filename = folder_path + '/' + model_name +                   \
                           'o.observation_well_conc.' + well_name +           \
                           '.Species001.dat'
                break
            else:
                print("INVALID FOLDER PATH! Enter a string.")
                
        infile = open(filename)
        readfile = infile.readlines()
        
        # Organize the data
        Title = []
        Variables = []
        Values = []
        # Assign the first two lines to the Title and Variables variables
        # Before appending the numerical results to the Values variable
        i = 0
        for line in readfile:
            if i == 0:
                Title.append(line)
                i += 1
            elif i == 1:
                Variables.append(line.split())
                i += 1
            else:
                Values.append(line.split())

        del Variables[0][0] # delete the 'VARIABLES' string
        Variables[0][0] = Variables[0][0].split(",")
        # Flatten the list
        Variables = Variables[0][0]
        # Get rid of the useless characters
        for i in range(len(Variables)):
            Variables[i] = Variables[i].strip('"=')

        # Put the data into lists
        T, C, X, Y, Z = [], [], [], [], [] # empty variable lists
        # Determine which column each quantity exists in
        for i in range(len(Variables)):
            if Variables[i] == 'Time':
                tindex = i
            elif Variables[i] == 'C':
                cindex = i
            elif Variables[i] == 'X':
                xindex = i
            elif Variables[i] == 'Y':
                yindex = i
            elif Variables[i] == 'Z':
                zindex = i
        # Now, put each column into the correct list
        for row in Values:
            T.append(float(row[tindex]))
            C.append(float(row[cindex]))
            X.append(float(row[xindex]))
            Y.append(float(row[yindex]))
            Z.append(float(row[zindex]))
        
        # Put lists into dictionaries
        self.vals['time'] = T
        self.vals['concentration'] = C
        self.vals['x'] = X
        self.vals['y'] = Y
        self.vals['z'] = Z
        
    def times(self):
        """Returns the time values from self.vals"""
        return self.vals['time']
    
    def concentrations(self):
        """Returns the concentration values from self.vals"""
        return self.vals['concentration']
    
    def xcoords(self):
        """Returns the x-coordiantes"""
        return self.vals['x']
    
    def ycoords(self):
        """Returns the y-coordinates"""
        return self.vals['y']
    
    def zcoords(self):
        """Returns the z-coordinates"""
        return self.vals['z']
