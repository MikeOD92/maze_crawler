from typing import Tuple
import numpy as np # type: ignore

# Tile graphics structured to be compatable with Console.tiles_rgb.
graphics_dt = np.dtype(
    [
    ("ch",np.int32),
    ("fg","3B"),
    ("bg", "3B"),
    ]
)

# tile scruct used fro staticlly defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over
        ("transparent", np.bool), # True if this tile doesn't block FOV
        ("dark", graphics_dt), # Graphics for when this tiles is not in FOV
    ]
)

def new_tile(
    *, #Enforce use of keywords
    walkable: int, 
    transparent: int,
    dark: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
) -> np.ndarray:
    """ Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255,255,255), (50,50,150)),  
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255,255,255), (0,0,100)),  
)