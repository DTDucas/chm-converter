# HasAssociatedParts Method (Document, LinkElementId) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PartUtils..::..HasAssociatedParts Method (Document, LinkElementId)  
[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.md "PartUtils Class") See Also  
---  
Checks if an element has associated parts. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static bool HasAssociatedParts(
	Document hostDocument,
	LinkElementId hostOrLinkElementId
)
```
  
Visual Basic  
---  
```text
Public Shared Function HasAssociatedParts ( _
	hostDocument As Document, _
	hostOrLinkElementId As LinkElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool HasAssociatedParts(
	Document^ hostDocument, 
	LinkElementId^ hostOrLinkElementId
)
```
  
# ### Parameters
hostDocument
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
hostOrLinkElementId
    Type: [Autodesk.Revit.DB..::..LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md "LinkElementId Class") The element to be checked for associated Parts. 
# ### Return Value
True if the element has associated Parts. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.md "PartUtils Class")
[HasAssociatedParts Overload](55cd42e2-3eca-3592-336c-197c0c525c52.md "HasAssociatedParts Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 