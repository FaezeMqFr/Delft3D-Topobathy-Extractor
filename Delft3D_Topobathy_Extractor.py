"""
Created on Jun 19, 2024

@author: Faezah Maghsoodifar

This script automates the extraction of topobathymetric data from DEM (Digital Elevation Model) raster files
to specific grid points used in the Delft3D-FM hydrodynamic model. 

Processes include:
1. Checking ArcGIS Spatial Analyst license and initializing the environment.
2. Listing DEM raster files in a specified folder and loading XY grid coordinates.
3. Iteratively copying, projecting rasters, and sampling data to extract elevations.
4. Exporting the sampled data into text files compatible with Delft3D-FM.

Inputs:
- Path to DEM raster files (TIF format)
- Path to grid coordinate file (TXT format)
- Output geodatabase for processing
- Output folder for sampled points as text files

Outputs:
- Text files containing sampled topobathy data for each DEM raster.

Requirements:
- ArcGIS with Spatial Analyst Extension
- Python with arcpy library

Repository: Delft3D-Topobathy-Extractor
"""

# Import modules
import arcpy
from os import listdir

# Check Spatial Analyst license
license = str(arcpy.CheckOutExtension("Spatial"))
if license != 'CheckedOut':
    arcpy.AddError('Spatial analysis license is invalid or has expired.')
    exit()
else:
    arcpy.AddMessage('Spatial analysis license successfully checked out.')

# Overwrite output
arcpy.env.overwriteOutput = True

# ---------------------------------------------------------------------------
# User-defined inputs
# ---------------------------------------------------------------------------
# Define input/output paths
raster_path = r"Path\To\DEM_Rasters"  # Replace with your DEM raster folder path
coord_file = r"Path\To\mesh_coord.txt"  # Replace with grid coordinate file path
output_gdb = r"Path\To\Output_GDB.gdb"  # Replace with output geodatabase path
output_folder = r"Path\To\SampledPoints_Output"  # Replace with folder for sampled points
raster_extension = "tif"

# ---------------------------------------------------------------------------
# Environment settings
arcpy.env.workspace = output_gdb
arcpy.env.newPrecision = "DOUBLE"
arcpy.env.XYResolution = "0.001 Meters"
arcpy.env.cellSize = "MINOF"

# ---------------------------------------------------------------------------
# Load grid coordinate file into GIS
coord_table_name = "Delft3D_Coordinates"
arcpy.TableToTable_conversion(coord_file, output_gdb, coord_table_name)
arcpy.MakeXYEventLayer_management(
    coord_table_name, "Field1", "Field2", "Delft3D_Points",
    "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]]"
)

# ---------------------------------------------------------------------------
# Process rasters and sample data
raster_files = [f for f in listdir(raster_path) if f.endswith('.' + raster_extension)]

for i, raster_file in enumerate(raster_files):
    print(f"Processing {i+1}/{len(raster_files)}: {raster_file}")
    
    # Copy raster
    temp_raster = f"TempRaster_{i}"
    arcpy.CopyRaster_management(f"{raster_path}\\{raster_file}", temp_raster)
    
    # Project raster to WGS84
    projected_raster = f"ProjectedRaster_{i}"
    arcpy.ProjectRaster_management(temp_raster, projected_raster,
                                   "GEOGCS['GCS_WGS_1984']")

    # Delete temporary raster
    arcpy.Delete_management(temp_raster)
    
    # Sample raster data at grid points
    sample_output = f"SamplePoints_{i}"
    arcpy.sa.Sample(projected_raster, "Delft3D_Points", sample_output, "NEAREST")
    
    # Export to text file
    arcpy.TableToTable_conversion(sample_output, output_folder, f"SamplePoints_{i}.txt")
    print(f"Sampled points exported for raster {i+1}.")
    
print("All rasters processed successfully.")
