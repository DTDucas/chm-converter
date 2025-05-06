# GetNumberingSchema Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
NumberingSchema..::..GetNumberingSchema Method   
[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.md "NumberingSchema Class") See Also  
---  
Returns an instance of the specified Numbering Schema in the given document. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public static NumberingSchema GetNumberingSchema(
	Document document,
	NumberingSchemaType schemaType
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetNumberingSchema ( _
	document As Document, _
	schemaType As NumberingSchemaType _
) As NumberingSchema
```
  
Visual C++  
---  
```text
public:
static NumberingSchema^ GetNumberingSchema(
	Document^ document, 
	NumberingSchemaType^ schemaType
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") A document to get the numbering schema from. 
schemaType
    Type: [Autodesk.Revit.DB..::..NumberingSchemaType](da916345-8494-ff19-96d0-1a2d0377a02e.md "NumberingSchemaType Class") The type of a built-in schema to get. 
# ### Return Value
Instance of the specified schema. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The given schemaType has an invalid Id. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.md "NumberingSchema Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 