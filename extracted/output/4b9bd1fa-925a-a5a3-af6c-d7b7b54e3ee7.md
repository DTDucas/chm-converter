

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
UIApplication..::..FabricationPartBrowserChanged Event  
[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Subscribe to MEP Fabrication part browser changed event to be notified when MEP Fabrication part browser is updated. 

**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md)**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public event EventHandler<[FabricationPartBrowserChangedEventArgs](2af49738-a0c3-0e9b-f344-0f39d15dbd49.md)> FabricationPartBrowserChanged  
  
Visual Basic  
---  
      
    
    Public Event FabricationPartBrowserChanged As EventHandler(Of [FabricationPartBrowserChangedEventArgs](2af49738-a0c3-0e9b-f344-0f39d15dbd49.md))  
  
Visual C++  
---  
      
    
    public:
     event EventHandler<[FabricationPartBrowserChangedEventArgs](2af49738-a0c3-0e9b-f344-0f39d15dbd49.md)^>^ FabricationPartBrowserChanged {
    	void add (EventHandler<[FabricationPartBrowserChangedEventArgs](2af49738-a0c3-0e9b-f344-0f39d15dbd49.md)^>^ value);
    	void remove (EventHandler<[FabricationPartBrowserChangedEventArgs](2af49738-a0c3-0e9b-f344-0f39d15dbd49.md)^>^ value);
    }  
  
# Remarks

More docs about the different conditions goes here

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.md)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)