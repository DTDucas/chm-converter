# ReinforcementAbbreviationTag Constructor (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ReinforcementAbbreviationTag Constructor   
[ReinforcementAbbreviationTag Class](bf71dcbf-bb5b-07db-9711-e901b109b8e2.md "ReinforcementAbbreviationTag Class") See Also  
---  
Constructs a new ReinforcementAbbreviationTag. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public ReinforcementAbbreviationTag(
	ReinforcementAbbreviationTagType typeTag,
	string abbreviationTag
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	typeTag As ReinforcementAbbreviationTagType, _
	abbreviationTag As String _
)
```
  
Visual C++  
---  
```text
public:
ReinforcementAbbreviationTag(
	ReinforcementAbbreviationTagType typeTag, 
	String^ abbreviationTag
)
```
  
# ### Parameters
typeTag
    Type: [Autodesk.Revit.DB.Structure..::..ReinforcementAbbreviationTagType](55ba9a83-6ce5-c4ec-67dd-52943a87e6f7.md "ReinforcementAbbreviationTagType Enumeration") Defines the type of abbreviation tag. 
abbreviationTag
    Type: System..::..String Defines the abbreviation tag value. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[ReinforcementAbbreviationTag Class](bf71dcbf-bb5b-07db-9711-e901b109b8e2.md "ReinforcementAbbreviationTag Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 