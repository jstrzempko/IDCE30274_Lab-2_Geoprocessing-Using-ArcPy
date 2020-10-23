# Lab 2: Geoprocessing using ArcPy
Due: 30th October 2020

This repo was created to submit files for Lab 2 for IDCE 30274 Computer Programming for GIS taught by Professor Shadrock Roberts at Clark University. It contains: 
* the python script `bikeroutes.py` 
*	an image of the map `bike_paths.png`

This lab was split into 3 parts. In Part 1, students examined tools and toolboxes in ArcGIS to get familiar with the software interface and capabilities. In Part 2, students used the ModelBuilder in ArcMap to create a model that clipped and selected hazardous flood zones in a particular basin. The model was exported as a python script and uploaded to this repo as `flooding.py`. In `flooding.py`, the inputs are `floodzones.shp` and `basin.shp` and the output is `flooding.shp`. In Part 3, the Python window in ArcMap was used to perform geoprocessing methods as practice. In addition, the python script `my_clip.py` was created separately in the Python IDLE on this computer. It clips a lakes layer to the same basin boundary as in Part 2 and was run to demonstrate how geoprocessing outputs can be created independent of the ArcDesktop software using the arcpy library. In the python script `my_clip.py`, the inputs are `lakes.shp` and `basin.shp` and the output is `lakes_myClip.shp`. Once the script was run, the output was opened in ArcMap to see the visual output given below: 

Your README should explain briefly what you did in the lab and clearly list the contents of the repo and explain what it is so that someone who is not in the class can look at your repo and understand both the lab and the outputs. In example, “file.flooding.py is a Python script for use in ArcMap. The script takes some inputs and then outputs something else…” For guidance on things you should include in your readme, or how to structure it nicely using markdown, [see this web page](https://www.makeareadme.com/). 

![](bike_paths.PNG)

# The Code
The two scripts are meant to be run using shapefiles provided for this class with file paths and names specific to the student submission. If questions arise, users can contact Jess Strzempko at JeStrzempko@clarku.edu for more help and further information.
