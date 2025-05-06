# CategoryType Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ExportLayerInfo..::..CategoryType Property   
[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.md "ExportLayerInfo Class") See Also  
---  
The category type which this layer belongs to. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public LayerCategoryType CategoryType { get; set; }
```
  
Visual Basic  
---  
```text
Public Property CategoryType As LayerCategoryType
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property LayerCategoryType CategoryType {
	LayerCategoryType get ();
	void set (LayerCategoryType value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.md "ExportLayerInfo Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 