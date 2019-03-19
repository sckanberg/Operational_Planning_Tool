# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:27:05 2019

@author: David

Operational Planning Tool: 
    Contains functions for both Timeline generator and XML generator

"""

import os, shutil
#sys.path.append(os.getcwd()+'/Operational_Planning_Tool')

if(os.path.isfile('OPT_Config_File.py') == False):
    shutil.copyfile('Operational_Planning_Tool/OPT_Config_File_Original.py','OPT_Config_File.py')


def Timeline_gen():
    """Timeline generator part of Operational Planning Tool for MATS.
    Predicts and schedueles Science Modes into a list containing dates for each Mode and saves it to a .json file
    Input: None
    Output: None
    """
    from Operational_Planning_Tool.OPT_Timeline_generator import Timeline_gen
    
    Timeline_gen()
    
def XML_gen(science_mode_timeline_path):
    """XML generator part of Operational Planning Tool for MATS.
    Converts a .json file containing a list of scheduled Science Modes into commands and saves them to a .xml file
    Input: path to the .json file containing the Science Mode Timeline
    Output: None
    """
    from Operational_Planning_Tool.OPT_XML_generator import XML_generator
    
    XML_generator(science_mode_timeline_path)

