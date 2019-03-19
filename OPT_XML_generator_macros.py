# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:31:43 2018

Contains macro functions that represent parts of or a whole sciencemode.

Input:
    root =  XML tree structure. Main container object for the ElementTree API. lxml.etree.Element class
    relativeTime = The starting time of the mode with regard to the start of the timeline [s] as an str class
    comment = A comment for the macro as a str class
    *Any other optional inputs depending on the macro which are defined in each macro function*
    
Output:
    None

@author: David
"""


from Operational_Planning_Tool.OPT_XML_generator_Commands import *


def NLC_night(root, relativeTime, pointing_altitude, comment):
    ''' Macro that corresponds to Mode1 when nadir is on during NLC season at latitudes polewards of +-45 degrees"
        Input:
            pointing_altitude = The altitude of the tangential LP [m] as a str class.
    '''
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime, Initial = pointing_altitude, Final = pointing_altitude, comment = comment)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '1', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '2', NumRows = '400', NumColumnsBin = '40', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '3', NumRows = '400', NumColumnsBin = '81', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '7', NumRows = '400', NumColumnsBin = '409', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)
    
    
def NLC_day(root, relativeTime, pointing_altitude, comment):
    ''' Macro that corresponds to Mode1 when nadir is off during NLC season at latitudes polewards of +-45 degrees"
        Input:
            pointing_altitude = The altitude of the tangential LP [m] as a str class.
    '''
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime,  Initial = pointing_altitude, Final = pointing_altitude, comment = comment)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '1', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '2', NumRows = '400', NumColumnsBin = '40', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '3', NumRows = '400', NumColumnsBin = '81', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '7', NumRows = '400', NumColumnsBin = '409', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '0', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)
    
    
def IR_night(root, relativeTime, pointing_altitude, comment):
    ''' Macro that corresponds to Mode1 (at latitudes equatorwards of +-45 degrees) and Mode2. Nadir is on."
        Input:
            pointing_altitude = The altitude of the tangential LP [m] as a str class.
    '''
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime, Initial = pointing_altitude, Final = pointing_altitude, comment = comment)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '0', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '2', NumRows = '400', NumColumnsBin = '40', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '3', NumRows = '400', NumColumnsBin = '81', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '7', NumRows = '400', NumColumnsBin = '409', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)
    

def IR_day(root, relativeTime, pointing_altitude, comment):
    ''' Macro that corresponds to Mode1 (at latitudes equatorwards of +-45 degrees) and Mode2. Nadir is off."
        Input:
            pointing_altitude = The altitude of the tangential LP [m] as a str class.
    '''
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime, Initial = pointing_altitude, Final = pointing_altitude, comment = comment,)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '0', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '2', NumRows = '400', NumColumnsBin = '40', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '3', NumRows = '400', NumColumnsBin = '81', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '7', NumRows = '400', NumColumnsBin = '409', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '0', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)
    

def Mode120_macro(root, relativeTime, freezeTime, FreezeDuration, pointing_altitude, comment):
    ''' Macro that corresponds to Mode120.
        Input:
            freezeTime = Start time of attitude freeze command in on-board time [s] as a str class.
            FreezeDuration = Duration of freeze [s] as a str class.
            pointing_altitude = The altitude of the tangential LP [m] as a str class.
    '''
    
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime, Initial = pointing_altitude, Final = pointing_altitude, Rate = "0", comment = comment)
    
    
    relativeTime = TC_affArgFreezeStart(root, relativeTime, StartTime = freezeTime, comment = comment)
    
    
    relativeTime = TC_affArgFreezeDuration(root, relativeTime, FreezeDuration = FreezeDuration, comment = comment)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '1', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '1', NumRows = '512', NumColumnsBin = '1', NumColumns = '2048')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '1', NumRows = '512', NumColumnsBin = '1', NumColumns = '2048')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '1', NumRows = '512', NumColumnsBin = '1', NumColumns = '2048')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '0', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)
    
    

def Mode130_macro(root, relativeTime, pointing_altitude, comment):
    ''' Macro that corresponds to Mode130"
        Input:
            pointing_altitude = The altitude of the tangential LP [m] as a str class.'''
    
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime, Initial = pointing_altitude, Final = pointing_altitude, Rate = "0", comment = comment)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '1', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '1', NumRows = '512', NumColumnsBin = '1', NumColumns = '2048')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '1', NumRows = '512', NumColumnsBin = '1', NumColumns = '2048')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '1', NumRows = '512', NumColumnsBin = '1', NumColumns = '2048')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '0', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)


def Mode200_macro(root, relativeTime, freezeTime, FreezeDuration, pointing_altitude, comment):
    ''' Macro that corresponds to Mode200.
        Input:
            freezeTime = Start time of attitude freeze command in on-board time [s] as a str class.
            FreezeDuration = Duration of freeze [s] as a str class.
            pointing_altitude = The altitude of the tangential LP [m] as a str class.
    '''
    
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "2", comment = comment)
    
    
    relativeTime = TC_acfLimbPointingAltitudeOffset(root, relativeTime, Initial = pointing_altitude, Final = pointing_altitude, Rate = "0", comment = comment)
    
    
    relativeTime = TC_affArgFreezeStart(root, relativeTime, StartTime = freezeTime, comment = comment)
    
    
    relativeTime = TC_affArgFreezeDuration(root, relativeTime, FreezeDuration = FreezeDuration, comment = comment)
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '3', CCDMode = '1', ExpInterval = '3000', ExpTime = '3000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '2', NumRows = '400', NumColumnsBin = '40', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '12', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '3', NumRows = '400', NumColumnsBin = '81', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '48', CCDMode = '1', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '100', NumRowsBin= '7', NumRows = '400', NumColumnsBin = '409', NumColumns = '2000')
    
    
    relativeTime = TC_pafCCDMain(root, relativeTime, CCDselect = '64', CCDMode = '0', ExpInterval = '5000', ExpTime = '5000', comment = comment, 
                  NumRowsSkip = '0', NumRowsBin= '110', NumRows = '500', NumColumnsBin = '196', NumColumns = '1980', JPEGquality = '100')
    
    
    relativeTime = TC_pafMode(root, relativeTime, mode = "1", comment = comment)
    
    
'''
def Mode_User_Specified_macro(root, relativeTime, comment):
    "This is a template for a new macro. Exchange '_User_Specified' for the name of the new macro"
    pass
    
'''
