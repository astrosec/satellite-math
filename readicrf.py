from skyfield.api import Topos, load
from skyfield.api import EarthSatellite
from skyfield.positionlib import ICRF
from skyfield.positionlib import Geometric
from skyfield.positionlib import Barycentric
ts = load.timescale()

thisx = 4085.0136322698854
thisy = -1852.4897691900894
thisz =  -4916.7862179899175

vec = ICRF([thisx,thisy,thisz])
vec.t = ts.utc(2020, 3, 18, 3, 36, 35.0)

vecG1 = Geometric([thisx,thisy,thisz])
vecG1.t = ts.utc(2020, 3, 18, 3, 36, 35.0)



satellites = load.tle_file('fullcatalog.txt')
print( 'Loaded', len(satellites), 'satellites')

firsttime = ts.utc(2020, 3, 18, 3, 36, 35.0)



for sat in satellites:
    geocentric = sat.apparent(firsttime)
    thatx, thaty, thatz = geocentric.position.km
    print(geocentric.position.km)
    #if (thatx == thisx):
    #    print("MATCH")
vecG2 = Geometric([thisx,thisy,thisz])
#vecG2.t = ts.utc(2020, 3, 18, 9, 2, 46.0)
#print vecG2





ts = load.timescale()
thislat = 38.89
thislong = -77.03
thisalt = 11.9
monument = Topos(thislat, thislong,elevation_m = thisalt)

line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'
satellite = EarthSatellite(line1, line2,'REDACT', ts);

t = ts.utc(2020,3,26,21,53,30)

difference = satellite - monument
#print(difference)

topocentric = difference.at(t)

print('Topocentric position elements')
print(topocentric.position.km)

alt, az, distance = topocentric.altaz()

if alt.degrees > 0:
        print('Good we can see REDACT iand its above the horizon')

print 'Altitude (deg): ', alt.degrees
print 'Azimuth (deg):',  az.degrees
print 'Distance (m):', int(distance.m), 'm'

LookatTilt = 90 - alt.degrees
LookatAzimuth = 180 - az.degrees

print 'Adjustments for KML viewpoint which is from the perspective of the satellite camera'
print '==================================================================================='

print '<LookAt id = \"REDACT\">'
print '<latitude>{0}</latitude>'.format(thislat)
print '<longitude>{0}</longitude>'.format(thislong)
print '<altitude>{0}</altitude>'.format(thisalt)
print '<heading>{0}</heading>'.format(LookatAzimuth)
print '<tilt>{0}</tilt>'.format(LookatTilt)
print '<range>{0}</range>'.format(int(distance.m),'m')
