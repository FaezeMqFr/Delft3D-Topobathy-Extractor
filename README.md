# Delft3D-Topobathy-Extractor

## Overview

The **Delft3D-Topobathy-Extractor** automates the extraction of topobathymetric data from DEM raster files to grid points used in Delft3D-FM hydrodynamic modeling. It ensures consistent raster projection, grid point sampling, and output export for accurate modeling.

---

## Features

1. **Batch Processing**: Processes multiple DEM raster files in a folder.
2. **Projection Consistency**: Converts all DEMs to WGS84.
3. **Sampling**: Extracts elevation values from DEMs at specified grid points.
4. **Output Export**: Saves sampled data as text files ready for Delft3D-FM.

---

## Requirements

- ArcGIS with **Spatial Analyst Extension** enabled.
- Python with `arcpy` module installed.
- DEM files in `.tif` format.
- A grid coordinate file in plain text format (X and Y coordinates).

---

## Inputs and Outputs

### Inputs:
1. **DEM Folder**: Directory containing DEM raster files.
2. **Coordinate File**: Text file with grid point coordinates (X, Y).
3. **Output Geodatabase**: For intermediate and processed data.
4. **Output Folder**: Directory for text files with sampled data.

### Outputs:
- Text files containing extracted elevation data at grid points.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Delft3D-Topobathy-Extractor.git
   cd Delft3D-Topobathy-Extractor
   
2. Install the required software:
   - Ensure you have ArcGIS installed with the **Spatial Analyst Extension** enabled.
   - Verify that Python and the `arcpy` module are properly configured in your environment.

3. Set up your input data:
   - Place all DEM raster files in a single directory. Ensure they are in `.tif` format.
   - Create a plain text file containing grid point coordinates in the following format:
     ```
     X1,Y1
     X2,Y2
     ...
     ```
   - Ensure the coordinate file and raster files are accessible from your environment.

4. Update the script:
   - Open `Delft3D_Topobathy_Extractor.py` and modify the following paths:
     ```python
     raster_path = r"Path\To\DEM_Rasters"
     coord_file = r"Path\To\mesh_coord.txt"
     output_gdb = r"Path\To\Output_GDB.gdb"
     output_folder = r"Path\To\SampledPoints_Output"
     ```

5. Run the script:
   - Execute the script in an **ArcGIS Python environment**:
     ```bash
     python Delft3D_Topobathy_Extractor.py
     ```

6. Verify the output:
   - Processed text files with sampled topobathy data will be saved in the specified output folder. The files will be named `SamplePoints_0.txt`, `SamplePoints_1.txt`, and so on for each DEM file processed.

---
