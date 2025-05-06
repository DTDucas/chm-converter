# None Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PrimarySizeCriterion..::..None Method   
[PrimarySizeCriterion Class](995cd666-6b07-2c7d-9052-6a36be3f7ed8.md "PrimarySizeCriterion Class") See Also  
---  
Creates a criterion with a range of no sizes. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static PrimarySizeCriterion None()
```
  
Visual Basic  
---  
```text
Public Shared Function None As PrimarySizeCriterion
```
  
Visual C++  
---  
```text
public:
static PrimarySizeCriterion^ None()
```
  
# ### Return Value
The new criterion. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also
[PrimarySizeCriterion Class](995cd666-6b07-2c7d-9052-6a36be3f7ed8.md "PrimarySizeCriterion Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 