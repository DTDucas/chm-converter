# CopyElements Method (Document, ICollection(ElementId), Document, Transform, CopyPasteOptions) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
ElementTransformUtils..::..CopyElements Method (Document, ICollection<(Of <(<'ElementId>)>)>, Document, Transform, CopyPasteOptions)  
[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.md "ElementTransformUtils Class") See Also  
---  
Copies a set of elements from source document to destination document. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public static ICollection<ElementId> CopyElements(
	Document sourceDocument,
	ICollection<ElementId> elementsToCopy,
	Document destinationDocument,
	Transform transform,
	CopyPasteOptions options
)
```
  
Visual Basic  
---  
```text
Public Shared Function CopyElements ( _
	sourceDocument As Document, _
	elementsToCopy As ICollection(Of ElementId), _
	destinationDocument As Document, _
	transform As Transform, _
	options As CopyPasteOptions _
) As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
static ICollection<ElementId^>^ CopyElements(
	Document^ sourceDocument, 
	ICollection<ElementId^>^ elementsToCopy, 
	Document^ destinationDocument, 
	Transform^ transform, 
	CopyPasteOptions^ options
)
```
  
# ### Parameters
sourceDocument
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document that contains the elements to copy. 
elementsToCopy
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> The set of elements to copy. 
destinationDocument
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The destination document to paste the elements into. 
transform
    Type: [Autodesk.Revit.DB..::..Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md "Transform Class") The transform for the new elements. Can be nullNothingnullptra null reference (Nothing in Visual Basic) if no transform is required. 
options
    Type: [Autodesk.Revit.DB..::..CopyPasteOptions](d8f58fd5-2106-7a88-6218-106a30415791.md "CopyPasteOptions Class") Optional settings. Can be nullNothingnullptra null reference (Nothing in Visual Basic) if default settings should be used. 
# ### Return Value
The ids of the newly created copied elements. 
# Remarks
Copies are placed at their respective original locations or locations specified by the optional transformation.
This method can be used for copying non-view specific elements only. For copying view-specific elements, use the view-specific form of the CopyElements method.
The destination document can be the same as the source document.
This method performs rehosting of elements where applicable.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The given element id set is empty. -or- One or more elements in elementsToCopy do not exist in the document. -or- Some of the elements cannot be copied, because they are view-specific. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The elements cannot be copied. |
| [Autodesk.Revit.Exceptions..::..OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.md "OperationCanceledException Class") | User cancelled the operation. |

# See Also
[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.md "ElementTransformUtils Class")
[CopyElements Overload](7b56b5c2-3aff-f42b-ab47-de1f89a1070f.md "CopyElements Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 