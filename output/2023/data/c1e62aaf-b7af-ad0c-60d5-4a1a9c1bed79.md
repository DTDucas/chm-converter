# MassLevelData Class (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
MassLevelData Class  
[Members](7ad5d221-ce41-42af-c63e-e868e6ae6aa1.md "MassLevelData Members") See Also  
---  
MassLevelData is a conceptual representation of an occupiable floor (Mass Floor) in a conceptual building model. It is defined by associating a particular level with a particular mass element in a Revit project. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
[ObsoleteAttribute("This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSpace' classes instead.")]
public class MassLevelData : Element
```
  
Visual Basic  
---  
```text
<ObsoleteAttribute("This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSpace' classes instead.")> _
Public Class MassLevelData _
	Inherits Element
```
  
Visual C++  
---  
```text
[ObsoleteAttribute(L"This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSpace' classes instead.")]
public ref class MassLevelData : public Element
```
  
# Remarks
MassLevelData reports metrics, such as floor areas, related to conceptual space planning. MassLevelData contains information, such as ConceptualConstructionType, used as part of the Conceptual Energy Analytical model. The MassLevel data geometry is determined by combining all the geometry of a mass into a single geometry, and then taking the area of intersection with the level of the MassLevelData. 
# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") Autodesk.Revit.DB.Analysis..::..MassLevelData
# See Also
[MassLevelData Members](7ad5d221-ce41-42af-c63e-e868e6ae6aa1.md "MassLevelData Members")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 