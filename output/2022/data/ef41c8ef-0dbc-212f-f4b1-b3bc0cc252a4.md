# Reset Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CurveByPointsArrayIterator..::..Reset Method   
[CurveByPointsArrayIterator Class](b9e33d5d-c5f1-2feb-8533-e82977da7f35.md "CurveByPointsArrayIterator Class") See Also  
---  
Bring the iterator back to the start of the array.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
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
  
# ### Implements
IEnumerator..::..Reset()()()()
# Remarks
The Reset method will return the iterator back to the start of the array in line with the definition of IEnumerator. Note that you must call MoveNext before the first item can be accessed via the Current property.
# See Also
[CurveByPointsArrayIterator Class](b9e33d5d-c5f1-2feb-8533-e82977da7f35.md "CurveByPointsArrayIterator Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 