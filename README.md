# 40 Cities OSMnx/Networkx Dijkstra Adjacency Matrices for Traffic Prediction Graph Convolutional Networks

## About

Adjacency matrices were calculated for 40 cities using sensor data from https://doi.org/10.1038/s41598-019-51539-5 (ETH Zürich). I personally rented a Google Cloud server for roughly 500€ to compute these matrices because we have so few of them in the traffic prediction Data Science community. Since most models in the community are being trained on just these few datasets there's risk for overfitting.

Use remove_missing_sensors.py to remove sensors that aren't in both the matrix and data.

## Terms of Use and Data Refrences
<img src="https://thomasafink.com/wp-content/uploads/2023/08/P8250742-scaled.jpg" width="450" align="right">
To use or publish this data, you must register and follow the terms of use, which can be found at the bottom of the dataset website UTD19 https://utd19.ethz.ch/. The website UTD19 https://utd19.ethz.ch/ and paper must be referenced "Understanding traffic capacity of urban networks" https://doi.org/10.1038/s41598-019-51539-5. It's best to reference the school as well, Eidgenössische Technische Hochschule Zürich (ETH Zürich). 6GB data collected from the sensors is also available when signing up for UTD19 https://utd19.ethz.ch/. 


<i>Loder, A., L. Ambühl, M. Menendez and K.W. Axhausen (2019) Understanding traffic capacity of urban networks, Scientific Reports, 9 (1) 16283. https://doi.org/10.1038/s41598-019-51539-5 </i>

OpenStreetMap https://www.openstreetmap.org/ must also be referenced because the matrices where calculated using OpenStreetMap. If you use any of the Maps you must reference both OpenStreetMap and Mapbox https://www.mapbox.com/ in addition to UTD19.

Furthermore it's probably best practice to also reference cities in publications. Additional data can often be received upon opendata requests from cities. 

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
The optimal Dijkstra distances between each sensor with every other sensor was calculated using OSMnx and NetworkX. Each city includes atleast one normalized and one original matrice with the raw values. Two example Graph Networks visualized:

<img src="https://github.com/ThomasAFink/40_cities_osmnx_adjacency_matrices_for_graph_convolutional_networks/blob/main/adj_matrix/innsbruck/innsbruck_dijkstra_map.jpg?raw=true" width="46%" align="left">

<img src="https://github.com/ThomasAFink/40_cities_osmnx_adjacency_matrices_for_graph_convolutional_networks/blob/main/adj_matrix/essen/essen_dijkstra_map.jpg?raw=true" width="46%" align="right">

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

## The Data
The data can be used for machine learning, but not all cities have enough data. Variables include speed flow and occupancy. I have only tested the Los Angeles dataset with an LSTM-GCN model so far. Accuracy, R2 and Variance were over 90% on par with other datasets such as METR-LA and PEMS-BAY.

<img src="https://raw.githubusercontent.com/ThomasAFink/40_cities_osmnx_adjacency_matrices_for_graph_convolutional_networks/main/img/sensor_1000_predictions_24hrs.jpg" width="46%" align="left">

<img 
src="https://raw.githubusercontent.com/ThomasAFink/40_cities_osmnx_adjacency_matrices_for_graph_convolutional_networks/main/img/sensor_1000_predictions_48hrs.jpg" width="46%" align="right">

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

## More Data Sources

Source: https://github.com/graphhopper/open-traffic-collection

### Global
https://wiki.openstreetmap.org/wiki/TMC#Available_datasets
https://unece.org/transport/transport-statistics/traffic-census-2020
https://telraam.net/#9/48.1497/11.5850
https://www.graphhopper.com/open-source/

### Australia
https://data-exchange.vicroads.vic.gov.au/
https://data-exchange.vicroads.vic.gov.au/docs/services
https://data-exchange.vicroads.vic.gov.au/data-exchange-platform-goes-live

### Canada
British Columbia
https://www.th.gov.bc.ca/trafficData/

### Europe:
https://data.europa.eu/data/datasets?locale=en&query=traffic&page=1
https://www.datex2.eu/

##### Austria:
https://contentportal.asfinag.at/data

##### Belgium:
https://datastore.brussels/web/-
https://www.verkeerscentrum.be/uitwisseling/datex2full-

##### Catalonia:
http://www.gencat.cat/transit/opendata/incidenciesGML.xml

##### Czechia:
https://registr.dopravniinfo.cz/en/

##### Estonia:
https://tarktee.mnt.ee/#/en/datex

##### Finland:
https://www.digitraffic.fi/en/road-traffic/
https://aineistot.vayla.fi/roadworks/roadworks_d2.xml
https://aineistot.vayla.fi/roadworks/roadworks_infoxml.xml
https://aineistot.vayla.fi/painorajoitukset/painorajoitukset_d2.xml

##### France:
https://data.nasdaq.com/data/INSEE-national-institute-of-statistics-and-economic-studies-france
https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/information/?disjunctive.libelle&disjunctive.etat_trafic&disjunctive.libelle_nd_amont&disjunctive.libelle_nd_aval

