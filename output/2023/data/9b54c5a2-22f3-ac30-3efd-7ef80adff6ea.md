# CentralModelVersionArchivedException Class (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
CentralModelVersionArchivedException Class  
[Members](35a5624c-ec18-7a94-3131-57fd2221f1c3.md "CentralModelVersionArchivedException Members") Example See Also  
---  
Exception is thrown when last central version merged into the local model has been archived in the central model. Reload Latest or Synchronized with Central needs to be conducted before the current failed operation is retried. 
**Namespace:** [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md "Autodesk.Revit.Exceptions Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021
# Syntax
C#  
---  
```text
[SerializableAttribute]
public class CentralModelVersionArchivedException : CentralModelException
```
  
Visual Basic  
---  
```text
<SerializableAttribute> _
Public Class CentralModelVersionArchivedException _
	Inherits CentralModelException
```
  
Visual C++  
---  
```text
[SerializableAttribute]
public ref class CentralModelVersionArchivedException : public CentralModelException
```
  
# Examples
CopyC#
```text
void HandleCentralModelVersionArchivedException(Document doc)
{
   FilteredElementCollector collector = new FilteredElementCollector(doc);
   ICollection<ElementId> rooms = collector.WherePasses(new RoomFilter()).ToElementIds();

   try
   {
      ICollection<ElementId> checkoutelements = WorksharingUtils.CheckoutElements(doc, rooms);
   }
   catch (Autodesk.Revit.Exceptions.CentralModelVersionArchivedException)
   {
      TaskDialog dlg = new TaskDialog("Elements can't be checked out")
      {
         MainInstruction = "The local model is out of date. Editing is limited to elements and worksets you own.",
         MainContent = "To check out elements and worksets owned by others, first reload latest or synchronize with the central model.",
      };
      dlg.Show();

      // Reload Latest, to update the local model to latest version
      ReloadLatestOptions rlOptions = new ReloadLatestOptions();
      doc.ReloadLatest(rlOptions);

      rooms = collector.WherePasses(new RoomFilter()).ToElementIds();
      ICollection<ElementId> checkoutelements = WorksharingUtils.CheckoutElements(doc, rooms);

      TaskDialog.Show(
         title: "Elements are checked out",
         mainInstruction: $"{checkoutelements.Count} elements are checked out.");
   }
}
```

CopyVB.NET
```text
Private Sub HandleCentralModelVersionArchivedException(ByVal doc As Document)
    Dim collector As FilteredElementCollector = New FilteredElementCollector(doc)
    Dim rooms As ICollection(Of ElementId) = collector.WherePasses(New RoomFilter()).ToElementIds()

    Try
        Dim checkoutelements As ICollection(Of ElementId) = WorksharingUtils.CheckoutElements(doc, rooms)
    Catch __unusedCentralModelVersionArchivedException1__ As Autodesk.Revit.Exceptions.CentralModelVersionArchivedException
        Dim dlg As TaskDialog = New TaskDialog("Elements can't be checked out") With {
    .MainInstruction = "The local model is out of date. Editing is limited to elements and worksets you own.",
    .MainContent = "To check out elements and worksets owned by others, first reload latest or synchronize with the central model."
}
        dlg.Show()

        ' Reload Latest, to update the local model to latest version
        Dim rlOptions As ReloadLatestOptions = New ReloadLatestOptions()
        doc.ReloadLatest(rlOptions)
        rooms = collector.WherePasses(New RoomFilter()).ToElementIds()
        Dim checkoutelements As ICollection(Of ElementId) = WorksharingUtils.CheckoutElements(doc, rooms)
        TaskDialog.Show(title:="Elements are checked out", mainInstruction:=$"{checkoutelements.Count} elements are checked out.")
    End Try
End Sub
```

# Inheritance Hierarchy
System..::..Object System..::..Exception [Autodesk.Revit.Exceptions..::..ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md "ApplicationException Class") [Autodesk.Revit.Exceptions..::..CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.md "CentralModelException Class") Autodesk.Revit.Exceptions..::..CentralModelVersionArchivedException
# See Also
[CentralModelVersionArchivedException Members](35a5624c-ec18-7a94-3131-57fd2221f1c3.md "CentralModelVersionArchivedException Members")
[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md "Autodesk.Revit.Exceptions Namespace")
Send comments on this topic to 