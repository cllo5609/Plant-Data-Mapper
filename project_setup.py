import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb"

# Select data from Colorado counties where COUNTY is equal to BOULDER
fc_boundary = r"C:\BoCo_Rare_Plants\Data\Colorado_County_Boundaries.shp"
arcpy.Select_analysis(fc_boundary, "BoCo_Boundary", "COUNTY = 'BOULDER'")

# Select data from Boulder County Open Space where the property is county owned
fc_open_space = r"C:\BoCo_Rare_Plants\Data\County_Open_Space.shp"

numFeats = arcpy.GetCount_management(fc_open_space)
print("{0} has {1} feature(s)".format(fc_open_space, numFeats))

arcpy.Select_analysis(fc_open_space, "County_Owned_Open_Space", "OWN_TYPE_C = 'COS'")


# Copies the surveyed properties shape file stored in 'BoCo_Rare_Plants\Data' to the project's geodatabase
shp1 = r"C:\BoCo_Rare_Plants\Data\BoCo_POS_Property.shp"
fc1 = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\Surveyed_Properties"

arcpy.management.CopyFeatures(shp1, fc1)

print("\nScript Completed")