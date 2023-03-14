# 40 Cities OSMnx/Networkx Dijkstra Adjacency Matrices for Traffic Prediction Graph Convolutional Networks

## About

Adjacency matrices were calculated for 40 cities using sensor data from https://doi.org/10.1038/s41598-019-51539-5 (ETH Zürich). I personally rented a Google Cloud server to calculate these matrices because we have so few of them in the traffic prediction Data Science community.

![image](https://user-images.githubusercontent.com/53316058/217098922-fb6fb157-20dd-443f-8faa-217122097361.png)

## Terms of Use and Data Refrences

To use or publish this data, you must register and follow the terms of use, which can be found at the bottom of their dataset website UTD19 https://utd19.ethz.ch/. There website UTD19 https://utd19.ethz.ch/ and paper must be referenced "Understanding traffic capacity of urban networks" https://doi.org/10.1038/s41598-019-51539-5. It's best to reference the school as well, Eidgenössische Technische Hochschule Zürich (ETH Zürich). 10GB data collected from the sensors is also available when signing up for UTD19 https://utd19.ethz.ch/. 

OpenStreetMap https://www.openstreetmap.org/ must also be referenced because the matrices where calculated using OpenStreetMap. If you use any of the Maps you must reference both OpenStreetMap and Mapbox https://www.mapbox.com/ in addition to UTD19.

Furthermore it's probably best practice to also reference cities in publications. Additional data can often be recieved upon opendata requests from cities. 

The code for mapping and calculating the matrices on the other hand is MIT licence. 

## Installation to Run the Code

    Python 3.10.6
    pip3 install osmnx==0.16.1
    pip3 install shapely==1.8.0
    pip3 install scipy
    pip3 install networkx
    pip3 install pandas
    pip3 install geopandas==0.9.0
    pip3 install -U kaleido
    pip3 install plotly

## Tutorials
Tutorials for the code have been provided on Medium by Thomas A. Fink.

Creating an Adjacency Matrix Using the Dijkstra Algorithm for Graph Convolutional Networks GCNs
https://thomasafink.medium.com/creating-an-adjacency-matrix-using-the-dijkstra-algorithm-for-graph-convolutional-networks-gcns-cc84c37e297
https://github.com/ThomasAFink/osmnx_adjacency_matrix_for_graph_convolutional_networks


Plotting the Optimal Route for Data Scientists in Python using the Dijkstra Algorithm
https://thomasafink.medium.com/plotting-the-optimal-route-for-data-scientists-in-python-using-the-dijkstra-algorithm-14e3e9383a0a
https://github.com/ThomasAFink/optimal_path_dijkstra_for_data_science

## The Graph Neural Networks
The optimal Dijkstra distances between each sensor with every other sensor was calculated using OSMnx and NetworkX. Each city includes atleast one normalized and one original matrice with the raw values. The Graph Networks for each city are visualized.

<img src="https://github.com/ThomasAFink/mfd_traffic_congestion_for_data_scientists/blob/main/output/mfd_speed_flow.jpg?raw=true" width="50%" align="right">

<img src="https://github.com/ThomasAFink/mfd_traffic_congestion_for_data_scientists/blob/main/output/mfd_speed_flow.jpg?raw=true" width="50%" align="right">
