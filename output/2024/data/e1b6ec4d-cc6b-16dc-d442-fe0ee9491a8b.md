# ComputeSecondDerivatives Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Face..::..ComputeSecondDerivatives Method   
[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.md "Face Class") See Also  
---  
Returns the second partial derivatives of the face at the specified point.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016
# Syntax
C#  
---  
```text
public FaceSecondDerivatives ComputeSecondDerivatives(
	UV point
)
```
  
Visual Basic  
---  
```text
Public Function ComputeSecondDerivatives ( _
	point As UV _
) As FaceSecondDerivatives
```
  
Visual C++  
---  
```text
public:
FaceSecondDerivatives^ ComputeSecondDerivatives(
	UV^ point
)
```
  
# ### Parameters
point
    Type: [Autodesk.Revit.DB..::..UV](1724be37-059b-91ff-aa74-d1508082f76d.md "UV Class")The parameters to be evaluated, in natural parameterization of the face.
# ### Return Value
The second partial derivatives of the face at the specified point.
# Remarks
It does not take the bounding edge loops into account. 
# See Also
[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.md "Face Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 