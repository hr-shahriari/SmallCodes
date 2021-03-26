"""Select Branches of the Data Tree according to the Depth.
    Inputs:
        Tree: input Data Tree
        Depth: Depth of the Data Tree to Select Branches from
        PathNum : Path Number of the branches to select in the selected Depth
    Output:
        Branches: Output Branches"""

__author__ = "Hamidreza"


import Grasshopper.Kernel.Data.GH_Path as path
import Grasshopper.DataTree as DataTree
import System.Object

if Tree and Depth != None and PathNum != None:
    Branches = DataTree[System.Object]()

    dic = {}

    for i in range(len(Tree.Paths)):
        p = str(Tree.Paths[i])
        p = p.strip("{}")
        lst = p.split(";")
        dic[i] = lst

    DepthLen = len(dic[0]) - 1

    PathNumList = []
    for i in range(len(dic.values())):
        PathNumList.append(int(dic[i][Depth]))
    pathMax = max(PathNumList)

    DepthSld = ghenv.Component.Params.Input[1].Sources[0]
    DepthSld.Slider.Maximum = DepthLen
    PathNumSld = ghenv.Component.Params.Input[2].Sources[0]
    
    if PathNumSld.Slider.Value > pathMax:
        PathNumSld.Slider.Value = 0
    
    PathNumSld.Slider.Maximum = pathMax
    
    

    BranchList = []

    for key,val in dic.items():
        if int(val[Depth]) == PathNum:
            BranchList.append(key)

    for i in range(len(BranchList)):
        newPath = path(i)
        Branches.AddRange(Tree.Branch(BranchList[i]), newPath)
