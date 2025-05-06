# Transaction Class (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Transaction Class  
[Members](8662608c-ff88-05be-778f-e9b80f54cb34.md "Transaction Members") Example See Also  
---  
Transactions are context-like objects that guard any changes made to a Revit model 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public class Transaction : IDisposable
```
  
Visual Basic  
---  
```text
Public Class Transaction _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class Transaction : IDisposable
```
  
# Remarks
Any change to a document can only be made while there is an active transaction open for that document. Changes do not become part of the document until the active transaction is [committed](32714010-7138-f64f-8fde-a310354448e3.md "Commit Method"). Consequently, all changes made in a transaction can be [rolled back](bd1e69e9-961e-1c07-f70a-a29b90c6eb97.md "RollBack Method") either explicitly or implicitly by the transaction's destructor.
A document can have only one transaction open at any given time.
Transactions cannot be started when the document is in read-only mode, either permanently or temporarily. See the Document class methods IsReadOnly and IsModifiable for more details.
Transactions in linked documents are not permitted, for linked documents are not allowed to be modified.
If a transaction was started and not finished yet by the time the Transaction object is about to be disposed, the default destructor will roll it back automatically, thus all changes made to the document while this transaction was open will be discarded. It is not recommended to rely on this default behavior though. Instead, it is advised to always call either [Commit](32714010-7138-f64f-8fde-a310354448e3.md "Commit Method") or [RollBack](bd1e69e9-961e-1c07-f70a-a29b90c6eb97.md "RollBack Method") explicitly before the transaction object gets disposed. Please note that unless invoked explicitly the actual destruction of an object in managed code might not happen until the object is collected by the garbage collector.
# Examples
CopyC#
```text
public void CreatingSketch(UIApplication uiApplication)
{
    Autodesk.Revit.DB.Document document = uiApplication.ActiveUIDocument.Document;
    Autodesk.Revit.ApplicationServices.Application application = uiApplication.Application;

    // Create a few geometry lines. These lines are transaction (not in the model),
    // therefore they do not need to be created inside a document transaction.
    XYZ Point1 = XYZ.Zero;
    XYZ Point2 = new XYZ(10, 0, 0);
    XYZ Point3 = new XYZ(10, 10, 0);
    XYZ Point4 = new XYZ(0, 10, 0);

    Line geomLine1 = Line.CreateBound(Point1, Point2);
    Line geomLine2 = Line.CreateBound(Point4, Point3);
    Line geomLine3 = Line.CreateBound(Point1, Point4);

    // This geometry plane is also transaction and does not need a transaction
    XYZ origin = XYZ.Zero;
    XYZ normal = new XYZ(0, 0, 1);
    Plane geomPlane = Plane.CreateByNormalAndOrigin(normal, origin);

    // In order to a sketch plane with model curves in it, we need
    // to start a transaction because such operations modify the model.

    // All and any transaction should be enclosed in a 'using'
    // block or guarded within a try-catch-finally blocks
    // to guarantee that a transaction does not out-live its scope.
    using (Transaction transaction = new Transaction(document))
    {
       if (transaction.Start("Create model curves") == TransactionStatus.Started)
       {
           // Create a sketch plane in current document
           SketchPlane sketch = SketchPlane.Create(document,geomPlane);

           // Create a ModelLine elements using the geometry lines and sketch plane
           ModelLine line1 = document.Create.NewModelCurve(geomLine1, sketch) as ModelLine;
           ModelLine line2 = document.Create.NewModelCurve(geomLine2, sketch) as ModelLine;
           ModelLine line3 = document.Create.NewModelCurve(geomLine3, sketch) as ModelLine;

           // Ask the end user whether the changes are to be committed or not
           TaskDialog taskDialog = new TaskDialog("Revit");
           taskDialog.MainContent = "Click either [OK] to Commit, or [Cancel] to Roll back the transaction.";
           TaskDialogCommonButtons buttons = TaskDialogCommonButtons.Ok | TaskDialogCommonButtons.Cancel;
           taskDialog.CommonButtons = buttons;

           if (TaskDialogResult.Ok == taskDialog.Show())
           {
               // For many various reasons, a transaction may not be committed
               // if the changes made during the transaction do not result a valid model.
               // If committing a transaction fails or is canceled by the end user,
               // the resulting status would be RolledBack instead of Committed.
               if (TransactionStatus.Committed != transaction.Commit())
               {
                  TaskDialog.Show("Failure", "Transaction could not be committed");
               }
           }
           else
           {
               transaction.RollBack();
           }
       }
    }
}
```

CopyVB.NET
```text
Public Sub CreatingSketch(uiApplication As UIApplication)
    Dim document As Autodesk.Revit.DB.Document = uiApplication.ActiveUIDocument.Document
    Dim application As Autodesk.Revit.ApplicationServices.Application = uiApplication.Application

    ' Create a few geometry lines. These lines are transaction (not in the model),
    ' therefore they do not need to be created inside a document transaction.
    Dim Point1 As XYZ = XYZ.Zero
    Dim Point2 As New XYZ(10, 0, 0)
    Dim Point3 As New XYZ(10, 10, 0)
    Dim Point4 As New XYZ(0, 10, 0)

    Dim geomLine1 As Line = Line.CreateBound(Point1, Point2)
    Dim geomLine2 As Line = Line.CreateBound(Point4, Point3)
    Dim geomLine3 As Line = Line.CreateBound(Point1, Point4)

    ' This geometry plane is also transaction and does not need a transaction
    Dim origin As XYZ = XYZ.Zero
    Dim normal As New XYZ(0, 0, 1)
 Dim geomPlane As Plane = Plane.CreateByNormalAndOrigin(normal, origin)

    ' In order to a sketch plane with model curves in it, we need
    ' to start a transaction because such operations modify the model.

    ' All and any transaction should be enclosed in a 'using'
    ' block or guarded within a try-catch-finally blocks
    ' to guarantee that a transaction does not out-live its scope.
    Using transaction As New Transaction(document)
        If transaction.Start("Create model curves") = TransactionStatus.Started Then
            ' Create a sketch plane in current document
            Dim sketch As SketchPlane = SketchPlane.Create(document, geomPlane)

            ' Create a ModelLine elements using the geometry lines and sketch plane
            Dim line1 As ModelLine = TryCast(document.Create.NewModelCurve(geomLine1, sketch), ModelLine)
            Dim line2 As ModelLine = TryCast(document.Create.NewModelCurve(geomLine2, sketch), ModelLine)
            Dim line3 As ModelLine = TryCast(document.Create.NewModelCurve(geomLine3, sketch), ModelLine)

            ' Ask the end user whether the changes are to be committed or not
            Dim taskDialog__1 As New TaskDialog("Revit")
            taskDialog__1.MainContent = "Click either [OK] to Commit, or [Cancel] to Roll back the transaction."
            Dim buttons As TaskDialogCommonButtons = TaskDialogCommonButtons.Ok Or TaskDialogCommonButtons.Cancel
            taskDialog__1.CommonButtons = buttons

            If TaskDialogResult.Ok = taskDialog__1.Show() Then
                ' For many various reasons, a transaction may not be committed
                ' if the changes made during the transaction do not result a valid model.
                ' If committing a transaction fails or is canceled by the end user,
                ' the resulting status would be RolledBack instead of Committed.
                If TransactionStatus.Committed <> transaction.Commit() Then
                    TaskDialog.Show("Failure", "Transaction could not be committed")
                End If
            Else
                transaction.RollBack()
            End If
        End If
    End Using
End Sub
```

# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..Transaction
# See Also
[Transaction Members](8662608c-ff88-05be-778f-e9b80f54cb34.md "Transaction Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 