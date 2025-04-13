

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PointCloudType..::..Create Method   
[PointCloudType Class](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new point cloud type for a given point cloud engine. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    public static [PointCloudType](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	string engineIdentifier,
    	string typeIdentifier
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	engineIdentifier As String, _
    	typeIdentifier As String _
    ) As [PointCloudType](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md)  
  
Visual C++  
---  
      
    
    public:
    static [PointCloudType](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	String^ engineIdentifier, 
    	String^ typeIdentifier
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document in which to create the point cloud. 

engineIdentifier
    Type: System..::..String The string identifying the engine to be invoked. It should be the file extension or engine identifier registered by the third party. 

typeIdentifier
    Type: System..::..String The file name or the identification string for a non-file based engine. 

#### Return Value

The newly created PointCloudType object to be used to create instances of this point cloud. 

# Remarks

A list of supported engine identifiers and whether they are file-based or not can be obtained from PointCloudEngineRegistry. The method GetSupportedEngines() returns a list of the identifiers registered for engines. 

# Examples

CopyC#
    
    
    private PointCloudInstance CreatePointCloud(Document doc)
    {
        PointCloudType type = PointCloudType.Create(doc, "rcs", "c:\\32_cafeteria.rcs");
        return (PointCloudInstance.Create(doc, type.Id, Transform.Identity));
    }

CopyVB.NET
    
    
    Private Function CreatePointCloud(doc As Document) As PointCloudInstance
        Dim type As PointCloudType = PointCloudType.Create(doc, "rcs", "c:\32_cafeteria.rcs")
        Return (PointCloudInstance.Create(doc, type.Id, Transform.Identity))
    End Function

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The engine identifier was not found in the Revit session. -or- document is not a project document. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.md) | The external file could not be found or loaded. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Unable to create a point cloud from the third party engine. |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[PointCloudType Class](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)