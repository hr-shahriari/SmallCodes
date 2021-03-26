"""This definition makes the boundary curve in regions by defining region points.
    Inputs:
        points: The Points in regions we want to make boundary curve

"""
__author__ = "Hamidreza"


import rhinoscriptsyntax as rs
import ghpythonlib.components as ghc
import copy

if len(points):
    
    if len(points) % 2 == 0:
        lst = points
        lst2 = copy.deepcopy(points)
        del lst2[0]
    else:
        lst = points
        lst2 = copy.deepcopy(points)
        lst2.append(points[0])
    
    
    for p in lst:
        
        rs.Command("_CurveBoolean _SelCrv _Enter {0},{1},{2} _Enter".format(p.X,p.Y,p.Z))
        print("_CurveBoolean _SelCrv _Enter {0},{1},{2} _Enter".format(p.X,p.Y,p.Z))
    
    for p in lst2:
        
        rs.Command("_CurveBoolean _SelCrv _Enter {0},{1},{2} _Enter".format(p.X,p.Y,p.Z))
        print("_CurveBoolean _SelCrv _Enter {0},{1},{2} _Enter".format(p.X,p.Y,p.Z))
    
    rs.Command("SelDup")
    rs.Command("_Delete")
