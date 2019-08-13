# python_MOS
Script to download the current NAM or GFS MOS short term text files and import them into a pandas dataframe. Currently only supported in Python 2.7 and below due to the urllib2 library being incompatible with Python 3.

This script takes the input for a MOS station in the United States and grabs
the data and puts it into a pandas dataframe.

import NAMMOS or GFSMOS

function call:
df = NAMMOS(stationcode) ex: 'KLWM', 'KBOX' 


This only is for the short term MOS. The values for Q06, P06, P12, Q12, X/N
are not properly spaced out to match with their appropriate times at this 
point so adjustments need to be made when using said data. This will be added
in a future update
