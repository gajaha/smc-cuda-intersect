Data contained here is hourly energy use output from two MOVES-Matrix simulations for the Chicago Loop:  morning commute for January 9, 2017 and  24-hour data for July 4 - 10, 2017.

The leftmost column gives the hour of day of the simulation.  The next column to the right gives the Link identification (key to link numbers is given at the end of this document).   The pollutant name is given by code in the next column.  The pollutant code is always 91 for this data set and it refers to energy consumed and emitted as heat exhaust.   Emrate is the emission rate in kJ/vehicle/operating hour and Emquant is the emission quantity in MMBtu.  To understand what the expected ambient temperature elevation for a given link due to vehicle exhaust, the analyst may want to convert the emission quantitiy to W/m2 . 
 
To Get W/m2 for each link:
Divide the MMBtu values for each link at each hour by 3600 to get MMBtu/s, then divide that value by the square area of the link in feet (LINKAREA_F).  This gives MMBtu/s/ft^2
This value is then multiplied by: 11356.538527 to get to Wm-2.  The citation for this value is this web page:  http://www.endmemo.com/sconvert/w_m2btu_sft2.php

Expected increase in air temperature per 100 W/m2 traffic heat exhaust is approximately 0.8 C based on a modeled average in the experiments of Oke et al. (2017).

Chicago Loop link numbers are included in the Road Network shape file.
 
Oke, T. R., Mills, G., Christen, A., & Voogt, J. A. (2017). Urban climates. Cambridge University Press.


   
