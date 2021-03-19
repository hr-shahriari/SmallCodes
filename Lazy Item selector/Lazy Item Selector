using System;
using System.Collections;
using System.Collections.Generic;

using Rhino;
using Rhino.Geometry;

using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using Grasshopper.Kernel.Types;



/// <summary>
/// This class will be instantiated on demand by the Script component.
/// </summary>
public class Script_Instance : GH_ScriptInstance
{
#region Utility functions
  /// <summary>Print a String to the [Out] Parameter of the Script component.</summary>
  /// <param name="text">String to print.</param>
  private void Print(string text) { __out.Add(text); }
  /// <summary>Print a formatted String to the [Out] Parameter of the Script component.</summary>
  /// <param name="format">String format.</param>
  /// <param name="args">Formatting parameters.</param>
  private void Print(string format, params object[] args) { __out.Add(string.Format(format, args)); }
  /// <summary>Print useful information about an object instance to the [Out] Parameter of the Script component. </summary>
  /// <param name="obj">Object instance to parse.</param>
  private void Reflect(object obj) { __out.Add(GH_ScriptComponentUtilities.ReflectType_CS(obj)); }
  /// <summary>Print the signatures of all the overloads of a specific method to the [Out] Parameter of the Script component. </summary>
  /// <param name="obj">Object instance to parse.</param>
  private void Reflect(object obj, string method_name) { __out.Add(GH_ScriptComponentUtilities.ReflectType_CS(obj, method_name)); }
#endregion

#region Members
  /// <summary>Gets the current Rhino document.</summary>
  private RhinoDoc RhinoDocument;
  /// <summary>Gets the Grasshopper document that owns this script.</summary>
  private GH_Document GrasshopperDocument;
  /// <summary>Gets the Grasshopper script component that owns this script.</summary>
  private IGH_Component Component; 
  /// <summary>
  /// Gets the current iteration count. The first call to RunScript() is associated with Iteration==0.
  /// Any subsequent call within the same solution will increment the Iteration count.
  /// </summary>
  private int Iteration;
#endregion

  /// <summary>
  /// This procedure contains the user code. Input parameters are provided as regular arguments, 
  /// Output parameters as ref arguments. You don't have to assign output parameters, 
  /// they will have a default value.
  /// </summary>
  private void RunScript(List<System.Object> List, int Index, ref object Item)
  {
    
    // This code were inspired from the discussion in:
    //https://www.grasshopper3d.com/forum/topics/change-number-slider-parameter-using-python?id=2985220%3ATopic%3A630153&page=1#comments
    
    List<System.Object> lst = new List<System.Object>();

    //Checking if the list is connected to the input
    if (List.Count != 0)
    {

      // Check to see if there is no slider, to add the slider
      if (lst.Count == 0 && this.Component.Params.Input[1].SourceCount == 0)
      {
        lst = List;
        Grasshopper.Kernel.Special.GH_NumberSlider slid = new Grasshopper.Kernel.Special.GH_NumberSlider();

        //Sets up default values, to makes sure that slider wouldn't cause crash
        slid.CreateAttributes();

        //slider position in grasshopper canvas
        slid.Attributes.Pivot = new System.Drawing.PointF((float) this.Component.Attributes.DocObject.Attributes.Bounds.Left -
          slid.Attributes.Bounds.Width - 50, this.Component.Attributes.DocObject.Attributes.Bounds.Bottom);


        // This command adds the slider to the grasshopper canvas
        GrasshopperDocument.AddObject(slid, false);

        //Connecting the new added slider to this component
        this.Component.Params.Input[1].AddSource(slid);

        //Changing the slider bounds to match the list length
        Grasshopper.Kernel.Special.GH_NumberSlider sld = (Grasshopper.Kernel.Special.GH_NumberSlider) this.Component.Params.Input[1].Sources[0];
        sld.Slider.Maximum = List.Count - 1;
        sld.Slider.Minimum = 0;
        sld.Slider.DecimalPlaces = 0;

        //Reseting the component so it reads the new input slider
        Component.ExpireSolution(true);
      }

      // Cheking if the list length has changed to change the bound
      if (lst.Count != List.Count)
      {
        lst = List;
        Grasshopper.Kernel.Special.GH_NumberSlider sld = (Grasshopper.Kernel.Special.GH_NumberSlider) this.Component.Params.Input[1].Sources[0];
        sld.Slider.Maximum = List.Count - 1;
        if (sld.Slider.Value > List.Count - 1)
        {
          sld.Slider.Value = 0;
        }
      }

      Item = List[Index];

    }



  }

  // <Custom additional code> 
  

  // </Custom additional code> 

  private List<string> __err = new List<string>(); //Do not modify this list directly.
  private List<string> __out = new List<string>(); //Do not modify this list directly.
  private RhinoDoc doc = RhinoDoc.ActiveDoc;       //Legacy field.
  private IGH_ActiveObject owner;                  //Legacy field.
  private int runCount;                            //Legacy field.
  
  public override void InvokeRunScript(IGH_Component owner, object rhinoDocument, int iteration, List<object> inputs, IGH_DataAccess DA)
  {
    //Prepare for a new run...
    //1. Reset lists
    this.__out.Clear();
    this.__err.Clear();

    this.Component = owner;
    this.Iteration = iteration;
    this.GrasshopperDocument = owner.OnPingDocument();
    this.RhinoDocument = rhinoDocument as Rhino.RhinoDoc;

    this.owner = this.Component;
    this.runCount = this.Iteration;
    this. doc = this.RhinoDocument;

    //2. Assign input parameters
        List<System.Object> List = null;
    if (inputs[0] != null)
    {
      List = GH_DirtyCaster.CastToList<System.Object>(inputs[0]);
    }
    int Index = default(int);
    if (inputs[1] != null)
    {
      Index = (int)(inputs[1]);
    }



    //3. Declare output parameters
      object Item = null;


    //4. Invoke RunScript
    RunScript(List, Index, ref Item);
      
    try
    {
      //5. Assign output parameters to component...
            if (Item != null)
      {
        if (GH_Format.TreatAsCollection(Item))
        {
          IEnumerable __enum_Item = (IEnumerable)(Item);
          DA.SetDataList(1, __enum_Item);
        }
        else
        {
          if (Item is Grasshopper.Kernel.Data.IGH_DataTree)
          {
            //merge tree
            DA.SetDataTree(1, (Grasshopper.Kernel.Data.IGH_DataTree)(Item));
          }
          else
          {
            //assign direct
            DA.SetData(1, Item);
          }
        }
      }
      else
      {
        DA.SetData(1, null);
      }

    }
    catch (Exception ex)
    {
      this.__err.Add(string.Format("Script exception: {0}", ex.Message));
    }
    finally
    {
      //Add errors and messages... 
      if (owner.Params.Output.Count > 0)
      {
        if (owner.Params.Output[0] is Grasshopper.Kernel.Parameters.Param_String)
        {
          List<string> __errors_plus_messages = new List<string>();
          if (this.__err != null) { __errors_plus_messages.AddRange(this.__err); }
          if (this.__out != null) { __errors_plus_messages.AddRange(this.__out); }
          if (__errors_plus_messages.Count > 0) 
            DA.SetDataList(0, __errors_plus_messages);
        }
      }
    }
  }
}
