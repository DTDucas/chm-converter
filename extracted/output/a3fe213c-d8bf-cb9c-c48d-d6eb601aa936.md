

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
StructuralConnectionHandler..::..Create Method (Document, IList<(Of <(<'ElementId>)>)>, ElementId)  
[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new instance of a Structural Connection Handler, which defines the connection between given elements. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public static [StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	IList<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> idsToConnect,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) typeId
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	idsToConnect As IList(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)), _
    	typeId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) _
    ) As [StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.md)  
  
Visual C++  
---  
      
    
    public:
    static [StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	IList<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ idsToConnect, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ typeId
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The Revit document. 

idsToConnect
    Type: System.Collections.Generic..::..IList<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)> List of element ids of connected elements. 

typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) The type of Structural Connection Handler. 

#### Return Value

The newly created connection. 

# Remarks

Elements should be of the following structural categories: framings (OST_StructuralFraming), columns (OST_StructuralColumns), walls (OST_Walls), floors (OST_Floors) or foundations (OST_StructuralFoundations). The first of given elements is set as primary one. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | It verifies that we have at least one element id in the list. -or- The type typeId is not a valid StructuralConnectionHandlerType. -or- Missing detailed structural connection service implementation. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.md)

[Create Overload](11664f7d-2088-4f39-3ad1-6d4c47839940.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)