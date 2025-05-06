# CanUnloadItemFiles Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
FabricationConfiguration..::..CanUnloadItemFiles Method   
[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.md "FabricationConfiguration Class") See Also  
---  
Checks if the fabrication item files are already in use and should not be unloaded. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2019 
# Syntax
C#  
---  
```text
public bool CanUnloadItemFiles(
	IList<FabricationItemFile> itemFiles
)
```
  
Visual Basic  
---  
```text
Public Function CanUnloadItemFiles ( _
	itemFiles As IList(Of FabricationItemFile) _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool CanUnloadItemFiles(
	IList<FabricationItemFile^>^ itemFiles
)
```
  
# ### Parameters
itemFiles
    Type: System.Collections.Generic..::..IList<(Of <(<'[FabricationItemFile](ccf31061-ac40-f869-0b9e-834a9c146427.md "FabricationItemFile Class")>)>)> The fabrication item files to unload. 
# ### Return Value
Returns true if the fabrication item files can be unloaded, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.md "FabricationConfiguration Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 