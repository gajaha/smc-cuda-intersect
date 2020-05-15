The simulation snapshot was generated using a TRANSIMS simulation of commute to work (but not from work). It contains vehicle traces at 30 second intervals on a work day.

We provide a short snapshot for testing (first 10000 lines, called Snapshot_small.csv), as well the full day split up into increments of 1 million lines (about 25 million lines total, named Snapshot_{index of first line}.csv).

The columns are:
- VEHICLE: Unique vehicle ID
- TIME: Time stamp
- LINK: Unique link ID, which matches the given road network
- DIR: Direction. 0 is in the same order as the line segments, 1 is opposite direction.
- LANE: Which lane of the link the vehicle is in
- OFFSET: distance traveled on link -- not needed if you use the coordinates
- SPEED: speed at exact time of snapshot
- ACCEL: acceleration -- negative = slowing down
- VEH_TYPE: vehicle type (should be all 1 = passenger car)
- DRIVER: unique driver ID
- PASSENGERS: number of passengers (should be all 0)
- X_COORD, Y_COORD: position in UTM coordinates. If you prefer lat/lon, you can convert it using a GIS program such as QGIS (EPSG:26916 works as projection), or using a library. Chicago is in UTM zone 16N.