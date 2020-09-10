__author__ = "Emmanuel Daucé, Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
################################################################################
from deck import Slide, Deck
################################################################################

slides = [] # a list of slides
################################################################################
################################################################################
# TITRE
################################################################################
################################################################################
slides.append(Slide(
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
    """],
    duration=6,
    ))
################################################################################
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


slides.append(Slide(
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
slides.append(Slide(
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

slides.append(Slide(
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
# FIN
################################################################################
################################################################################
slides.append(Slide(
    texts = ["""
For more info, and the full, open-sourced code... visit


""", """
For more info, and the full, open-sourced code... visit

https://laurentperrinet.github.io/publication/dauce-20/
""",
],
    fontsizes = [30, 24],
    color='orange',
    duration=6,
))
################################################################################
################################################################################
d = Deck()
clips = d.compositing(slides)
d.compiling(clips)
################################################################################
################################################################################
