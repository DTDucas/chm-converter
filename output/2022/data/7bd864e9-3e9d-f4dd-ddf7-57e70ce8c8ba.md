# DeckProfileId Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CompoundStructureLayer..::..DeckProfileId Property   
[CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.md "CompoundStructureLayer Class") See Also  
---  
The ElementId of the structural deck profile - only for a layer whose function is StructuralDeck. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public ElementId DeckProfileId { get; set; }
```
  
Visual Basic  
---  
```text
Public Property DeckProfileId As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ DeckProfileId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# ### Field Value
The default is InvalidElementId. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.md "CompoundStructureLayer Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 