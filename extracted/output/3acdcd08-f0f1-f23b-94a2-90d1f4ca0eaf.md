

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ViewDisplayDepthCueing Class  
[Members](86be30af-5c94-1565-22d7-dd48b113ff7c.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Represents the settings for depth cueing. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public class ViewDisplayDepthCueing : IDisposable  
  
Visual Basic  
---  
      
    
    Public Class ViewDisplayDepthCueing _
    	Implements IDisposable  
  
Visual C++  
---  
      
    
    public ref class ViewDisplayDepthCueing : IDisposable  
  
# Examples

CopyC#
    
    
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

CopyVB.NET
    
    
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

# Inheritance Hierarchy

System..::..Object Autodesk.Revit.DB..::..ViewDisplayDepthCueing

# See Also

[ViewDisplayDepthCueing Members](86be30af-5c94-1565-22d7-dd48b113ff7c.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)