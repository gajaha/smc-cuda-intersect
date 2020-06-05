##Script to read simulation snapshots departure time and location. Assign agent location to building.
##Global imports
import pandas as pd
import xarray as xr
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import numpy as np

##Read simulation snapshot departure and arrival time. 
# sim_snap = "/Users/vsundar/Documents/personal/smc/smc-cuda-intersect/data/vehicle_data/Simulation_Snapshot/Snapshot_small.csv"
def start_df(sim_snap:str):
sim_snap = pd.read_csv(sim_snap)
sim_snap_df = sim_snap.groupby('VEHICLE')
sim_start = pd.DataFrame(sim_snap_df.head(1))
sim_start.X_COORD = pd.to_numeric(sim_start.X_COORD)
sim_start.Y_COORD = pd.to_numeric(sim_start.Y_COORD)
return sim_start

def end_df(sim_snap:str):
    sim_snap = pd.read_csv(sim_nap)
    sim_snap_df = sim_snap.groupby('VEHICLE')
    sim_end = pd.DataFrame(sim_snap_df.tail(1))
    sim_end.X_COORD = pd.to_numeric(sim_end.X_COORD)
    sim_end.Y_COORD = pd.to_numeric(sim_end.Y_COORD)
return sim_end

##Calculate distance metrics and return vehicle dataframe with agent mapped toi building. 
# This can be extended to a probabilistic metric.
# Calculate Euclidean distances.
building_map= "/Users/vsundar/Documents/personal/smc/smc-cuda-intersect/data/building_data/Building_Footprints/ChicagoLoop_attr.geojson"
def agent_to_building(sim_start,sim_end,building_map):
building_map = gpd.read_file(building_map)
building_map = building_map.to_crs("EPSG:26916")
building_map = building_map.assign(centroid=building_map.centroid)

sim_start_gdf = gpd.GeoDataFrame(sim_start, geometry=gpd.points_from_xy(sim_start.X_COORD,sim_start.Y_COORD))
sim_start_gdf.crs="EPSG:26916"
##Each vehicle maps to multiple buiuldings. find min distance b/w building and vehicle for start and end times.
min_dist = np.empty(len(sim_start_gdf))
# build_index = np.empty(len(sim_start_gdf))
for i, agent in enumerate(sim_start_gdf.geometry):
    ##Get associated building index
    min_dist[i] = np.argmin([agent.distance(centroid) for centroid in building_map.centroid])
sim_start_gdf['building_id'] = min_dist
agent_count = sim_start_gdf.groupby('building_id').count()
build_agent_count = building_map.merge(agent_count.VEHICLE,right_index=True,left_index=True) 
##ADD 1 to move building ID


##Generate plots.Visualize start and end locations.
def plot_start_end(sim_start:str,sim_end:str,building_map:str):
    # building_map = gpd.read_file("/Users/vsundar/Documents/personal/smc/smc-cuda-intersect/data/building_data/Building_Footprints/ChicagoLoop_attr.geojson")
    # building_map= building_map.to_crs("EPSG:26916")
building_map = build_agent_count.to_crs("EPSG:26916")
fig,ax = plt.subplots()


building_map.plot(ax=ax,column="VEHICLE",cmap='hot',vmin=0,vmax=50)
sm = plt.cm.ScalarMappable(cmap='hot', norm=plt.Normalize(vmin=0, vmax=50))
fig.colorbar(sm, ax=ax)
minx, miny, maxx, maxy = building_map.geometry.total_bounds
sim_start_gdf = gpd.GeoDataFrame(sim_start, geometry=gpd.points_from_xy(sim_start.X_COORD,sim_start.Y_COORD))
##set layer crs
sim_start_gdf.crs="EPSG:26916"
sim_start_gdf.plot(ax=ax, marker='o', color='red', markersize=2)
ax.set_xlim(minx - 100, maxx + 100) # added/substracted value is to give some margin around total bounds
ax.set_ylim(miny - 100, maxy + 100)

plt.show()







