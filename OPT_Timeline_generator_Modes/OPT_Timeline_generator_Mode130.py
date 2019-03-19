# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:31:27 2018

Part of a program to automatically generate a mission timeline.
The timeline consists of science modes and their start dates expressed 
as a list in chronological order

@author: David
"""

import ephem, sys, logging
from OPT_Config_File import Mode130_settings, Timeline_settings, Logger_name



def Mode130(Occupied_Timeline):
    
    initial_date = date_calculator()
    
    Occupied_Timeline, comment = date_select(Occupied_Timeline, initial_date)
    
    
    return Occupied_Timeline, comment
    


##################################################################################################
##################################################################################################



def date_calculator():
    
    Logger = logging.getLogger(Logger_name())
    
    try:
        Logger.info('Mode start_time used as initial date')
        initial_date = Mode130_settings['start_time']
    except:
        Logger.info('Timeline start_time used as initial date')
        initial_date = Timeline_settings()['start_time']
    
    return initial_date



##################################################################################################
##################################################################################################



def date_select(Occupied_Timeline, initial_date):
    
    from Operational_Planning_Tool.OPT_library import scheduler
    
    date = initial_date
    endDate = ephem.Date(initial_date + ephem.second*Timeline_settings()['mode_separation'] +
                                 ephem.second*Mode130_settings()['mode_duration'])
    
    
    ############### Start of availability schedueler ##########################
    
    date, endDate, iterations = scheduler(Occupied_Timeline, date, endDate)
                
    ############### End of availability schedueler ##########################
    
    comment = 'Number of times date postponed: ' + str(iterations)
    
    "Get the name of the parent function, which is always defined as the name of the mode"
    Mode_name = sys._getframe(1).f_code.co_name
    
    Occupied_Timeline[Mode_name] = (date,endDate)
    
    return Occupied_Timeline, comment



'''
import ephem, sys
from OPT_Config_File import Mode130_settings, Timeline_settings, Logger_name



def Mode130(Occupied_Timeline):
    
    Mode130_initial_date = Mode130_date_calculator()
    
    Occupied_Timeline, Mode130_comment = Mode130_date_select(Occupied_Timeline, Mode130_initial_date)
    
    
    
    return Occupied_Timeline, Mode130_comment
    


##################################################################################################
##################################################################################################



def Mode130_date_calculator():
    
    Mode130_initial_date = Timeline_settings()['start_time']
    
    return Mode130_initial_date



##################################################################################################
##################################################################################################



def Mode130_date_select(Occupied_Timeline, Mode130_initial_date):
    
    
    Mode130_date = Mode130_initial_date
    Mode130_endDate = ephem.Date(Mode130_initial_date + ephem.second*Timeline_settings()['mode_separation'] +
                                 ephem.second*Mode130_settings()['mode_duration'])
    
    
    ############### Start of availability schedueler ##########################
    
    iterations = 0
    restart = True
    ## Checks if date is available and postpones starting date of mode until available
    while( restart == True):
        restart = False
        
        for busy_dates in Occupied_Timeline.values():
            if( busy_dates == []):
                continue
            else:
                if( busy_dates[0] <= Mode130_date < busy_dates[1] or 
                       busy_dates[0] < Mode130_endDate <= busy_dates[1]):
                    
                    Mode130_date = ephem.Date(Mode130_date + ephem.second*Timeline_settings()['mode_separation']*2)
                    Mode130_endDate = ephem.Date(Mode130_endDate + ephem.second*Timeline_settings()['mode_separation']*2)
                    
                    iterations = iterations + 1
                    restart = True
                    break
                
    ############### End of availability schedueler ##########################
    
    Mode130_comment = 'Number of times date postponed: ' + str(iterations)
    
    
    
    Occupied_Timeline['Mode130'] = (Mode130_date,Mode130_endDate)
    
    return Occupied_Timeline, Mode130_comment
'''