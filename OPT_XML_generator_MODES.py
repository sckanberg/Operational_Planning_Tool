# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:35:08 2018

Generates and calculates parameters for each mode, and converts them to strings,
then calls for macros, which will generate commands in the XML-file.

Functions on the form "XML_generator_X", where the last X is any Mode:
    Input:
        root =  XML tree structure. Main container object for the ElementTree API. lxml.etree.Element class
        date = Starting date of the Mode. On the form of the ephem.Date class.
        duration = The duration of the mode [s] as an integer class.
        relativeTime = The starting time of the mode with regard to the start of the timeline [s] as an integer class
        params = Dictionary containing the parameters of the mode.
    Output:
        None

When creating new Mode functions it is crucial that the function name is
XML_generator_"Mode_name", where Mode_name is the same as the string used in the Science Mode Timeline

 
@author: David
"""

from pylab import zeros, pi, arccos
import ephem, logging
from OPT_Config_File import Logger_name, Timeline_settings
Logger = logging.getLogger(Logger_name())


def XML_generator_Mode1(root, date, duration, relativeTime, params = {}):
    "Generates parameters and calls for macros, which will generate commands in the XML-file"
    
    from OPT_Config_File import Mode1_settings, getTLE
    from Operational_Planning_Tool.OPT_XML_generator_macros import IR_night, IR_day, NLC_day, NLC_night
    
    log_timestep = Mode1_settings()['log_timestep']
    Logger.info('log_timestep [s]: '+str(log_timestep))
    
    Logger.debug('params from Science Mode List: '+str(params))
    params = params_checker(params,Mode1_settings)
    Logger.info('params after params_checker function: '+str(params))
    
    Sun = ephem.Sun(date)
    MATS = ephem.readtle('MATS', getTLE()[0], getTLE()[1])
    
    "Pre-allocate space"
    lat_MATS = zeros((duration,1))
    sun_angle = zeros((duration,1))
    
    
    R_mean = 6371
    pointing_altitude = str(params['pointing_altitude'])
    lat = params['lat']/180*pi
    
    #Estimation of the angle between the sun and the FOV position when it enters eclipse
    MATS_nadir_eclipse_angle = arccos(R_mean/(R_mean+90))/pi*180 + 90
    
    Logger.info('MATS_nadir_eclipse_angle : '+str(MATS_nadir_eclipse_angle))
    
    "Loop and calculate the relevant angle of each star to each direction of MATS's FOV"
    for t in range(duration):
        
        
        
        current_time = ephem.Date(date+ephem.second*t)
        
        
        
        MATS.compute(current_time)
        
        lat_MATS[t]= MATS.sublat
        
        
        Sun.compute(current_time)
        sun_angle[t]= ephem.separation(Sun,MATS)/pi*180
        
        if( t % log_timestep == 0):
            Logger.info('')
            Logger.info('current_time: '+str(current_time))
            Logger.info('lat_MATS [degrees]: '+str(lat_MATS[t]/pi*180))
            Logger.info('sun_angle [degrees]: '+str(sun_angle[t]))
        
        
        ############# Initial Mode setup ##########################################
        
        if( t == 0 ):
            
            "Check if night or day"
            if( sun_angle[t] > MATS_nadir_eclipse_angle ):
                
                if( abs(lat_MATS[t]) < lat):
                    current_state = "IR_night"
                    comment = current_state+': '+str(params)
                    IR_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                elif( abs(lat_MATS[t]) > lat):
                    current_state = "NLC_night"
                    comment = current_state+': '+str(params)
                    NLC_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                    
            elif( sun_angle[t] < MATS_nadir_eclipse_angle ):
                
                if( abs(lat_MATS[t]) < lat):
                    current_state = "IR_day"
                    comment = current_state+': '+str(params)
                    IR_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                elif( abs(lat_MATS[t]) > lat):
                    current_state = "NLC_day"
                    comment = current_state+': '+str(params)
                    NLC_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                
        
        
        ############# End of Initial Mode setup ###################################
        
        
        
       
        if(t != 0):
            ####################### SCI-mode Operation planner ################
            
            
           
            #Check if night or day
            if( sun_angle[t] > MATS_nadir_eclipse_angle ):
                
                #Check latitude
                if( abs(lat_MATS[t]) < lat and current_state != "IR_night"):
                    
                    #Check dusk/dawn and latitude boundaries
                    if( sun_angle[t] > MATS_nadir_eclipse_angle and sun_angle[t-1] < MATS_nadir_eclipse_angle):
                        current_state = "IR_night"
                        comment = current_state+': '+str(params)
                        IR_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                    elif(abs(lat_MATS[t]) < lat and abs(lat_MATS[t-1]) > lat):
                        current_state = "IR_night"
                        comment = current_state+': '+str(params)
                        IR_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                        
                #Check latitude
                if( abs(lat_MATS[t]) > lat and current_state != "NLC_night"):
                    
                    #Check dusk/dawn and latitude boundaries
                    if( sun_angle[t] > MATS_nadir_eclipse_angle and sun_angle[t-1] < MATS_nadir_eclipse_angle):
                        current_state = "NLC_night"
                        comment = current_state+': '+str(params)
                        NLC_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                    elif(abs(lat_MATS[t]) > lat and abs(lat_MATS[t-1]) < lat):
                        current_state = "NLC_night"
                        comment = current_state+': '+str(params)
                        NLC_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                        
            #Check if night or day#            
            if( sun_angle[t] < MATS_nadir_eclipse_angle ):
                
                #Check latitude
                if( abs(lat_MATS[t]) < lat and current_state != "IR_day"):
                    
                    #Check dusk/dawn and latitude boundaries
                    if( sun_angle[t] > MATS_nadir_eclipse_angle and sun_angle[t-1] < MATS_nadir_eclipse_angle):
                        current_state = "IR_day"
                        comment = current_state+': '+str(params)
                        IR_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                    elif(abs(lat_MATS[t]) < lat and abs(lat_MATS[t-1]) > lat):
                        current_state = "IR_day"
                        comment = current_state+': '+str(params)
                        IR_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                        
                #Check latitude
                if( abs(lat_MATS[t]) > lat and current_state != "NLC_day"):
                    
                    #Check dusk/dawn and latitude boundaries
                    if( sun_angle[t] > MATS_nadir_eclipse_angle and sun_angle[t-1] < MATS_nadir_eclipse_angle):
                        current_state = "NLC_day"
                        comment = current_state+': '+str(params)
                        NLC_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                    elif(abs(lat_MATS[t]) > lat and abs(lat_MATS[t-1]) < lat):
                        current_state = "NLC_day"
                        comment = current_state+': '+str(params)
                        NLC_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                        
            
        if( t % log_timestep == 0):
            Logger.info(current_state)
            
            ############### End of SCI-mode operation planner #################




#######################################################################################




def XML_generator_Mode2(root, date, duration, relativeTime, params = {}):
    "Generates parameters and calls for macros, which will generate commands in the XML-file"
    
    
    from OPT_Config_File import Mode2_settings, getTLE
    from Operational_Planning_Tool.OPT_XML_generator_macros import IR_night, IR_day
    
    
    log_timestep = Mode2_settings()['log_timestep']
    Logger.info('log_timestep [s]: '+str(log_timestep))
    
    Logger.debug('params from Science Mode List: '+str(params))
    params = params_checker(params,Mode2_settings)
    Logger.info('params after params_checker function: '+str(params))
    
    
    Sun = ephem.Sun(date)
    MATS = ephem.readtle('MATS', getTLE()[0], getTLE()[1])
    
    "Pre-allocate space"
    sun_angle = zeros((duration,1))
    
    
    R_mean = 6371
    pointing_altitude = str(params['pointing_altitude'])
    
    #Estimation of the angle between the sun and the FOV position when it enters eclipse
    MATS_nadir_eclipse_angle = arccos(R_mean/(R_mean+90))/pi*180 + 90
    Logger.info('MATS_nadir_eclipse_angle : '+str(MATS_nadir_eclipse_angle))
    
    "Loop and calculate the relevant angle of each star to each direction of MATS's FOV"
    for t in range(duration):
        
        
        current_time = ephem.Date(date+ephem.second*t)
        
        MATS.compute(current_time)
        
        Sun.compute(current_time)
        sun_angle[t]= ephem.separation(Sun,MATS)/pi*180
        
        if( t % log_timestep == 0):
            Logger.info('')
            Logger.info('current_time: '+str(current_time))
            Logger.info('sun_angle [degrees]: '+str(sun_angle[t]))
        
        ############# Initial Mode setup ##########################################
        
        if( t == 0 ):
            
            "Check if night or day"
            if( sun_angle[t] > MATS_nadir_eclipse_angle):
                current_state = "IR_night"
                comment = current_state+': '+str(params)
                IR_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
            elif( sun_angle[t] < MATS_nadir_eclipse_angle):
                current_state = "IR_day"
                comment = current_state+': '+str(params)
                IR_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                
        
        ############# End of Initial Mode setup ###################################
        
        
        
        if(t != 0):
        ####################### SCI-mode Operation planner ################
            
            
           
            #Check if night or day
            if( sun_angle[t] > MATS_nadir_eclipse_angle and current_state != "IR_night"):
                
                #Check dusk/dawn boundaries and if NLC is active
                if( (sun_angle[t] > MATS_nadir_eclipse_angle and sun_angle[t-1] < MATS_nadir_eclipse_angle) or current_state == "NLC_night"):
                    current_state = "IR_night"
                    comment = current_state+': '+str(params)
                    IR_night(root,str(t+relativeTime),pointing_altitude, comment = comment)
                
                    
            #Check if night or day            
            if( sun_angle[t] < MATS_nadir_eclipse_angle and current_state != "IR_day"):
                
                #Check dusk/dawn boundaries and if NLC is active
                if( (sun_angle[t] < MATS_nadir_eclipse_angle and sun_angle[t-1] > MATS_nadir_eclipse_angle) or current_state != "NLC_day"):
                    current_state = "IR_day"
                    comment = current_state+': '+str(params)
                    IR_day(root,str(t+relativeTime),pointing_altitude, comment = comment)
                        
        
        if( t % log_timestep == 0):
            Logger.info(current_state)
                 
        ############### End of SCI-mode operation planner #################





############################################################################################




def XML_generator_Mode120(root, date, duration, relativeTime, 
                       params = {}):
    "Generates and calculates parameters and calls for macros, which will generate commands in the XML-file"
    
    
    from OPT_Config_File import Mode120_settings
    from Operational_Planning_Tool.OPT_XML_generator_macros import Mode120_macro
    
    Logger.debug('params from Science Mode List: '+str(params))
    params = params_checker(params,Mode120_settings)
    Logger.info('params after params_checker function: '+str(params))
    
    comment = 'Mode 120 starting date: '+str(date)+', '+str(params)
    
    GPS_epoch = Timeline_settings()['GPS_epoch']
    leapSeconds = ephem.second*Timeline_settings()['leap_seconds']
    freeze_start_utc = ephem.Date(date+ephem.second*params['freeze_start'])
    freezeTime = str(int((freeze_start_utc+leapSeconds-GPS_epoch)*24*3600))
    
    FreezeDuration = str(params['freeze_duration'])
    
    pointing_altitude = str(params['pointing_altitude'])
    
    Logger.info('GPS_epoch: '+str(GPS_epoch))
    Logger.info('freeze_start_utc: '+str(freeze_start_utc))
    Logger.info('freezeTime [GPS]: '+freezeTime)
    Logger.info('FreezeDuration: '+FreezeDuration)
    
    Mode120_macro(root = root, relativeTime = str(relativeTime), freezeTime=freezeTime, 
                     FreezeDuration = FreezeDuration, pointing_altitude = pointing_altitude, comment = comment)




################################################################################################




def XML_generator_Mode130(root, date, duration, relativeTime, 
                       params = {}):
    "Generates parameters and calls for macros, which will generate commands in the XML-file"
    
    
    from OPT_Config_File import Mode130_settings
    from Operational_Planning_Tool.OPT_XML_generator_macros import Mode130_macro
    
    Logger.debug('params from Science Mode List: '+str(params))
    params = params_checker(params,Mode130_settings)
    Logger.info('params after params_checker function: '+str(params))
    
    comment = 'Mode 130 starting date: '+str(date)+', '+str(params)
    
    pointing_altitude = str(params['pointing_altitude'])
    
    
    
    Mode130_macro(root = root, relativeTime = str(relativeTime), pointing_altitude = pointing_altitude, comment = comment)




##############################################################################################




def XML_generator_Mode200(root, date, duration, relativeTime, 
                       params = {}):
    "Generates and calculates parameters, and convert them to strings, then and calls for macros, which will generate commands in the XML-file"
    
    
    from OPT_Config_File import Mode200_settings
    from Operational_Planning_Tool.OPT_XML_generator_macros import Mode200_macro
    
    params = params_checker(params,Mode200_settings)
    
    comment = 'Mode 200 starting date: '+str(date)+', '+str(params)
    
    
    GPS_epoch = Timeline_settings()['GPS_epoch']
    leapSeconds = ephem.second*Timeline_settings()['leap_seconds']
    freeze_start_utc = ephem.Date(date+ephem.second*params['freeze_start'])
    
    pointing_altitude = str(params['pointing_altitude'])
    freezeTime = str(int((freeze_start_utc+leapSeconds-GPS_epoch)*24*3600))
    FreezeDuration = str(params['freeze_duration'])
    
    Logger.info('GPS_epoch: '+str(GPS_epoch))
    Logger.info('freeze_start_utc: '+str(freeze_start_utc))
    Logger.info('freezeTime [GPS]: '+freezeTime)
    Logger.info('FreezeDuration: '+FreezeDuration)
    
    Mode200_macro(root = root, relativeTime = str(relativeTime), freezeTime=freezeTime, 
                     FreezeDuration = FreezeDuration, pointing_altitude = pointing_altitude, comment = comment)


'''
def XML_generator_Mode=X=(root, date, duration, relativeTime, params = {}):
    "This is a template for a new mode. Exchange 'Mode=X=' for the name of the new mode"
    
    from Operational_Planning_Tool.OPT_XML_generator_macros import Mode=X=_macro
    from OPT_Config_File import Mode=X=_settings
    
    #params = params_checker(params,Mode=X=_settings)
    
    
    Mode=X=_macro()
'''

#######################################################################################################






def params_checker(params, Mode_settings):
    '''Function to check what parameters are given in the Science Mode Timeline List and fill in any missing from the Config File.
    Inputs:
        params: Dictionary containing the parameters given in the Science Mode Timeline List.
        Mode_settings: Function to the settings given in OPT_Config_File of the current Mode"
    Output:
        params: Dictionary containing parameters given in the Science Mode List together with any parameters missing, '
        which are give in OPT_Config_File
    '''
    
    
    "Check if optional params were given"
    if( params != Mode_settings()):
        params_new = Mode_settings()
        "Loop through parameters given and exchange the settings ones"
        for key in params.keys():
            params_new[key] = params[key]
        params = params_new
    return params

