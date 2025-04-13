

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ImporterIFCUtils..::..GetLocalFileName Method   
[ImporterIFCUtils Class](63c96f27-12ea-3b90-aa39-515a81c79e33.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Get the local file name, including the path, corresponding to a linked IFC file. This will create a local copy of the IFC file if necessary. 

**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md)**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 

# Syntax

C#  
---  
      
    
    public static string GetLocalFileName(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) aDoc,
    	string fileName
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function GetLocalFileName ( _
    	aDoc As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	fileName As String _
    ) As String  
  
Visual C++  
---  
      
    
    public:
    static String^ GetLocalFileName(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ aDoc, 
    	String^ fileName
    )  
  
#### Parameters

aDoc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document that will contain the IFC link. 

fileName
    Type: System..::..String The original file name and path. 

#### Return Value

The local file name and path corresponding to the input file name. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | Can't process file name. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[ImporterIFCUtils Class](63c96f27-12ea-3b90-aa39-515a81c79e33.md)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)