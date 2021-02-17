# This code accesses raster statistics based on shapefile regions
# This code summarizes raster values over polygonal areas
# This code used zonal statistics to get pixel statistics per polygon


## Importing libraries
import fiona
import pandas as pd
from rasterstats import zonal_stats

## Opening shapefile
# each region in the shapefile must contain IDs
region_shp = fiona.open('./regions_ID.shp')

## Creating a file to save the results
results = {}

## Getting the raster statistics based on each reagion displayed in the shapefile
# change the variable 'stats' according to the desired statistic, as max, min, etc
# The full documentation is available here: <https://pythonhosted.org/rasterstats/manual.html>
for i in region_shp: 
    raster_statistics = zonal_stats(i, './your_raster_here.tif',
                             stats=['majority']) 
    region = i['id'] 
    results[region] = raster_statistics 


## Creating a new data frame to save the results in csv
df = pd.DataFrame(columns=['id', 'statistical_measure', 'pixel_value'])


## Accessing dataset and appeding in the already created data frame (df)
for id, statistics in results.items(): 
    dados = {}                              
    for infomation in statistics:            
        for statistical_measure, pixel_value in information.items(): 
            dados = {'id': id,
                  'statistical_measure': statistical_measure,
                  'pixel_value': pixel_value}
            df = df.append(dados, ignore_index=True) #'ignore_index=True': adds the data in the order that they have been received
            

## Saving final data frame in csv
df.to_csv('./final_file.csv', index=False) # 'index=False': does not add an index to the csv


