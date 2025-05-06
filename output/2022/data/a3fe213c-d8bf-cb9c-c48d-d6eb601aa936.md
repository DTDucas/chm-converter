# Create Method (Document, IList(ElementId), ElementId) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
StructuralConnectionHandler..::..Create Method (Document, IList<(Of <(<'ElementId>)>)>, ElementId)  
[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.md "StructuralConnectionHandler Class") See Also  
---  
Creates a new instance of a Structural Connection Handler, which defines the connection between given elements. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public static StructuralConnectionHandler Create(
	Document document,
	IList<ElementId> idsToConnect,
	ElementId typeId
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	idsToConnect As IList(Of ElementId), _
	typeId As ElementId _
) As StructuralConnectionHandler
```
  
Visual C++  
---  
```text
public:
static StructuralConnectionHandler^ Create(
	Document^ document, 
	IList<ElementId^>^ idsToConnect, 
	ElementId^ typeId
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The Revit document. 
idsToConnect
    Type: System.Collections.Generic..::..IList<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> List of element ids of connected elements. 
typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The type of Structural Connection Handler. 
# ### Return Value
The newly created connection. 
# Remarks
Elements should be of the following structural categories: framings (OST_StructuralFraming), columns (OST_StructuralColumns), walls (OST_Walls), floors (OST_Floors) or foundations (OST_StructuralFoundations). The first of given elements is set as primary one. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | It verifies that we have at least one element id in the list. -or- The type typeId is not a valid StructuralConnectionHandlerType. -or- Missing detailed structural connection service implementation. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.md "StructuralConnectionHandler Class")
[Create Overload](11664f7d-2088-4f39-3ad1-6d4c47839940.md "Create Method")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 