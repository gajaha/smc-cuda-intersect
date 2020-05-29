##Script to read simulation snapshots departure time and location. Assign agent location to building.
##Global imports
import pandas as pd
import xarray as xr
import geopandas as gpd
import matplotlib.pyplot as plt

##Read simulation snapshot departure time.
sim_snap = pd.read_csv("/Users/vsundar/Documents/personal/smc/smc-cuda-intersect/data/vehicle_data/Simulation_Snapshot/Snapshot_small.csv")
def start_end(sim_snap_df:str,sim_start,sim_end):
sim_snap_df = sim_snap.groupby('VEHICLE')
sim_start = sim_snap_df.head(1)
sim_end = sim_snap_df.tail(1)
return sim_start,sim_end

##Generate plots.Visualize start and end locations.
def plot_start_end(sim_start,sim_end):

building_map = pd.read_json("/Users/vsundar/Documents/personal/smc/smc-cuda-intersect/data/building_data/Building_Footprints/ChicagoLoop.geojson")
fig,ax = plt.subplots(figsize = (15,15))
building_map.plot(ax=ax)
sim_start_gdf = gpd.GeoDataFrame(sim_start)
##set layer crs
sim_start_gdf.crs = {'init':'epsg:26916'}  






