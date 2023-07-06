# Local imports
from .xamlWriter import XamlWriter
from .tabStringManager import TabStringManager
from .tabChange import TabChange

class WriterWithTabs:
    def __init__(self):
        self.writer = XamlWriter()
        self.tab_string_manager = TabStringManager()
        
    def toString(self):
        return self.writer.toString()
    
    def write(self, text):
        self.writer.write(text)

    def write_with_2tabs(self, text, tab_change_before_this_line, tab_change_after_this_line):
        if (tab_change_before_this_line != TabChange.NoChange):
            self.tab_string_manager.edit(tab_change_before_this_line)
        self.write(f'{self.tab_string_manager.toString()}{text}')
        if (tab_change_after_this_line != TabChange.NoChange):
            self.tab_string_manager.edit(tab_change_after_this_line)
    
    def write_with_tabs(self, text, tab_change = TabChange.NoChange, tab_change_before_this_line = True):
        if tab_change_before_this_line:
            self.write_with_2tabs(text, tab_change, TabChange.NoChange)
        else:
            self.write_with_2tabs(text, TabChange.NoChange, tab_change)
    
    def write_line_with_2tabs(self, line, tab_change_before_this_line, tab_change_after_this_line):
        self.write_with_2tabs(f'{line}\n', tab_change_before_this_line, tab_change_after_this_line)

    def write_line(self, line = '', tab_change = TabChange.NoChange, tab_change_before_this_line = True):
        self.write_with_tabs(f'{line}\n', tab_change, tab_change_before_this_line)