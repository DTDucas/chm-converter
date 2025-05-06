# IsSpec Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
SpecUtils..::..IsSpec Method   
[SpecUtils Class](21c660df-947f-4aa4-29f0-f3cd78f62d6c.md "SpecUtils Class") See Also  
---  
Checks whether a ForgeTypeId identifies a spec. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public static bool IsSpec(
	ForgeTypeId specTypeId
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsSpec ( _
	specTypeId As ForgeTypeId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsSpec(
	ForgeTypeId^ specTypeId
)
```
  
# ### Parameters
specTypeId
    Type: [Autodesk.Revit.DB..::..ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md "ForgeTypeId Class") The identifier to check. 
# ### Return Value
True if the ForgeTypeId identifies a spec, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[SpecUtils Class](21c660df-947f-4aa4-29f0-f3cd78f62d6c.md "SpecUtils Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 