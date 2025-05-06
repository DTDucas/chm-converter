# GetLabelForDiscipline Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
LabelUtils..::..GetLabelForDiscipline Method   
[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.md "LabelUtils Class") See Also  
---  
Gets the user-visible name for a discipline. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public static string GetLabelForDiscipline(
	ForgeTypeId disciplineTypeId
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetLabelForDiscipline ( _
	disciplineTypeId As ForgeTypeId _
) As String
```
  
Visual C++  
---  
```text
public:
static String^ GetLabelForDiscipline(
	ForgeTypeId^ disciplineTypeId
)
```
  
# ### Parameters
disciplineTypeId
    Type: [Autodesk.Revit.DB..::..ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md "ForgeTypeId Class") Identifier of the discipline. 
# Remarks
The name is obtained in the current Revit language. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Discipline must have a definition. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.md "LabelUtils Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 