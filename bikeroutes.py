# Name: Jess Strzempko 
# Python Version: 2.7.15
# Assignment: Lab 2 Geoprocessing Using Python

# Description: This script performs two clips and a buffer to generate layers related to the proximity of bike paths to UN office buildings.
# It is used to identify portions of existing bike routes that may be problematic/pose safety concerns by going too close to facilities.
# File paths included in the script are specific to the local computer on which the script was initially run. 
# It was created as Exercise 1 in Lab 2 Geoprocessing using Python for IDCE 30274 Computer Programming for GIS. 

# Inputs: parks.shp [layer of parks], zip.shp [polygon of relevant zipcode]
# facilities.shp [locations of UN office buildings], bike_routes.shp [lines depicting all bike paths]

# Outputs: parks_Clip.shp [intermediary layer of parks clipped to the provided zip code],
# facilities_buffer.shp [a 500-meter buffer around the office buildings/facilities],
# bike_Clip.shp [bike paths clipped to the zip code]

# Process: Clip
# Input Feature: parks.shp
# Clip Feature: zip.shp
# Output Feature: parks_Clip.shp
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab2\\Data_Lab_2_Geoprocessing_Python\\Results\\parks_Clip.shp")

# Import the env class to set environment properties
from arcpy import env
# Set workspace to Data folder for Lab 2
env.workspace = "C:\\Users\\JeStrzempko\\Documents\\Comp_Prog\\Lab2\\Data_Lab_2_Geoprocessing_Python"

# Process: Buffer
# Input Feature: facilities.shp
# Output Feature: facilities_buffer.shp
# Buffer Distance: 500 meters
arcpy.Buffer_analysis("facilities.shp", "Results\\facilities_buffer.shp", "500 METERS")
# Same as above, but with {dissolve_option} set to "ALL" to dissolve all boundaries between individual buffers
arcpy.Buffer_analysis("facilities.shp", "Results\\facilities_buffer.shp", "500 METERS", "", "", "ALL")

# Alternate method
# Create a variable for each of Buffer tool's parameters
in_features = "bike_routes.shp"
clip_features = "zip.shp"
out_features = "bike_Clip.shp"
xy_tolerance = ""
# Run tool using variable names as arguments
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)
