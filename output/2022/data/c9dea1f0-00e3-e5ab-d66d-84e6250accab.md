# IsPinned Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
MultistoryStairs..::..IsPinned Method   
[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.md "MultistoryStairs Class") See Also  
---  
Checks if a stair is pinned. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public bool IsPinned(
	Stairs stairs
)
```
  
Visual Basic  
---  
```text
Public Function IsPinned ( _
	stairs As Stairs _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsPinned(
	Stairs^ stairs
)
```
  
# ### Parameters
stairs
    Type: [Autodesk.Revit.DB.Architecture..::..Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.md "Stairs Class") A stairs element in this multistory stairs element. 
# ### Return Value
Returns true if the stairs is pinned; otherwise returns false. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The input stairs is not a member of this multistory stairs. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.md "MultistoryStairs Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 