

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
IExportContext2D..::..OnElementBegin2D Method   
[IExportContext2D Interface](a4578846-6ecf-e354-668d-96d8ef5d1a32.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
This method marks the beginning of an element to be exported. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2020 

# Syntax

C#  
---  
      
    
    [RenderNodeAction](39f98799-628b-8d65-765c-ca86949ce7ed.md) OnElementBegin2D(
    	[ElementNode](45f8a303-c479-9d6e-c39e-7705169820c2.md) node
    )  
  
Visual Basic  
---  
      
    
    Function OnElementBegin2D ( _
    	node As [ElementNode](45f8a303-c479-9d6e-c39e-7705169820c2.md) _
    ) As [RenderNodeAction](39f98799-628b-8d65-765c-ca86949ce7ed.md)  
  
Visual C++  
---  
      
    
    [RenderNodeAction](39f98799-628b-8d65-765c-ca86949ce7ed.md) OnElementBegin2D(
    	[ElementNode](45f8a303-c479-9d6e-c39e-7705169820c2.md)^ node
    )  
  
#### Parameters

node
    Type: [Autodesk.Revit.DB..::..ElementNode](45f8a303-c479-9d6e-c39e-7705169820c2.md) Node representing the element that is about to start being exported. Contains element ID and document. 

#### Return Value

Return RenderNodeAction.Skip if you wish to skip exporting this element, or return RenderNodeAction.Proceed otherwise. 

# Remarks

For views having non-Wireframe display style, geometry of elements is output outside of view, instance and link begin/end brackets. Therefore the argument to this method is ElementNode that has both element ID and the host document. 

# See Also

[IExportContext2D Interface](a4578846-6ecf-e354-668d-96d8ef5d1a32.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)