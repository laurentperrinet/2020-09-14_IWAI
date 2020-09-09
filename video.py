__author__ = "Emmanuel Daucé, Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'

videoname = "video-abstract"
gifname = videoname + ".gif"
fps = 30

from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip

H, W = 500, 800
H_fig, W_fig = int(H-H/(1.618*3)), int(W-W/(1.618*3))


opt_t = dict(font="Open-Sans-Regular", size=(W,H), method='caption')
opt_st = dict(font="Open-Sans-SemiBold", size=(W,H), method='caption')

clip = []
t = 0

# TITRE
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
txt_opts = dict(align='center', color='white', **opt_t) #stroke_color='gray', stroke_width=.5
duration = 2
for text in texts:
    txt = TextClip(text, fontsize=35, **txt_opts).set_start(t).set_duration(duration)
    t += duration
    clip.append(txt)

# FIN
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
    clip.append(txt)


video = CompositeVideoClip(clip)
video.write_videofile(videoname + '.mp4', fps=fps)
video.write_gif(gifname, fps=fps)
from pygifsicle import optimize
optimize(gifname)