##### Germany:
https://opendata.muenchen.de/dataset?tags=Fahrrad
https://www.offenedaten-koeln.de/search/type/dataset
https://opendata.duesseldorf.de/dataset/verkehrsmeldungen-mobilit%C3%A4tsdaten
https://opendata.jena.de/group/mobilitat
https://darmstadt.ui-traffic.de/faces/TrafficData.xhtml
https://suche.transparenz.hamburg.de/dataset/geo-online-portal-hamburg
https://geodienste.hamburg.de/HH_WFS_Verkehr_opendata?REQUEST=GetCapabilities&SERVICE=WFS
https://open.nrw/dataset/verkehrszentrale-verkehrsinformationen-der-viz-nrw-fuer-nordrhein-westfalen-1476687235163
https://open.nrw/dataset/verkehrszentrale-verkehrslage-los-1476688071631
https://www.mcloud.de/web/guest/suche/-/results/detail/verkehrsdatenautomatischedauerzhlstellen
https://www.bast.de/DE/Verkehrstechnik/Fachthemen/v2-verkehrszaehlung/Daten/2017_1/Jawe2017.html?nn=1819490
https://mobilithek.info/
https://www.mdm-portal.de/migration/
https://autobahn.api.bund.dev/
https://www.mdm-portal.de/

##### Italy:
https://github.com/noi-techpark/BZtraffic

##### Lithuania:
http://restrictions.eismoinfo.lt/
https://eismoinfo.lt/#!/

##### Luxembourg:
https://www.cita.lu/info_trafic/datex/situationrecord

##### Netherlands:
http://opendata.ndw.nu/
https://gitlab.com/traffxml/vild2ltef

##### Norway:
https://www.vegvesen.no/

##### Poland:
https://gitlab.com/traffxml/traff-gddkia
https://kpd.gddkia.gov.pl/index.php/en/homepage/

##### Slovenia:
https://www.promet.si/en/plugins-for-developers

##### Spain:
https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=33cb30c367e78410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default

##### Sweden:
https://statistik.tkgbg.se//
https://www.trafikverket.se/tjanster/Oppna_data/oppna-data-vi-erbjuder/

##### Switzerland:
https://www.astra.admin.ch/astra/de/home/dokumentation/daten-informationsprodukte/verkehrsdaten.html

##### UK:
https://www.trafficengland.com/services-info
https://www.traffic.gov.scot/datex/
https://www.gov.uk/traffic-counts
https://www.data.gov.uk/dataset/dc18f7d5-2669-490f-b2b5-77f27ec133ad/highways-agency-network-journey-time-and-traffic-flow-data

### USA

Several entries are take from [this stackexchange answer](http://opendata.stackexchange.com/a/1772/12662)

* [nationwide](http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm)
* [Alabama](https://www.dot.state.al.us/maweb/trafficMonitoring/trafficMonitoring.html)
* [Arizona](http://www.azdot.gov/planning/DataandAnalysis)
* [Arlington](https://www.arlingtonva.us/Government/Projects/22202-Data/Traffic-Transit-Data)
* [California](http://traffic-counts.dot.ca.gov/) and https://koordinates.com/layer/109326-california-traffic-volumes-aadt/
* [Chicago](https://data.cityofchicago.org/browse?tags=traffic) or [one specific set](https://data.cityofchicago.org/Transportation/Average-Daily-Traffic-Counts/pfsx-4n4m)
* [Colorado](http://dtdapps.coloradodot.info/otis)
* [Delaware Valley](http://www.dvrpc.org/webmaps/trafficcounts/)
* [Florida](http://www.dot.state.fl.us/planning/statistics/trafficdata/)
* [Indiana](http://www.in.gov/indot/2720.htm)
* [Maine](http://www.maine.gov/mdot/traffic/ytc/)
* [Massachusetts](http://www.massdot.state.ma.us/highway/TrafficVolumeCounts.aspx)
* [Michigan](http://www.michigan.gov/mdot/0,4616,7-151-9615---,00.html) (seems to be no longer available)
* [Minnesota](http://www.dot.state.mn.us/traffic/data/)
* [New York City](https://opendata.cityofnewyork.us/) and [New York](https://www.dot.ny.gov/highway-data-services)
* [North Carolina](http://www.ncdot.gov/projects/trafficsurvey/)
* [Ohio](http://www.dot.state.oh.us/Divisions/Planning/TechServ/traffic/Pages/Traffic-Count-Reports-and-Maps.aspx)
* [Oregon](http://www.oregon.gov/ODOT/td/tdata/Pages/tsm/tvt.aspx)
* [South Carolina](http://www.scdot.org/getting/trafficcounts.aspx)
* [Tennessee](http://www.tdot.state.tn.us/projectplanning/adt.asp) (seems to be no longer available)
* [Washington](http://www.wsdot.wa.gov/mapsdata/travel/annualtrafficreport.htm)
* [Wisconsin](http://wisconsindot.gov/Pages/projects/data-plan/traf-counts/default.aspx)

New York City: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

### Other
https://opentraffic.io/
