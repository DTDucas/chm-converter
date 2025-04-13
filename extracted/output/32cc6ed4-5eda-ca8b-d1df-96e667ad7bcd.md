

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
TextNote..::..Create Method (Document, ElementId, XYZ, Double, String, ElementId)  
[TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new line-wrapping text note element of the given width and properties. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 

# Syntax

C#  
---  
      
    
    public static [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) viewId,
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) position,
    	double width,
    	string text,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) typeId
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	viewId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md), _
    	position As [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md), _
    	width As Double, _
    	text As String, _
    	typeId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) _
    ) As [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md)  
  
Visual C++  
---  
      
    
    public:
    static [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ viewId, 
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^ position, 
    	double width, 
    	String^ text, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ typeId
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) A valid Revit document that is currently modifiable (i.e. with an open transaction). 

viewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) Id of the graphic view in which the note is to be created. 

position
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) A model position of the new note. 

For a left-aligned text (default), the origin is set at the top-left corner of the note's bounding box.

width
    Type: System..::..Double Width [ft] of the text in paper space (i.e. as it is measured when printed.) If a line of text is longer than the specified Width, the text will be automatically wrapped. If a a zero Width is supplied then this method will create an unwrapped text note element. 

text
    Type: System..::..String Text to populate the text note with. 

typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) Id of the text type to use for the new text note. The text type allows its font name parameter to be set to a font unavailable on the current system. However, any text note created with or set to this font type will be displayed in a default substituted font (e.g. Arial) and the UI will show a blank value in the text type font name parameter. Once the document is opened on a system which has the font set on the text type, the text note will display with that font and the UI will show that font in the text type font name parameter. 

#### Return Value

The newly created text note. 

# Remarks

As a view-specific element the text note will be visible only in the specified view.

The new text note will be created using the given text type, which defines the style. The currently default style can be obtained from the Document.GetDefaultElementTypeId method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The document is a family that cannot contain text notes. -or- The viewId does not represent a valid graphic view element in the given document. -or- The typeId does not represent a valid text type in the given document. -or- A valid point must not be father then 10 miles (approx. 16 km) from the origin. -or- The given width is not valid. A valid value must be within the range returned by the static methods GetMinimumAllowedWidth and GetMaximumAllowedWidth. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.md)

[Create Overload](7dddec5f-15a3-f835-85ab-0ff677b564db.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)