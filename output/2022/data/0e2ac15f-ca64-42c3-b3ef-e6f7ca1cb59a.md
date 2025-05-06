# CentralModelException Class (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CentralModelException Class  
[Members](013d6963-ddce-0f42-07c2-c6e6cf728509.md "CentralModelException Members") See Also  
---  
The base class for exceptions that are common to both file-based and server-based central models or specific to just file-based central models.
**Namespace:** [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md "Autodesk.Revit.Exceptions Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014
# Syntax
C#  
---  
```text
[SerializableAttribute]
public class CentralModelException : ApplicationException
```
  
Visual Basic  
---  
```text
<SerializableAttribute> _
Public Class CentralModelException _
	Inherits ApplicationException
```
  
Visual C++  
---  
```text
[SerializableAttribute]
public ref class CentralModelException : public ApplicationException
```
  
# Inheritance Hierarchy
System..::..Object System..::..Exception [Autodesk.Revit.Exceptions..::..ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md "ApplicationException Class") Autodesk.Revit.Exceptions..::..CentralModelException [Autodesk.Revit.Exceptions..::..CentralFileCommunicationException](20094e4f-8326-8378-e5bc-452341d131c2.md "CentralFileCommunicationException Class") [Autodesk.Revit.Exceptions..::..CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.md "CentralModelAccessDeniedException Class") [Autodesk.Revit.Exceptions..::..CentralModelAlreadyExistsException](2ffb2cbc-6ab4-c486-b683-96483f33df78.md "CentralModelAlreadyExistsException Class") [Autodesk.Revit.Exceptions..::..CentralModelContentionException](ad511076-c435-23c1-5720-1205c4ed28b9.md "CentralModelContentionException Class") [Autodesk.Revit.Exceptions..::..CentralModelVersionArchivedException](9b54c5a2-22f3-ac30-3efd-7ef80adff6ea.md "CentralModelVersionArchivedException Class") [Autodesk.Revit.Exceptions..::..CheckoutElementsRequestTooLargeException](61162ab4-01c4-cf01-d307-fc45c19ad63d.md "CheckoutElementsRequestTooLargeException Class") [Autodesk.Revit.Exceptions..::..OutdatedDirectlyOpenedCentralException](d38fd86b-6281-788d-bf20-6b896da2fbbb.md "OutdatedDirectlyOpenedCentralException Class")
# See Also
[CentralModelException Members](013d6963-ddce-0f42-07c2-c6e6cf728509.md "CentralModelException Members")
[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md "Autodesk.Revit.Exceptions Namespace")
Send comments on this topic to 