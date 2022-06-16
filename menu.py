
import nuke

import explore_this
import pasteToSelected

print('Loading Paul Tools')
menu = nuke.menu('Nuke')
toolbar = nuke.toolbar('Paul')
for i in (menu, toolbar):
    i.addCommand('Edit/Paste To Selected', 'pasteToSelected.pasteToSelected()', 'ctrl+shift+v', index=10)
    i.addCommand('Edit/explore this', 'explore_this.explore_this()')
