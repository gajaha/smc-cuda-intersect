1. Darksky API service: https://darksky.net/.
DarkSky is one possible service which enables the downloading of the weather data. Participants are free to use any other service which provides weather data. 

In case participants choose to use darksky api to download the weather data, we would recommend to read their terms of service fully. This is one reason that we can not provide the weather data. However, we are providing some directions which are helpful for the participants to fetch the data. 

2. Code snippet to use the api: https://darksky.net/dev/docs/libraries 

3. FetchWeatherFeeds.r: a sample R script to fetch the weather data for a provided geo-location and a time window. There is a limit on how many API request one can make with own API key. Participants can decide upon how data is needed for the analysis before downloading the data. For more information in the use of the api refer above api reference.

4. Grid_0_05_clipped: This CSV file contains 24 geo-locations in the form of regular grid points which can be used as a reference to download the weather data from the API service (refer the R script provided).  This is a reference file and provides potential geo-locations at regular intervals that cover the entire study region of the city of Chicago. Participants can try different strategies on selecting geo-locations to download the weather data. The above code script can not automatically use this file as an input to read the the location (lat/long). Participants can either manually enter the locations in the script by referring this file or modify the script to read this CSV file.  


  