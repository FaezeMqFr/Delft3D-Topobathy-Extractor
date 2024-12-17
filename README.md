# Topobathy Data Extraction for Delft3D-FM

## Overview

This script automates the extraction of topobathymetric data (elevation and bathymetry) from DEM raster files to Delft3D-FM grid points. It iteratively processes raster files, samples elevation values at specified grid points, and saves the output in text format.

---

## Features

1. **Batch Processing**: Processes multiple DEM files at once.
2. **Projection Handling**: Reprojects rasters to WGS84 for consistency.
3. **Sampling**: Extracts elevation values at Delft3D-FM grid coordinates.
4. **Outputs**: Saves sampled data as text files for further analysis.

---

## Requirements

- ArcGIS with **Spatial Analyst Extension** enabled.
- Python with `arcpy` module.
- DEM files in `.tif` format.
- Grid points stored in a text file with X and Y coordinates.

---

## Input/Output

### Inputs:
1. **DEM Files**: Folder containing raster files (`.tif`).
2. **Coordinate File**: Text file with X and Y grid points.
3. **Output Geodatabase**: Workspace for temporary and intermediate data.
4. **Output Folder**: Directory to save final sampled data as text files.

### Outputs:
- Text files containing sampled topobathy values at grid points.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DEM_Topobathy_Sampling.git
   cd DEM_Topobathy_Sampling
