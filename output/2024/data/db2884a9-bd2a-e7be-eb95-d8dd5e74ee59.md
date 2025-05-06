# GetFirstCoreLayerIndex Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
CompoundStructure..::..GetFirstCoreLayerIndex Method   
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class") See Also  
---  
Gets the index of the first core layer. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public int GetFirstCoreLayerIndex()
```
  
Visual Basic  
---  
```text
Public Function GetFirstCoreLayerIndex As Integer
```
  
Visual C++  
---  
```text
public:
int GetFirstCoreLayerIndex()
```
  
# ### Return Value
The index of the first core layer. 
# Remarks
This is the index on the exterior side. You can change the shell/core layer boundary using [SetNumberOfShellLayers(ShellLayerType, Int32)](8b8ea4e3-e697-6176-92c0-dc2687723a71.md "SetNumberOfShellLayers Method"). 
# See Also
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 