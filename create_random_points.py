
import arcpy
import random
arcpy.env.overwriteOutput = True

# set workspace
arcpy.env.workspace = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb"

if arcpy.Exists("Rare_Plant_Points"):
    arcpy.Delete_management("Rare_Plant_Points")

outGDB = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb"
outName = "Rare_Plant_Points"
conFC = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\Surveyed_Properties"
numPoints = 10
minDistance = "5 Feet"
arcpy.management.CreateRandomPoints(outGDB, outName, conFC, "", numPoints,
                                    minDistance)

arcpy.management.AddField("Rare_Plant_Points", "Common", "TEXT", field_length=64)
arcpy.management.AddField("Rare_Plant_Points", "Scientific", "TEXT", field_length=64)
arcpy.management.AddField("Rare_Plant_Points", "Count", "SHORT")
arcpy.management.AddField("Rare_Plant_Points", "Year", "TEXT", field_length=4)

fc = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\Rare_Plant_Points"


def rand_plant_species():
    rare_plant_list = [
        {"Common Name": "Rocky Mountain Aletes", "Scientific Name": "Aquilegia saximontana"},
        {"Common Name": "Sweet Flag", "Scientific Name": "Acorus calamus"},
        {"Common Name": "Bigtooth Maple", "Scientific Name": "Acer grandidentatum"},
        {"Common Name": "Richardson Needlegrass", "Scientific Name": "Achnatherum richardsonii"},
        {"Common Name": "Dwarf Sand Verbena", "Scientific Name": "Abronia nana var. nana"},
        {"Common Name": "Hoary Mallow", "Scientific Name": "Abutilon incanum"}
    ]

    rand_int = random.randint(0, len(rare_plant_list) - 1)
    return rare_plant_list[rand_int]


def rand_year():
    year_list = ["2020", "2021", "2022", "2023"]
    rand_int = random.randint(0, len(year_list) - 1)

    return year_list[rand_int]


with arcpy.da.UpdateCursor(fc, ["Common", "Scientific", "Count", "Year"]) as cursor:
    for row in cursor:
        species = rand_plant_species()
        row[0] = species.get("Common Name")
        row[1] = species.get("Scientific Name")
        row[2] = random.randint(1, 20)
        row[3] = rand_year()
        cursor.updateRow(row)

print("\nScript Completed!")
