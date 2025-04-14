# Add Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ExportPatternTable..::..Add Method   
[ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.md "ExportPatternTable Class") See Also  
---  
Inserts a (key,info) pair into Export pattern table. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public void Add(
	ExportPatternKey exportPatternKey,
	ExportPatternInfo exportPatternInfo
)
```
  
Visual Basic  
---  
```text
Public Sub Add ( _
	exportPatternKey As ExportPatternKey, _
	exportPatternInfo As ExportPatternInfo _
)
```
  
Visual C++  
---  
```text
public:
void Add(
	ExportPatternKey^ exportPatternKey, 
	ExportPatternInfo^ exportPatternInfo
)
```
  
# ### Parameters
exportPatternKey
    Type: [Autodesk.Revit.DB..::..ExportPatternKey](8e55a491-0886-37f5-b867-e4eea95276eb.md "ExportPatternKey Class") The export pattern key to be added. 
exportPatternInfo
    Type: [Autodesk.Revit.DB..::..ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.md "ExportPatternInfo Class") The export pattern info to be added. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The key already exists in the table. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.md "ExportPatternTable Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)