# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:42:57 2016

@author: RupGautam
"""

'''
A flight was scheduled to arrive at a particular time and it is now estimated
to arrive at another time. Write function that returns the flight's status:
- One time
- Early 
- Delayed 
'''

def report_status(scheduled_time, estimated_time):
    '''(number, number) -> str 
    
    Return the flight status (on time, early, delayed) for a flight that was
    scheduled to arrive at scheduled_time but is not estimated to arrive 
    at estimated_time.
    
    Pre-condition:
    0.0 <= scheduled_time  < 24
    0.0 <= estimated_time < 24
    
    >>> report_status(14.3,  14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >> report_status(9.0, 9.5)
    'delayed'
    '''
    
    if scheduled_time == estimated_time:
        return 'on time' 
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed' #scheduled_time < estimated_time
    
