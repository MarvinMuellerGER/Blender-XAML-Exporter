# Local imports
from .tabChange import TabChange

class TabStringManager:
    def __init__(self):
        self.tab_string = ''

    def toString(self):
        return self.tab_string
    
    def edit(self, tab_change):
        if (tab_change == TabChange.Add):
            self.tab_string = self.tab_string + '    '
        elif (tab_change == TabChange.Remove):
            self.tab_string = self.tab_string[:-4]