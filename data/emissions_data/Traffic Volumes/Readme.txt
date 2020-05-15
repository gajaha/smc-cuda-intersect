Link volumes are provided by day of the week and by hour for a typical work week. They reflect commute *to* work but not *from* work.

Each file contains one hour of data for one day of the week, and the following fields:
- linkID: unique ID, identical to that in the network
- countyID: ID of the county (17031 for all links)
- zoneID: ID of the zone (0 for all links)
- roadTypeID: 4 for Freeway (Urban Restricted), 5 for Local Road (Urban Unrestricted)
- linkLength: link length in miles
- linkVolume: number of vehicles that traversed this link during a given time
- linkDescription: corresponds to roadTypeID
- linkAvgGrade: elevation change (0 for all links/not computed -- feel free to add elevation if you want)