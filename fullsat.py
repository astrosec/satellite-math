# --------- fullsat.py --------- Apr.27-May.07, 2019 --------------------
from skyfield.api import EarthSatellite, Topos, load
from numpy import around

ts = load.timescale()
timestring= '2020, 3, 26, 21, 53, 30'
t = ts.utc(2020,3,26,21,53,30)
# TLE twoline dbase
line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'
#
loc = Topos(38.8892771, -77.0353628)
satellite = EarthSatellite(line1, line2)

# Geocentric
geometry = satellite.at(t)

# Geographic point beneath satellite
subpoint = geometry.subpoint()
latitude = subpoint.latitude
longitude = subpoint.longitude
elevation = subpoint.elevation

# Topocentric
difference = satellite - loc
geometry = difference.at(t)
topoc= loc.at(t)
#
topocentric = difference.at(t)
geocentric = satellite.at(t)
# ------ Start outputs -----------
print ('\n Ephemeris time:', timestring)
print (' JD time: ',t)
print ('',loc)
print ('\n Subpoint Longitude= ', longitude )
print (' Subpoint Latitude = ', latitude )
print (' Subpoint Elevation=  {0:.3f}'.format(elevation.km),'km')
# ------ Step 1: compute sat horizontal coords ------
alt, az, distance = topocentric.altaz()
if alt.degrees > 0:
    print('\n',satellite, '\n is above the horizon')
print ('\n Altitude= ', alt.degrees )
print (' Azimuth = ', az.degrees )
print (' Distance=  {0:.3f}'.format(distance.km), 'km')
#
# ------ Step 2: compute sat RA,Dec [equinox of date] ------
ra, dec, distance = topocentric.radec(epoch='date')
print ('\n Right Ascension RA= ', ra )
print (' Declination     de= ', dec )
#
# ------ Step 3: compute sat equatorial coordinates  --------
print ('\n Vectors to define sat position: r = R + rho')
print('    Obs. posit.(R): ',topoc.position.km,'km')
print(' Topocentric (rho): ',topocentric.position.km,'km')
print(' -----------------')
print('    Geocentric (r): ',geocentric.position.km,'km')
#
# ------ Step 4: sat equatorial coordinates roundoff 3 decimals  --------
sho1= around(topoc.position.km, decimals=3)
sho2= around(topocentric.position.km, decimals=3)
sho3= around(geocentric.position.km, decimals=3)
print ('\n Rounded Vectors to define sat position: r = R + rho')
print('    Obs. posit.(R): ',sho1,'km')
print(' Topocentric (rho): ',sho2,'km')
print(' -----------------')
print('    Geocentric (r): ',sho3,'km')
# EOF: ----- fullsat.py -----------
