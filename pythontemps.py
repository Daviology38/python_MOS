# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:59:47 2019

@author: CoeFamily
"""

from awips.dataaccess import DataAccessLayer
import unittest
import numpy as np
DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")
dataTypes = DataAccessLayer.getSupportedDatatypes()
dataTypes.sort()
list(dataTypes)

request = DataAccessLayer.newDataRequest()
request.setDatatype("grid")
available_grids = DataAccessLayer.getAvailableLocationNames(request)
available_grids.sort()
list(available_grids)

request.setLocationNames("NAM12")
availableParms = DataAccessLayer.getAvailableParameters(request)
availableParms.sort()
list(availableParms)

request.setParameters("T")
availableLevels = DataAccessLayer.getAvailableLevels(request)

request.setLevels("0.0SFC")

cycles = DataAccessLayer.getAvailableTimes(request, True)
times = DataAccessLayer.getAvailableTimes(request)
fcstRun = DataAccessLayer.getForecastRun(cycles[-2], times)
list(fcstRun)


response = DataAccessLayer.getGridData(request, [fcstRun[36]])
for grid in response:
    data = grid.getRawData()
    lons, lats = grid.getLatLonCoords()
    print('Time :', str(grid.getDataTime().getFcstTime()/3600))

Ta = ((data - 273.15))
DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")
dataTypes = DataAccessLayer.getSupportedDatatypes()
dataTypes.sort()
list(dataTypes)

request = DataAccessLayer.newDataRequest()
request.setDatatype("grid")
available_grids = DataAccessLayer.getAvailableLocationNames(request)
available_grids.sort()
list(available_grids)

request.setLocationNames("NAM12")
availableParms = DataAccessLayer.getAvailableParameters(request)
availableParms.sort()
list(availableParms)

request.setParameters("RH")
availableLevels = DataAccessLayer.getAvailableLevels(request)


request.setLevels("0.0SFC")

cycles = DataAccessLayer.getAvailableTimes(request, True)
times = DataAccessLayer.getAvailableTimes(request)
fcstRun = DataAccessLayer.getForecastRun(cycles[-2], times)
list(fcstRun)


response = DataAccessLayer.getGridData(request, [fcstRun[36]])

for grid in response:
    data = grid.getRawData()
    lons, lats = grid.getLatLonCoords()
    print('Time :', str(grid.getDataTime().getFcstTime()/3600))
rh = data 

request = DataAccessLayer.newDataRequest()
request.setDatatype("grid")
available_grids = DataAccessLayer.getAvailableLocationNames(request)
available_grids.sort()
list(available_grids)

request.setLocationNames("NAM12")
availableParms = DataAccessLayer.getAvailableParameters(request)
availableParms.sort()
list(availableParms)

request.setParameters("WGS")
availableLevels = DataAccessLayer.getAvailableLevels(request)


request.setLevels("0.0SFC")

cycles = DataAccessLayer.getAvailableTimes(request, True)
times = DataAccessLayer.getAvailableTimes(request)
fcstRun = DataAccessLayer.getForecastRun(cycles[-2], times)
list(fcstRun)


response = DataAccessLayer.getGridData(request, [fcstRun[7]])

for grid in response:
    data = grid.getRawData()
    lons, lats = grid.getLatLonCoords()
    print('Time :', str(grid.getDataTime().getFcstTime()/3600))
ws = data 

data = np.zeros((rh.shape[0],rh.shape[1]))
for l in range(rh.shape[0]):
    for m in range(rh.shape[1]):
        
        e = (rh[l,m] / 100) * (6.105 * (10**( 7.5 * Ta[l,m] / ( 237.3 + Ta[l,m] ) )))
        data[l,m] =  ((0.5 * ((Ta[l,m] * (9/5) + 32) + 61.0 + (((Ta[l,m] * (9/5) + 32)-68.0)*1.2) + (rh[l,m]*0.094))) + (Ta[l,m] * (9/5) + 32))/2 
print('Model:', str(grid.getLocationName()))
print('Parm :', str(grid.getParameter()))
print('Unit :', str(grid.getUnit()))
print(data.shape)
fcstHr = int(grid.getDataTime().getFcstTime()/3600)
import matplotlib.pyplot as plt
import matplotlib
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import numpy as np
import numpy.ma as ma

from cartopy.feature import NaturalEarthFeature
from scipy.io import loadmat
def make_map(bbox, projection=ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(16, 9),
                           subplot_kw=dict(projection=projection))
    ax.set_extent(bbox)
    ax.coastlines(resolution='50m')
    states = NaturalEarthFeature(category="cultural", scale="50m",
                             facecolor="none",
                             name="admin_1_states_provinces_shp")
    ax.add_feature(states, linewidth=.5, edgecolor="black")
    gl = ax.gridlines(draw_labels=True)
    gl.xlabels_top = gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    return fig, ax
levels = np.arange(40,120,4)
cmap = plt.get_cmap('jet')
bbox = [-74, -69,41, 45]
fig2, ax2 = make_map(bbox=bbox)
cs2 = ax2.contourf(lons, lats, data, levels, cmap=cmap,
                  vmin=data.min(), vmax=data.max())
cbar2 = fig2.colorbar(cs2, extend='both', shrink=0.5, orientation='horizontal')
cbar2.set_label(grid.getLocationName() +" " + grid.getLevel() + " " \
               + "Heat Index (°F) " \
               + "valid " + str(grid.getDataTime().getRefTime()))