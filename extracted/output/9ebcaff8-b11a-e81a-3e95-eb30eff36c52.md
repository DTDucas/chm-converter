# GetNodeByIndex Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
MEPAnalyticalModelData..::..GetNodeByIndex Method   
[MEPAnalyticalModelData Class](9bb95365-04a3-6c28-5f72-477facd80cbc.md "MEPAnalyticalModelData Class") See Also  
---  
Gets the specified analytical node. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public MEPAnalyticalNode GetNodeByIndex(
	int index
)
```
  
Visual Basic  
---  
```text
Public Function GetNodeByIndex ( _
	index As Integer _
) As MEPAnalyticalNode
```
  
Visual C++  
---  
```text
public:
MEPAnalyticalNode^ GetNodeByIndex(
	int index
)
```
  
# ### Parameters
index
    Type: System..::..Int32 The node index number by their storing sequence, starting from 0. 
# ### Return Value
The returned analytical node. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | The index must range from 0 to GetNumberOfNodes()-1. |

# See Also
[MEPAnalyticalModelData Class](9bb95365-04a3-6c28-5f72-477facd80cbc.md "MEPAnalyticalModelData Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)