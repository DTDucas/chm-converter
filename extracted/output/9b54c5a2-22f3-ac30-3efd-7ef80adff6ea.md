

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
CentralModelVersionArchivedException Class  
[Members](35a5624c-ec18-7a94-3131-57fd2221f1c3.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Exception is thrown when last central version merged into the local model has been archived in the central model. Reload Latest or Synchronized with Central needs to be conducted before the current failed operation is retried. 

**Namespace:** [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021

# Syntax

C#  
---  
      
    
    [SerializableAttribute]
    public class CentralModelVersionArchivedException : [CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.md)  
  
Visual Basic  
---  
      
    
    <SerializableAttribute> _
    Public Class CentralModelVersionArchivedException _
    	Inherits [CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.md)  
  
Visual C++  
---  
      
    
    [SerializableAttribute]
    public ref class CentralModelVersionArchivedException : public [CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.md)  
  
# Examples

CopyC#
    
    
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

CopyVB.NET
    
    
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

# Inheritance Hierarchy

System..::..Object System..::..Exception [Autodesk.Revit.Exceptions..::..ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.md) [Autodesk.Revit.Exceptions..::..CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.md) Autodesk.Revit.Exceptions..::..CentralModelVersionArchivedException

# See Also

[CentralModelVersionArchivedException Members](35a5624c-ec18-7a94-3131-57fd2221f1c3.md)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)