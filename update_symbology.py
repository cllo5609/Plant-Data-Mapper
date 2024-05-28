import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.aprx")
mapx = aprx.listMaps()[0]

fc1 = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\BoCo_Boundary"
mapx.addDataFromPath(fc1)

fc2 = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\County_Owned_Open_Space"
mapx.addDataFromPath(fc2)

fc3 = r"C:\BoCo_Rare_Plants\Projects\BoCoRarePlantsProject\BoCoRarePlantsProject.gdb\Surveyed_Properties"
mapx.addDataFromPath(fc3)

# Boulder County Boundary Layer
lyr1 = mapx.listLayers("BoCo_Boundary")[0]
sym1 = lyr1.symbology

sym1.renderer.symbol.applySymbolFromGallery("Black Outline")
lyr1.symbology = sym1

# County Open Space Layer
lyr2 = mapx.listLayers("County_Owned_Open_Space")[0]
sym2 = lyr2.symbology

sym2.renderer.symbol.applySymbolFromGallery("Gray 60% (Transparent)")
lyr2.symbology = sym2

# Surveyed Properties Layer
lyr3 = mapx.listLayers("Surveyed_Properties")[0]
sym3 = lyr3.symbology
sym3.updateRenderer("UniqueValueRenderer")
sym3.renderer.fields = ["PROP_NAME"]
sym3.renderer.groups[0].heading = "Open Space Properties"
lyr3.symbology = sym3
aprx.save()

lyr4 = mapx.listLayers("Surveyed_Properties")[0]
cim_def = lyr4.getDefinition("V3")
colorRampSymLyr = cim_def.renderer.colorRamp
colorRampSymLyr.minAlpha = 40
colorRampSymLyr.maxAlpha = 40

transMod = cim_def.renderer.defaultSymbol.symbol.symbolLayers[1]
transMod.color.values = [130,130,130,40]

lyr4.setDefinition(cim_def)
aprx.save()

print("\nScript Completed")