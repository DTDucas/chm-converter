

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
CentralModelException Class  
[Members](013d6963-ddce-0f42-07c2-c6e6cf728509.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The base class for exceptions that are common to both file-based and server-based central models or specific to just file-based central models.

**Namespace:** [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014

# Syntax

C#  
---  
      
    
    [SerializableAttribute]
    public class CentralModelException : [ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md)  
  
Visual Basic  
---  
      
    
    <SerializableAttribute> _
    Public Class CentralModelException _
    	Inherits [ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md)  
  
Visual C++  
---  
      
    
    [SerializableAttribute]
    public ref class CentralModelException : public [ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md)  
  
# Inheritance Hierarchy

System..::..Object System..::..Exception [Autodesk.Revit.Exceptions..::..ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md) Autodesk.Revit.Exceptions..::..CentralModelException [Autodesk.Revit.Exceptions..::..CentralFileCommunicationException](20094e4f-8326-8378-e5bc-452341d131c2.md) [Autodesk.Revit.Exceptions..::..CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.md) [Autodesk.Revit.Exceptions..::..CentralModelAlreadyExistsException](2ffb2cbc-6ab4-c486-b683-96483f33df78.md) [Autodesk.Revit.Exceptions..::..CentralModelContentionException](ad511076-c435-23c1-5720-1205c4ed28b9.md) [Autodesk.Revit.Exceptions..::..CentralModelVersionArchivedException](9b54c5a2-22f3-ac30-3efd-7ef80adff6ea.md) [Autodesk.Revit.Exceptions..::..CheckoutElementsRequestTooLargeException](61162ab4-01c4-cf01-d307-fc45c19ad63d.md) [Autodesk.Revit.Exceptions..::..OutdatedDirectlyOpenedCentralException](d38fd86b-6281-788d-bf20-6b896da2fbbb.md)

# See Also

[CentralModelException Members](013d6963-ddce-0f42-07c2-c6e6cf728509.md)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)