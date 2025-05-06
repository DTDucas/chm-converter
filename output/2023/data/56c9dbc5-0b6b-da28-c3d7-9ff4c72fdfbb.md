# Reset Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
FilteredWorksetIdIterator..::..Reset Method   
[FilteredWorksetIdIterator Class](3d4b2969-fe55-7b1a-bdc0-b60165e12856.md "FilteredWorksetIdIterator Class") See Also  
---  
Resets the iterator to the beginning. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public virtual void Reset()
```
  
Visual Basic  
---  
```text
Public Overridable Sub Reset
```
  
Visual C++  
---  
```text
public:
virtual void Reset()
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The FilteredWorksetCollector that yielded this iterator has been reset by another operation. No further iteration is permitted with this iterator. |

# See Also
[FilteredWorksetIdIterator Class](3d4b2969-fe55-7b1a-bdc0-b60165e12856.md "FilteredWorksetIdIterator Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 