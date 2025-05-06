# SetCreateAnalyticalModel Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
EnergyDataSettings..::..SetCreateAnalyticalModel Method   
[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.md "EnergyDataSettings Class") See Also  
---  
If this is true, data, features, and geometry related to the Energy Analytical Model will be created, allowing the energy performance to be analyzed through GreenBuilidingXML. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
[ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyModel' property instead.")]
public void SetCreateAnalyticalModel(
	bool createAnalyticalModel
)
```
  
Visual Basic  
---  
```text
<ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyModel' property instead.")> _
Public Sub SetCreateAnalyticalModel ( _
	createAnalyticalModel As Boolean _
)
```
  
Visual C++  
---  
```text
[ObsoleteAttribute(L"This method is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyModel' property instead.")]
public:
void SetCreateAnalyticalModel(
	bool createAnalyticalModel
)
```
  
# ### Parameters
createAnalyticalModel
    Type: System..::..Boolean True to enable the Energy Analytical Model otherwise. 
# See Also
[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.md "EnergyDataSettings Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 