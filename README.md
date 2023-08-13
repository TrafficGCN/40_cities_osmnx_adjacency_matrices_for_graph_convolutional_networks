# 40 Cities OSMnx/Networkx Dijkstra Adjacency Matrices for Traffic Prediction Graph Convolutional Networks

## About

Adjacency matrices were calculated for 40 cities using sensor data from https://doi.org/10.1038/s41598-019-51539-5 (ETH Zürich). I personally rented a Google Cloud server to calculate these matrices because we have so few of them in the traffic prediction Data Science community.

## Terms of Use and Data Refrences
<img src="https://thomasafink.com/wp-content/uploads/2023/08/P8250742-scaled.jpg" width="450" align="right">
To use or publish this data, you must register and follow the terms of use, which can be found at the bottom of their dataset website UTD19 https://utd19.ethz.ch/. There website UTD19 https://utd19.ethz.ch/ and paper must be referenced "Understanding traffic capacity of urban networks" https://doi.org/10.1038/s41598-019-51539-5. It's best to reference the school as well, Eidgenössische Technische Hochschule Zürich (ETH Zürich). 10GB data collected from the sensors is also available when signing up for UTD19 https://utd19.ethz.ch/. 

OpenStreetMap https://www.openstreetmap.org/ must also be referenced because the matrices where calculated using OpenStreetMap. If you use any of the Maps you must reference both OpenStreetMap and Mapbox https://www.mapbox.com/ in addition to UTD19.

Furthermore it's probably best practice to also reference cities in publications. Additional data can often be recieved upon opendata requests from cities. 

The code for mapping and calculating the matrices on the other hand is MIT licence. 

## Tutorials
Tutorials for the code have been provided on Medium by Thomas A. Fink.

Creating an Adjacency Matrix Using the Dijkstra Algorithm for Graph Convolutional Networks GCNs
https://thomasafink.medium.com/creating-an-adjacency-matrix-using-the-dijkstra-algorithm-for-graph-convolutional-networks-gcns-cc84c37e297
https://github.com/ThomasAFink/osmnx_adjacency_matrix_for_graph_convolutional_networks


Plotting the Optimal Route for Data Scientists in Python using the Dijkstra Algorithm
https://thomasafink.medium.com/plotting-the-optimal-route-for-data-scientists-in-python-using-the-dijkstra-algorithm-14e3e9383a0a
https://github.com/ThomasAFink/optimal_path_dijkstra_for_data_science

## The Graph Networks
The optimal Dijkstra distances between each sensor with every other sensor was calculated using OSMnx and NetworkX. Each city includes atleast one normalized and one original matrice with the raw values. The Graph Networks for each city are visualized.

<img src="https://github.com/ThomasAFink/40_cities_osmnx_adjacency_matrices_for_graph_convolutional_networks/blob/main/adj_matrix/innsbruck/innsbruck_dijkstra_map.jpg?raw=true" width="46%" align="left">

<img src="https://github.com/ThomasAFink/40_cities_osmnx_adjacency_matrices_for_graph_convolutional_networks/blob/main/adj_matrix/essen/essen_dijkstra_map.jpg?raw=true" width="46%" align="right">
