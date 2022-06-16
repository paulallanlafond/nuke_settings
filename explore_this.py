
import os
import subprocess

import nuke


def explore_this():
    node = [node for node in nuke.selectedNodes() if node.Class() in ('Read', 'Write')]
    if not node:
        try:
            directory = os.path.dirname(nuke.root()['name'].value())
            directory = os.path.realpath(directory)
            open_explorer(directory)
            return
        except Exception:
            return
    file_path = node[0]['file'].getEvaluatedValue()
    directory = os.path.dirname(file_path)
    directory = os.path.realpath(directory)
    if os.path.exists(directory):
        open_explorer(directory)


def open_explorer(path):
    subprocess.Popen(r'explorer {}'.format(path))
