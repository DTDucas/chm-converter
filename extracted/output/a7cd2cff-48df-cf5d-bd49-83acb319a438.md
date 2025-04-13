

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
EffectInstance..::..MatchesFormat Method   
[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Tests whether the effect instance is appropriate for the given vertex format. 

**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public bool MatchesFormat(
    	[VertexFormat](a946fa2b-bb1f-202c-38dc-8ae0307bedac.md) vertexFormat
    )  
  
Visual Basic  
---  
      
    
    Public Function MatchesFormat ( _
    	vertexFormat As [VertexFormat](a946fa2b-bb1f-202c-38dc-8ae0307bedac.md) _
    ) As Boolean  
  
Visual C++  
---  
      
    
    public:
    bool MatchesFormat(
    	[VertexFormat](a946fa2b-bb1f-202c-38dc-8ae0307bedac.md)^ vertexFormat
    )  
  
#### Parameters

vertexFormat
    Type: [Autodesk.Revit.DB.DirectContext3D..::..VertexFormat](a946fa2b-bb1f-202c-38dc-8ae0307bedac.md) A vertex format. 

#### Return Value

True if the effect instance is valid for use with the specified vertex format. 

# Remarks

The vertex format may define vertex data that are not used by the effect instance. However, the effect instance can not reference vertex data that do not exist in the vertex format. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.md)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)