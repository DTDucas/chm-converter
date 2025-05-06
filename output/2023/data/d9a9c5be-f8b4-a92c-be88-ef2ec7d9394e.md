# SetLayerSelection Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
BaseImportOptions..::..SetLayerSelection Method   
[BaseImportOptions Class](75898e94-cff4-fb64-c613-9596599444c4.md "BaseImportOptions Class") See Also  
---  
Set the layers name which user want to import into Revit. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public void SetLayerSelection(
	ICollection<string> layerSelection
)
```
  
Visual Basic  
---  
```text
Public Sub SetLayerSelection ( _
	layerSelection As ICollection(Of String) _
)
```
  
Visual C++  
---  
```text
public:
void SetLayerSelection(
	ICollection<String^>^ layerSelection
)
```
  
# ### Parameters
layerSelection
    Type: System.Collections.Generic..::..ICollection<(Of <(<'String>)>)> The layers imported into Revit. 
# Remarks
If user don't set any layer selection, all layers would be imported into Revit for dgn. But for dwg|dxf, all layers (or visible layers, it is up to visibleLayersOnly was set or not) would be imported into Revit. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[BaseImportOptions Class](75898e94-cff4-fb64-c613-9596599444c4.md "BaseImportOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 