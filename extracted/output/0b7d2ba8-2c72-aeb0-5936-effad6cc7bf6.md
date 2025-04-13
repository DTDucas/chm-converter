

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ConnectorElement..::..CreatePipeConnector Method (Document, PipeSystemType, Reference, Edge)  
[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Create a new pipe ConnectorElement with a face and an edge. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    public static [ConnectorElement](cd7d7579-1058-e8ca-d55a-c3a914843667.md) CreatePipeConnector(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.md) pipeSystemType,
    	[Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md) planarFace,
    	[Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.md) edge
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function CreatePipeConnector ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	pipeSystemType As [PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.md), _
    	planarFace As [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md), _
    	edge As [Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.md) _
    ) As [ConnectorElement](cd7d7579-1058-e8ca-d55a-c3a914843667.md)  
  
Visual C++  
---  
      
    
    public:
    static [ConnectorElement](cd7d7579-1058-e8ca-d55a-c3a914843667.md)^ CreatePipeConnector(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.md) pipeSystemType, 
    	[Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md)^ planarFace, 
    	[Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.md)^ edge
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document to add the connector to. 

pipeSystemType
    Type: [Autodesk.Revit.DB.Plumbing..::..PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.md) The PipeSystemType of the connector. 

planarFace
    Type: [Autodesk.Revit.DB..::..Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md) The planar face to place the connector on. 

edge
    Type: [Autodesk.Revit.DB..::..Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.md) One of the edges in the edge loop that defines the connector location on the planar face. 

#### Return Value

The pipe ConnectorElement. 

# Remarks

Regenerates the document. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The reference is not a planar face. -or- document is not a family document. -or- Thrown when the edge does not belong to the face. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Connector creation is not allowed in this family. |
  
# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.md)

[CreatePipeConnector Overload](c6188202-bd11-204d-de6e-afa1c6799d50.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)