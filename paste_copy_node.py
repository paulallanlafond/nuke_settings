import os
from PySide import QtGui
import nuke
import nukescripts


def copy_script():
    nuke.nodeCopy('%clipboard%')
    clipboard = QtGui.QApplication.clipboard()
    script = clipboard.text()
    return script


def paste_script(script, x, y, clear_selection=True):
    if clear_selection:
        nukescripts.clear_selection_recursive()

    clipboard = QtGui.QApplication.clipboard()
    clipboard.setText(script)
    nuke.nodePaste('%clipboard%')

    x1, y1 = 0, 0
    for line in script.split('\n'):
        if not x1 and 'xpos' in line:
            x1 = int(line.split()[-1])
        if not y1 and 'ypos' in line:
            y1 = int(line.split()[-1])

    n = nuke.selectedNodes()[-1]
    x2, y2 = n.xpos(), n.ypos()

    dx, dy = x2 - x1, y2 - y1

    for n in nuke.selectedNodes():
        nx = n.xpos() - dx
        ny = n.ypos() - dy
        n.setXYpos(nx + x, ny + y)
