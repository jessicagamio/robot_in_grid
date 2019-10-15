
def get_path(grid):
    """return the path clear of any block"""
    if grid == None or len(grid)==0:
        return None

    path =[]
    block = []

    if eval_grid(grid, len(grid)-1, len(grid[0])-1, path, block):
        return path

def eval_grid(grid, row, col, path, block):
    """return true if path is not blocked"""
    if row<0 or col<0 or grid[row][col] == 'X':
        return false

    curr = grid[row][col]

    if curr in block:
        return false

    elif curr==grid[0][0] or eval_grid(grid, row-1,col, path , block) or eval_grid(grid, row, col-1, path, block):
        path.append(curr)
        return True

    block.append(curr)
    return False





class Test(unittest.TestCase):
    def test_path(self):
        """return path for robot to get from top left to bottom right of grid"""

        grid = [
                        ['0','0','0'],
                        ['0','X','0'],
                        ['X','0','0']
                   ]
        return get_path(grid)

if __name__=="__main__":
    unittest.main()






