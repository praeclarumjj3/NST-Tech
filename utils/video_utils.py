import os
import subprocess


def create_video_from_intermediate_results(results_path, img_format):
    import shutil
    #
    # change this depending on what you want to accomplish (modify out video name, change fps and trim video)
    #
    out_file_name = 'out.mp4'
    fps = 3

    ffmpeg = 'ffmpeg'
    if shutil.which(ffmpeg):  # if ffmpeg is in system path
        img_name_format = '*' + img_format[1]  # example: '%4d.png' for (4, '.png')
        pattern = os.path.join(results_path, img_name_format)
        out_video_path = os.path.join(results_path, out_file_name)

        input_options = ['-r', str(fps), '-pattern_type', 'glob', '-i', str(pattern)]
        encoding_options = ['-c:v', 'libx264', '-crf', '25', '-pix_fmt', 'yuv420p']
        subprocess.call([ffmpeg, *input_options, *encoding_options, out_video_path])
    else:
        print(f'{ffmpeg} not found in the system path, aborting.')
