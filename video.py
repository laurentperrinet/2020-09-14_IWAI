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
    contents = ["""
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

    *Journal of Vision* (2020)
    """],
    duration=6,
    ))
################################################################################
################################################################################
# INTRO
################################################################################
################################################################################

slides.append(Slide(
    type='figures',
    contents=['charlie_mnist_ZOOM.jpeg', 'charlie_mnist_FOCAL.jpeg'],
    subtitles = ["Visual search is the common task of looking ...",
               "...for a visual object in a cluttered environment...",
               "...such as finding the familiar shape of a ...",
               "...digit taken from the MNIST database and overlaid on ...",
               "...the back of this character. Finding a model for ...",
               "...such a cognitive process is still open...",
               ],
    duration=8,
    ))

contents = []
for i in [0, 4, 8, 9]:
    contents.append('film_FIX.png')
    contents.append(f'film_display{i}.png')
    contents.append(f'film_display{i}_SAC.png')
    # contents.append('film_ANS.png')

slides.append(Slide(
    type='figures',
    contents=contents,
    subtitles = [
               "In order to test a model of visual search, ",
               "...we consider a simple visual search task, ...",
               "...where an agent tries to identify such a target ...",
               "...from a noisy background.",
               "Inspired by the physiology of biological vision...",
               "...we will design a dual foveal-peripheral visual processing.",
                ],
    duration=9,
    ))
################################################################################
################################################################################
# Model
################################################################################
################################################################################
slides.append(Slide(
    type='figures',
    contents=['CNS-what-where.png',
              # 'CNS-where-diagram.png',
              'fig_methods.png',
              ],
    subtitles = ["Indeed, we consider a separate processing of the central part...",
               "...of the visual field and the periphery...",
               "...similarly to the ''What'' and ''Where'' pathways found ...",
               "...in vision. Finally,  we end up with a simple computational...",
               "...graph for inferring location and identity...",
               "...into two independent yet collaborating models.",
               ],
    duration=15,
    ))
################################################################################
################################################################################
# Results
################################################################################
################################################################################

slides.append(Slide(
    type='figures',
    contents=[f'CNS-saccade-{i}.png' for i in [8, 17, 12, 32, 20, 46, 47]],
    subtitles = ["In most cases, the ''Where'' network can correctly infer...",
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
    contents = ["""
For more info, and the full, open-sourced code... visit


""", """
For more info, and the full, open-sourced code... visit

https://laurentperrinet.github.io/publication/dauce-20/
""",
],
    fontsizes = [30, 30],
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
