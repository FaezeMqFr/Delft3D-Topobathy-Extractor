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
