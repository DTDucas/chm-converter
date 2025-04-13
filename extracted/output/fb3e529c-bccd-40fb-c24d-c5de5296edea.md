

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
NumberingSchema..::..GetNumberingSchema Method   
[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Returns an instance of the specified Numbering Schema in the given document. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    public static [NumberingSchema](8f2b22da-5963-301f-44d8-10c68828c436.md) GetNumberingSchema(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[NumberingSchemaType](da916345-8494-ff19-96d0-1a2d0377a02e.md) schemaType
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function GetNumberingSchema ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	schemaType As [NumberingSchemaType](da916345-8494-ff19-96d0-1a2d0377a02e.md) _
    ) As [NumberingSchema](8f2b22da-5963-301f-44d8-10c68828c436.md)  
  
Visual C++  
---  
      
    
    public:
    static [NumberingSchema](8f2b22da-5963-301f-44d8-10c68828c436.md)^ GetNumberingSchema(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[NumberingSchemaType](da916345-8494-ff19-96d0-1a2d0377a02e.md)^ schemaType
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) A document to get the numbering schema from. 

schemaType
    Type: [Autodesk.Revit.DB..::..NumberingSchemaType](da916345-8494-ff19-96d0-1a2d0377a02e.md) The type of a built-in schema to get. 

#### Return Value

Instance of the specified schema. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The given schemaType has an invalid Id. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)