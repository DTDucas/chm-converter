# Create Method (Document, ElementId, XYZ, Double, String, ElementId) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
TextNote..::..Create Method (Document, ElementId, XYZ, Double, String, ElementId)  
[TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md "TextNote Class") See Also  
---  
Creates a new line-wrapping text note element of the given width and properties. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public static TextNote Create(
	Document document,
	ElementId viewId,
	XYZ position,
	double width,
	string text,
	ElementId typeId
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	viewId As ElementId, _
	position As XYZ, _
	width As Double, _
	text As String, _
	typeId As ElementId _
) As TextNote
```
  
Visual C++  
---  
```text
public:
static TextNote^ Create(
	Document^ document, 
	ElementId^ viewId, 
	XYZ^ position, 
	double width, 
	String^ text, 
	ElementId^ typeId
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") A valid Revit document that is currently modifiable (i.e. with an open transaction). 
viewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") Id of the graphic view in which the note is to be created. 
position
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") A model position of the new note. 
For a left-aligned text (default), the origin is set at the top-left corner of the note's bounding box.
width
    Type: System..::..Double Width [ft] of the text in paper space (i.e. as it is measured when printed.) If a line of text is longer than the specified Width, the text will be automatically wrapped. If a a zero Width is supplied then this method will create an unwrapped text note element. 
text
    Type: System..::..String Text to populate the text note with. 
typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") Id of the text type to use for the new text note. The text type allows its font name parameter to be set to a font unavailable on the current system. However, any text note created with or set to this font type will be displayed in a default substituted font (e.g. Arial) and the UI will show a blank value in the text type font name parameter. Once the document is opened on a system which has the font set on the text type, the text note will display with that font and the UI will show that font in the text type font name parameter. 
# ### Return Value
The newly created text note. 
# Remarks
As a view-specific element the text note will be visible only in the specified view.
The new text note will be created using the given text type, which defines the style. The currently default style can be obtained from the Document.GetDefaultElementTypeId method.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The document is a family that cannot contain text notes. -or- The viewId does not represent a valid graphic view element in the given document. -or- The typeId does not represent a valid text type in the given document. -or- A valid point must not be father then 10 miles (approx. 16 km) from the origin. -or- The given width is not valid. A valid value must be within the range returned by the static methods GetMinimumAllowedWidth and GetMaximumAllowedWidth. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md "TextNote Class")
[Create Overload](7dddec5f-15a3-f835-85ab-0ff677b564db.md "Create Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 