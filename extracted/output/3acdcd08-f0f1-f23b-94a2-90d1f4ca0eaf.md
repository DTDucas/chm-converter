# ViewDisplayDepthCueing Class

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ViewDisplayDepthCueing Class  
[Members](86be30af-5c94-1565-22d7-dd48b113ff7c.md "ViewDisplayDepthCueing Members") Example See Also  
---  
Represents the settings for depth cueing. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public class ViewDisplayDepthCueing : IDisposable
```
  
Visual Basic  
---  
```text
Public Class ViewDisplayDepthCueing _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class ViewDisplayDepthCueing : IDisposable
```
  
# Examples
CopyC#
```text
private void AdjustDepthCueing(View view)
{
    if (view.CanUseDepthCueing())
    {
        using (Transaction t = new Transaction(view.Document, "Change depth cueing"))
        {
            t.Start();
            ViewDisplayDepthCueing depthCueing = view.GetDepthCueing();
            depthCueing.EnableDepthCueing = true;
            depthCueing.FadeTo = 50;    // set fade to percent
            depthCueing.SetStartEndPercentages(0, 75);
            view.SetDepthCueing(depthCueing);
            t.Commit();
        }
    }
}
```

CopyVB.NET
```text
Private Sub AdjustDepthCueing(view As View)
    If view.CanUseDepthCueing() Then
        Using t As New Transaction(view.Document, "Change depth cueing")
            t.Start()
            Dim depthCueing As ViewDisplayDepthCueing = view.GetDepthCueing()
            depthCueing.EnableDepthCueing = True
            depthCueing.FadeTo = 50
            ' set fade to percent
            depthCueing.SetStartEndPercentages(0, 75)
            view.SetDepthCueing(depthCueing)
            t.Commit()
        End Using
    End If
End Sub
```

# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..ViewDisplayDepthCueing
# See Also
[ViewDisplayDepthCueing Members](86be30af-5c94-1565-22d7-dd48b113ff7c.md "ViewDisplayDepthCueing Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)