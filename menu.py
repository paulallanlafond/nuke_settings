
import nuke

import explore_this
import pasteToSelected

print('Loading Paul Tools')
menu = nuke.menu('Nuke')
#toolbar = nuke.toolbar('Paul')


for i in [menu]:
    i.addCommand('Paul tools/Paste to selected', 'pasteToSelected.pasteToSelected()', 'ctrl+shift+v')
    i.addCommand('Paul tools/Explore this', 'explore_this.explore_this()')
    i.addCommand('Paul tools/ShiftRGB', "nuke.createNode('ShiftRGB')")
    i.addCommand('Paul tools/PMerge', "nuke.createNode('PMerge')")
