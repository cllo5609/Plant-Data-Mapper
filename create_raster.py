import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True

arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb"

for i in range(0, 4):
    year_list = ["2020", "2021", "2022", "2023"]
    if arcpy.Exists("Plant_Count_Raster_" + year_list[i]):
        arcpy.Delete_management("Plant_Count_Raster_" + year_list[i])

    inFeatures = "Rare_Plant_Points_" + year_list[i]
    valField = "Count"
    outRaster = "Plant_Count_Raster_" + year_list[i]
    assignmentType = "SUM"

    arcpy.conversion.PointToRaster(inFeatures, valField, outRaster,
                                   assignmentType)

in_raster1 = "Plant_Count_Raster_2020"
in_raster4 = "Plant_Count_Raster_2023"

if arcpy.Exists("Sum_Count_Raster"):
        arcpy.Delete_management("Sum_Count_Raster")

out_rc_minus_raster = RasterCalculator([in_raster1, in_raster4], ["x", "y"],
                                       "y-x", "FirstOf")
out_rc_minus_raster.save("C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\Sum_Count_Raster")

print("\nScript Completed!")
