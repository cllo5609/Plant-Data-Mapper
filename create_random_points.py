
import arcpy
import random
arcpy.env.overwriteOutput = True

arcpy.env.workspace = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb"

if arcpy.Exists("Rare_Plant_Points_2020"):
    arcpy.Delete_management("Rare_Plant_Points_2020")
if arcpy.Exists("Rare_Plant_Points_2021"):
    arcpy.Delete_management("Rare_Plant_Points_2021")
if arcpy.Exists("Rare_Plant_Points_2022"):
    arcpy.Delete_management("Rare_Plant_Points_2022")
if arcpy.Exists("Rare_Plant_Points_2023"):
    arcpy.Delete_management("Rare_Plant_Points_2023")

for i in range(0,3):
    year_list = ["2020", "2021", "2022", "2023"]
    outGDB = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb"
    outName = "Rare_Plant_Points_" + year_list[i]
    conFC = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\Surveyed_Properties"
    numPoints = 10
    minDistance = "5 Feet"
    arcpy.management.CreateRandomPoints(outGDB, outName, conFC, "", numPoints,
                                        minDistance)

    arcpy.management.AddField(outName, "Common", "TEXT", field_length=64)
    arcpy.management.AddField(outName, "Scientific", "TEXT", field_length=64)
    arcpy.management.AddField(outName, "Count", "SHORT")
    arcpy.management.AddField(outName, "Year", "TEXT", field_length=4)

    fc = "C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\\" + outName


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

    with arcpy.da.UpdateCursor(fc, ["Common", "Scientific", "Count", "Year"]) as cursor:
        for row in cursor:
            species = rand_plant_species()
            row[0] = species.get("Common Name")
            row[1] = species.get("Scientific Name")
            row[2] = random.randint(1, 20)
            row[3] = year_list[i]
            cursor.updateRow(row)


print("\nScript Completed!")
