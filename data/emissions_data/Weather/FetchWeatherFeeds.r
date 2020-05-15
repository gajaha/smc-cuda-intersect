## This code will featch the hourly weather information for a given location for year 2017
## This stores weather information for each day in seperate file
## Developer: Kuldeep Kurte,
## Contact: kurtekr@ornl.gov

library(darksky)
#library(tidyverse)
library(lubridate)


Sys.setenv(DARKSKY_API_KEY = "-----Paste API key here-----") #my API key


location_id=0
lat=41.97303858
long=-87.890114


num_of_days=2 #365

startdatetime=ymd_hms("2017-01-01 00:00:00", tz = "US/Central")

dir.create(paste("data/weather_data_loc/",location_id, sep = ""), showWarnings=FALSE)

for(delta in (0:num_of_days))
{
  WeatherDF_All=get_forecast_for(lat, long , paste(startdatetime+days(delta),"T00:00:00-06:00", sep = ""), add_headers=TRUE)
  WeatherDF_Hourly= WeatherDF_All$hourly
  write.csv(WeatherDF_Hourly, file = paste("data/weather_data_loc/",location_id,"/", paste(startdatetime+days(delta)),".csv",sep = ""))

  
}
