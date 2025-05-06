# TypeId Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
AlignmentStationLabelSetOptions..::..TypeId Property   
[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.md "AlignmentStationLabelSetOptions Class") See Also  
---  
Specifies the ElementId of the labels' type. The default value is InvalidElementId. in this case, [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.md "CreateSet Method") will throw an exception. 
**Namespace:** [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.md "Autodesk.Revit.DB.Infrastructure Namespace")**Assembly:** Autodesk.CivilAlignments.DBApplication (in Autodesk.CivilAlignments.DBApplication.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021.1 
# Syntax
C#  
---  
```text
public ElementId TypeId { get; set; }
```
  
Visual Basic  
---  
```text
Public Property TypeId As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ TypeId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# Remarks
Recommended types can be found using [IsRecommendedTypeForSet(Element)](df3f1355-5c15-5665-23e6-520ce91c8815.md "IsRecommendedTypeForSet Method") Other valid types can be found using [IsValidType(Element)](ff11b964-e6e7-9dad-fbf1-461244fcf010.md "IsValidType Method"). 
# See Also
[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.md "AlignmentStationLabelSetOptions Class")
[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.md "Autodesk.Revit.DB.Infrastructure Namespace")
Send comments on this topic to 