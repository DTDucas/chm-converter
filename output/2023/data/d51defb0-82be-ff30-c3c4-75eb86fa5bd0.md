# IsBindingHandleWithTarget Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
RebarConstraint..::..IsBindingHandleWithTarget Method   
[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.md "RebarConstraint Class") See Also  
---  
Gets the relationship between two RebarConstrainedHandles. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2020.1 
# Syntax
C#  
---  
```text
public bool IsBindingHandleWithTarget()
```
  
Visual Basic  
---  
```text
Public Function IsBindingHandleWithTarget As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsBindingHandleWithTarget()
```
  
# ### Return Value
Returns False if only the constrained RebarConstrainedHandle follows the target. Returns True if the constrained RebarConstrainedHandle and the target bar handle are bound and move together. 
# Remarks
Throws exception for any type of constraint other than 'ToOtherRebar' or if the RebarTargetConstraintType of the constraint is 'HookBend' or 'BarBend'. Will also throw if the target Rebar has the 'Number with Spacing' layout rule and the RebarTargetConstraintType of the constraint is 'OutOfPlaneExtent'. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | RebarConstraint is no longer valid. -or- The RebarConstraint is not of RebarConstraintType 'ToOtherRebar.' -or- The RebarTargetConstraintType is 'HookBend' or 'BarBend'. -or- The RebarTargetConstraintType is 'OutOfPlaneExtent' and the rebar target layout is 'Number with Spacing'. |

# See Also
[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.md "RebarConstraint Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 