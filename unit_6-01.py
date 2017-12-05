# Created by: Matthew walsh
# Created on: Nov 2017
# Created for: ICS3U
# This program uses enumerated types for days of the week

from enum import Enum

# an enumerated type of planets
weekdays = Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

day_selected = raw_input('Enter your favourite day: ')
if day_selected in weekdays:
    print('your favourite day is: ' + day_selected)



