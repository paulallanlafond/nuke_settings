
import os

import nuke


def main():
    p_merge = nuke.thisNode()
    for input_ in range(p_merge.inputs()):
        export_layer = input_ + 1 if input_ < 2 else input_
        command = "nuke.toNode('{}')['export_layer'].setValue({})".format(p_merge.name(), export_layer)
        if input_ == 2:
            continue
        read = p_merge.input(input_)
        part_name = os.path.basename(read['file'].value().split('.')[0])
        output_directory = r'{}'.format(p_merge['output_path'].value())
        print(p_merge['output_path'].value())
        final_output = '{0}/{1}/{1}.png'.format(output_directory, part_name)
        nuke.nodes.Write(
            inputs=[p_merge],
            beforeRender=command,
            beforeFrameRender=command,
            file_type='png',
            channels='rgba',
            file=final_output,
            create_directories=True,
        )