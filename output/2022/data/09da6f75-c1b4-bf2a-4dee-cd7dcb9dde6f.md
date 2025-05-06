# CreateNotEqualsRule Method (ElementId, Int32) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ParameterFilterRuleFactory..::..CreateNotEqualsRule Method (ElementId, Int32)  
[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.md "ParameterFilterRuleFactory Class") See Also  
---  
Creates a filter rule that determines whether integer values from the document do not equal a certain value. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public static FilterRule CreateNotEqualsRule(
	ElementId parameter,
	int value
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateNotEqualsRule ( _
	parameter As ElementId, _
	value As Integer _
) As FilterRule
```
  
Visual C++  
---  
```text
public:
static FilterRule^ CreateNotEqualsRule(
	ElementId^ parameter, 
	int value
)
```
  
# ### Parameters
parameter
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") An integer-typed parameter used to get values from the document for a given element. 
value
    Type: System..::..Int32 The user-supplied value against which values from the document will be compared. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.md "ParameterFilterRuleFactory Class")
[CreateNotEqualsRule Overload](c3b622c3-1609-9eb7-b3e7-ec13705a24e8.md "CreateNotEqualsRule Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 