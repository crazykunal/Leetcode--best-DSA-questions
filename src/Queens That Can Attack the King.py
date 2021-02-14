
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        BOARD_ROWS = 8
        BOARD_COLS = 8
        def check(r,c,ro,co):
            while (r >= 0 and r < BOARD_ROWS and
                   c >= 0 and c < BOARD_COLS):
                if (r,c) in queens:
                    return (r,c)
                r += ro
                c += co
            return None
        queens = set([(r,c) for r,c in queens])
        res = []
        for ro,co in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            check_res = check(king[0],king[1],ro,co) 
            if check_res != None:
                res.append([check_res[0],check_res[1]])
                if len(check_res) == 8:
                    return res

        return res
