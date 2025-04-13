

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
AnalyticalPanel..::..Create Method (Document, CurveLoop)  
[AnalyticalPanel Class](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new instance of an Analytical Panel within the project. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2023 

# Syntax

C#  
---  
      
    
    public static [AnalyticalPanel](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) aDoc,
    	[CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.md) curveLoop
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	aDoc As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	curveLoop As [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.md) _
    ) As [AnalyticalPanel](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.md)  
  
Visual C++  
---  
      
    
    public:
    static [AnalyticalPanel](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ aDoc, 
    	[CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.md)^ curveLoop
    )  
  
#### Parameters

aDoc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) Revit document. 

curveLoop
    Type: [Autodesk.Revit.DB..::..CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.md) CurveLoop for the Analytical Panel. 

#### Return Value

The newly created AnalyticalPanel instance. 

# Remarks

CurveLoop must be planar and not self-intersecting. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | One of the following requirements is not satisfied : \- curve loop curveLoop is not planar \- curve loop curveLoop is self-intersecting \- curve loop curveLoop contains zero length curves |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[AnalyticalPanel Class](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.md)

[Create Overload](6091562c-c40f-b6ea-962a-4b5bdc21b875.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)