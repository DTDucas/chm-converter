

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
INavisworksExporter..::..ValidateExportOptions Method   
[INavisworksExporter Interface](b389017c-d7af-f0a4-7440-e9dc30f47718.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Determines if the inputs are valid, and returns an error message if not. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    bool ValidateExportOptions(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	string folder,
    	string name,
    	[NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.md) options,
    	out string exceptionMessage
    )  
  
Visual Basic  
---  
      
    
    Function ValidateExportOptions ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	folder As String, _
    	name As String, _
    	options As [NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.md), _
    	<OutAttribute> ByRef exceptionMessage As String _
    ) As Boolean  
  
Visual C++  
---  
      
    
    bool ValidateExportOptions(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	String^ folder, 
    	String^ name, 
    	[NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.md)^ options, 
    	[OutAttribute] String^% exceptionMessage
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document to export. 

folder
    Type: System..::..String The folder path. 

name
    Type: System..::..String The file name. 

options
    Type: [Autodesk.Revit.DB..::..NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.md) The export options. 

exceptionMessage
    Type: System..::..String% The message to show in the exception thrown. This is not an end-user visible message, it is a developer message, and does not have to be localized. Ignored if the function returns true. 

#### Return Value

True if the options are valid, false otherwise. 

# See Also

[INavisworksExporter Interface](b389017c-d7af-f0a4-7440-e9dc30f47718.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)