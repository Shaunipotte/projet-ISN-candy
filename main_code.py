"""
Created on 16/03/2023
@author: Bleuenn Even, Anaïs Febvre, Shaun Ferrand, Oliwier Ostasz
"""

def gravité(grid):
    """
    Renvoie une liste a laquelle elle a appliquée la gravité sur toutes les cases
    
    Parameters : Grille initiale
    Output : Grille avec gravitée appliquée
    """ 
    for l in range(len(grid),0,-1):
        for c in range(len(grid)):
            if grid[l][c] == 0:
                grid[l][c] = grid[l-1][c]
                grid[l-1][c] = 0
    return(grid)
