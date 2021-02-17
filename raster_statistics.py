# importing libraries
import fiona
import pandas as pd
from rasterstats import zonal_stats

# opening shapefile
regiao_shp = fiona.open('./regioes_ID.shp')

# creting a file to save the results
resultados = {}

# getting the raster statistics based on each reagion displayed in the shapefile
# change the variable 'stats' according to the desired statistic
for i in regiao_shp: 
    estatisticas_raster = zonal_stats(i, './your_raster_here.tif',
                             stats=['majority']) 
    regiao = i['id'] #(III)
    resultados[regiao] = estatisticas_raster 
    
# creating a new data frame to save the results in csv
df = pd.DataFrame(columns=['id', 'medida_estatistica', 'valor_pixel'])

# accessing dataset and appeding in the aforementioned data frame 
for id, estatisticas in resultados.items(): 
    dados = {}                              
    for informacoes in estatisticas:            
                    
        for medida_estatistica, valor_pixel in informacoes.items(): 
            dados = {'id': id,
                  'medida_estatistica': medida_estatistica,
                  'valor_pixel': valor_pixel}
            df = df.append(dados, ignore_index=True)
#'ignore_index=True': adds the data in the order that they have been received

df.to_csv('./final_file.csv', index=False)
# 'index=False': does not add an index to the csv

