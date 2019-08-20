# python_MOS
Script to download the current NAM or GFS MOS short term text files and import them into a pandas dataframe. Currently only supported in Python 2.7, Python 3 and below using the requests library.

This script takes the input for a MOS station in the United States and grabs
the data and puts it into a pandas dataframe.

import NAMMOS or GFSMOS

function call:
df = NAMMOS(stationcode) ex: 'KLWM', 'KBOS' 


This only is for the short term MOS, long term MOS will be added in a future update.
