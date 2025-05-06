# IsValidSpacingRuleLayout Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
DividedPath..::..IsValidSpacingRuleLayout Method   
[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.md "DividedPath Class") See Also  
---  
Checks that the spacing rule layout enumeration value is valid 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public bool IsValidSpacingRuleLayout(
	SpacingRuleLayout layout
)
```
  
Visual Basic  
---  
```text
Public Function IsValidSpacingRuleLayout ( _
	layout As SpacingRuleLayout _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidSpacingRuleLayout(
	SpacingRuleLayout layout
)
```
  
# ### Parameters
layout
    Type: [Autodesk.Revit.DB..::..SpacingRuleLayout](163b0cc7-31f0-68b4-ced5-bea6d3c5abcc.md "SpacingRuleLayout Enumeration")
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.md "DividedPath Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 