# IsCodeSuccess Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
LinkLoadResult..::..IsCodeSuccess Method   
[LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.md "LinkLoadResult Class") See Also  
---  
Check if load result code signifies success. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static bool IsCodeSuccess(
	LinkLoadResultType code
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsCodeSuccess ( _
	code As LinkLoadResultType _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsCodeSuccess(
	LinkLoadResultType code
)
```
  
# ### Parameters
code
    Type: [Autodesk.Revit.DB..::..LinkLoadResultType](11b095e1-24d9-91b9-ae2e-004f67c94d6e.md "LinkLoadResultType Enumeration") Load result code to be verified. 
# ### Return Value
True if LinkLoadResultType argument is success, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.md "LinkLoadResult Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 