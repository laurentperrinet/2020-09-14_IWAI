__author__ = "Emmanuel Daucé, Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
import os
home = os.environ['HOME']
figpath_talk = 'figures'
videoname = "video-abstract"
gifname = videoname + ".gif"
fps = 30

from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip

H, W = 500, 800
H_fig, W_fig = int(H-H/(1.618*3)), int(W-W/(1.618*3))


opt_t = dict(font="Open-Sans-Regular", size=(W,H), method='caption')
opt_st = dict(font="Open-Sans-SemiBold", size=(W,H), method='caption')

clips = []
t = 0
################################################################################
################################################################################
# TITRE
################################################################################
################################################################################
texts = ["""
A dual foveal-peripheral visual processing
model implements efficient saccade selection




""", """
A dual foveal-peripheral visual processing
model implements efficient saccade selection

by Daucé, Albigès and Perrinet


""", """
A dual foveal-peripheral visual processing
model implements efficient saccade selection

by Daucé, Albigès and Perrinet

Journal of Vision (2020)
"""]
txt_opts = dict(align='center', color='white', **opt_t)
duration = 2
for text in texts:
    txt = TextClip(text, fontsize=35, **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clips.append(txt)

################################################################################
slides = []
################################################################################
# INTRO
################################################################################
################################################################################
filenames = []
for i in [0, 4, 8, 9]:
    filenames.append('film_FIX.png')
    filenames.append(f'film_display{i}.png')
    filenames.append(f'film_display{i}_SAC.png')
    filenames.append('film_ANS.png')

slides.append(dict(
    filenames=filenames,
    subtitles = ["Visual search is the common task of looking ...",
               "...for a visual object in a cluttered environment...",
               "In order to test a model of visual search, ",
               "...we consider a simple visual search task, ...",
               "...where an agent tries to identify a target ...",
               "...from a cluttered background..",],
    duration=15,
    ))
################################################################################
################################################################################
# Model
################################################################################
################################################################################
slides.append(dict(
    filenames=['CNS-what-where.png', 'CNS-where-diagram.png'],
    subtitles = ["We consider a separate processing of the central part...",
               "...of the visual field and the periphery...",
               "...similarly to the What and What pathways found ...",
               "...in vision. Finally,  we end up with a simple computational...",
               "...graph for inferring location and identity.",],
    duration=15,
    ))


################################################################################
################################################################################
# Results
################################################################################
################################################################################

slides.append(dict(
    filenames=[f'CNS-saccade-{i}.png' for i in [8, 17, 12, 32, 20, 46, 47]],
    subtitles = ["In most cases, the ``Where'' network can correctly infer...",
               "...the accuracy map of counter-factual saccades (that is, ...",
               "... *before* they are actuated). Sometime, the model will ...",
               "...infer an incorrect prediction, looking for  a digit in noise...",
               "...and sometimes it is the ``What'' network that will fail ...",
               "...to give a correct identification.",],
    duration=15,
    ))


################################################################################
################################################################################
# http://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=compositevideoclip#textclip
txt_opts = dict(fontsize=65, bg_color='white', align='center', **opt_st)
sub_opts = dict(fontsize=28, align='South', color='yellow', **opt_st)

for slide in slides:
    # drawing the list of figures
    fig_duration = slide['duration'] / len(slide['filenames'])
    for filename in slide['filenames']:
        if filename is None:
            clip = TextClip(text, fontsize=35, **txt_opts).set_start(t).set_duration(fig_duration)
        else:
            fname = os.path.join(figpath_talk, filename)
            clip = ImageClip(fname).set_duration(fig_duration)
            clip = clip.set_start(t).set_pos('center').resize(height=H_fig, width=W_fig)
        t += fig_duration
        clips.append(clip)

    # overlaying subtitles
    t_sub = t - slide['duration']
    sub_duration = duration / len(slide['subtitles'])
    for subtitle in slide['subtitles']:
        sub = TextClip(subtitle, **sub_opts).set_start(t_sub).set_duration(sub_duration)
        t_sub += sub_duration
        clips.append(sub)

################################################################################
################################################################################
# FIN
################################################################################
################################################################################
texts = ["""
For more info, and the full, open-sourced code... visit


""", """
For more info, and the full, open-sourced code... visit

https://laurentperrinet.github.io/publication/dauce-20/
""",
]

txt_opts = dict(align='center', **opt_t)
duration = 3
for text, fontsize in zip(texts, [30, 24]):
    txt = TextClip(text, color='orange', fontsize=fontsize, **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clips.append(txt)


video = CompositeVideoClip(clips)
video.write_videofile(videoname + '.mp4', fps=fps)
video.write_gif(gifname, fps=fps)
from pygifsicle import optimize
optimize(gifname)
