# RemoveGaps Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
NumberingSchema..::..RemoveGaps Method   
[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.md "NumberingSchema Class") See Also  
---  
Removes gaps, if any, in a numbering sequence 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public void RemoveGaps(
	string partition
)
```
  
Visual Basic  
---  
```text
Public Sub RemoveGaps ( _
	partition As String _
)
```
  
Visual C++  
---  
```text
public:
void RemoveGaps(
	String^ partition
)
```
  
# ### Parameters
partition
    Type: System..::..String Name of the partition that identifies the sequence. The sequence must exist. 
# Remarks
Gaps are removed by shifting numbers above each gap down by the amount of numbers skipped in the gap. The lowest number in the sequence will remain unchanged. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The sequence partition does not exist in the schema. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Either the schema or its document cannot be modified at present. |

# See Also
[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.md "NumberingSchema Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 