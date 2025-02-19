ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[0;33m"
ANSI_GREEN = "\033[0;32m"
ANSI_GRAY = "\033[0;37m"
ANSI_BLUE = "\033[0;34m"

class Tile:
    def __init__(self, symbol: str, color: str = ANSI_RESET, colored: bool = True):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if colored else symbol


plains  = Tile("|", ANSI_YELLOW)
moutian = Tile("M", ANSI_GRAY)
water   = Tile("O", ANSI_BLUE)
forest  = Tile("T", ANSI_GREEN)