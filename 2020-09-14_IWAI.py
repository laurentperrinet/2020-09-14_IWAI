__author__ = "Emmanuel Daucé, Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
DEBUG = True
DEBUG = False

fig_width = 12

import os
home = os.environ['HOME']
figpath_talk = 'figures'
figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')
#
import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv)>1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

from academic.cli import slugify
slugified = slugify(tag)

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_px = 80
height_ratio = .9

meta = dict(
 embed = False,
 draft = False, # show notes etc
 #width= 1600, # phi ratio
 #height= 1000,
 width= 1280, # 4/3 ratio
 height= 1024,
 margin= 0.1618,#
 reveal_path='reveal.js-master/',
 # reveal_path='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.0.2/',
 #reveal_path='https://s3.amazonaws.com/hakim-static/reveal-js/',
 theme='simple',
 bgcolor="white",
 author='Emmanuel Daucé and Laurent Perrinet',
 author_link=f'<a href="https://laurentperrinet.github.io/talk/{slugified}/">Emmanuel Daucé & Laurent Perrinet</a>',
 short_title='Visual search as active inference',
 title='Visual search as active inference',
 conference_url='https://iwaiworkshop.github.io/',
 conference='1st International Workshop on Active Inference',
 short_conference='IWAI*2020',
 location='Ghent (Belgium), gone virtual',
 abstract="""Visual search is an essential cognitive ability, offering a prototypical control problem to be addressed with Active Inference. Under a Naive Bayes assumption, the maximization of the information gain objective is consistent with the separation of the visual sensory flow in two independent pathways, namely the "What" and the "Where" pathways. On the "What" side, the processing of the central part of the visual field (the fovea) provides the current interpretation of the scene, here the category of the target. On the "Where" side, the processing of the full visual field (at lower resolution) is expected to provide hints about future central foveal processing given the potential realization of saccadic movements. A map of the classification accuracies, as obtained by such counterfactual saccades, defines a utility function on the motor space, whose maximal argument prescribes the next saccade. The comparison of the foveal and the peripheral predictions finally forms an estimate of the future information gain, providing a simple and resource-efficient way to implement information gain seeking policies in active vision. This dual-pathway information processing framework is found efficient on a synthetic visual search task and we show here quantitatively the role of the precision encoded within the accuracy map. More importantly, it is expected to draw connections toward a more general actor-critic principle in action selection, with the accuracy of the central processing taking the role of a value (or intrinsic reward) of the previous saccade.""",
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 projects='laurentperrinet',
 time_start = '12:20:00',
 time_end = '12:40:00',
 url=f'https://laurentperrinet.github.io/talk/{slugified}',
 sections=['Motivation',
          'Methods',
          'Results',
          'Conclusion'
          ]
)

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname_qr = os.path.join(figpath_talk, 'qr.png')
if not os.path.isfile(figname_qr):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname_qr, scale=5)

print(meta['sections'])
s = Slides(meta)

# TODO : adapt Acknowledgements
# figpath_people = os.path.join(home, 'ownCNRS/2019-01_LACONEU/people')
url_people = 'https://laurentperrinet.github.io/authors/'
Karl = s.content_imagelet(os.path.join(url_people, 'karl-friston/avatar.jpg'), height_px)
Rick = s.content_imagelet(os.path.join(url_people, 'rick-a.-adams/avatar.jpg'), height_px)
Anna = s.content_imagelet(os.path.join(url_people, 'anna-montagnini/avatar.jpg'), height_px)
LM = s.content_imagelet(os.path.join(url_people, 'laurent-madelain/avatar.png'), height_px)
JB = s.content_imagelet(os.path.join(url_people, 'jean-bernard-damasse/avatar.jpg'), height_px)
Fredo = s.content_imagelet(os.path.join(url_people, 'frederic-chavane/avatar.png'), height_px)
Python = s.content_imagelet('https://www.python.org/static/community_logos/python-powered-h-140x182.png', height_px)
s.meta['Acknowledgements'] =f"""

"""

# <small>
# <h5>Acknowledgements:</h5>
# <ul>
#     <li>Rick Adams and Karl Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
#     <li>Jean-Bernard Damasse and Laurent Madelain - ANR REM</li>
#     <li>Frédéric Chavane - INT</li>
# </ul>
# <BR>
# {Rick}{Karl}{JB}{LM}{Anna}{Fredo}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
# <BR>
#     This work was supported by the <a href="https://laurentperrinet.github.io/project/pace-itn/">PACE-ITN Project</a>.
# </small>
#
# """
i_section = 0
#############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Learning where to look 🏄🏄🏄🏄🏄🏄🏄🏄
#############################################################################
s.open_section()
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
# intro += s.content_imagelet('figures/ins-logo.png',
#                             s.meta['height']*.24,
#                             embed=False)
intro += s.content_imagelet('https://laurentperrinet.github.io/slides.py/figures/troislogos.png',
                            s.meta['height']*.32,
                            embed=False) #bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference} ({short_conference})</a>, {DD}/{MM}/{YYYY} </h4>

{Acknowledgements}
""".format(**meta)
#############################################################################

#############################################################################
#############################################################################
#############################################################################
###################### M O T I V A T I O N S ################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################

####################### SLIDE 1 : TITLE PAGE ########################

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hi, I am Emmanuel Daucé. I will present this work about **modelling**  visual search as active inference. This is a joint work with Laurent Perrinet, from the Institute of Neurosciences la Timone, in Marseille.

Many thanks to the organizers for setting up this first conference on Active Inference.

This work is about the design of an artificial vision system that utilizes active vision principles to guide a visual sensor toward visual targets, like in a classic visual search task.


  Today, I wish to view an important aspect of visual cognitive functions, Visual search, in light of active inference theories. As classicly formalized by past authors like Anne Treisman or Jeremy Wolfe, visual search is the common task of looking for a visual object in a cluttered visual environment...

""")

# TODO : rajouter une slide "lightning talk" : For the 15 and 30 minute talks, the first 3 minutes should consist of a self-contained, high-level overview of the contribution, similar to a spotlight presentation. The workshop organizers may choose to stream just this part of your presentation (depending on the format of the workshop), with the complete recording available for offline viewing before or after the event

####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'scene-observer-1.svg')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""

 So, in visual search, an observer is expected to find a target (cat, a tree or a person...) in a cluttered scene. 
""")


####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'scene-observer-1-1.svg')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""

So, in contrast to computer vision, human and animal vision is active. Eye movements (e.g. saccades) are necessary to analyze a visual scene.
The effect of a saccade is to bring new visual data at the fovea, where the number of photoreceptors is higher. 
This combination of eye movements with visual data processing makes it an ideal testbed for the active inference principles. 
""")


####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'scene-observer-2.svg')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""
    
In order to apply the active inference principles,

First one need a **generative model** that explains how the sensory data is generated from external sources and body movements. 
(in vision, the cause of the visual data is both the content of the scene and the orientation of the eye)

""")

####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'scene-observer-3.svg')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""
Second, one needs **to make predictions**.
In general, the observer predicts that its saccade will improve its understanding of the visual data.

 More precisely, it needs predicts the reduction of surprise after the next saccade. Unfortunately, the surprise reduction can only be measured once the saccade is issued. 

In order to guess the surprise reduction before the actual data read-out, we need to **train** a model.

Assume that the category (or identity) of the stimulus is a variable explaining the visual data, predicting a certain distribution of pixels on the fovea. 

The model is constructed around a quantity called the **information gain**, that is a log difference between two scalar quantities, that is a probability on the target category as it is guessed from the future foveal data (after the saccade) minus the target category as it is guessed from the current foveal data.
(or the future accuracy minus the current accuracy)

** each quantity needs to be trained/guessed from the current visual data **

Then, the agent must bring the fovea toward visual data that will **maximize** the information gain. 

We will see that -given the retinotopic arrangment of photoreceptor, this amounts to guess where an object is *before* knowing axactly what it is,
because it is easier to predict the recognition accuracy than the category itself.
""")

####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'film_display9.png')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""
In order to test those ideas, we consider a simple visual search task, where an agent tries to identify a target from a cluttered background.

we manipulate the contrast and the eccentricity...
""")


####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'fig_methods.svg')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""

**The information gain metric defines a computational architecture, that fits well with the separation of the visual processing into a ventral and a dorsal pathway, with the ventral pathway making a prediction about the current visual data and the dorsal pathway making predictions about the future visual data, for different possible saccades.** 

 The visual processing is separated in two pathway, with the foveal data processed separately from the peripheral data. 
...
On the one side, a ventral pathway predicts the target identity  inspecting the cuirrent foveal data.

On the other side, a dorsal pathway, that utilizes all the peripheral visual data. The prediction takes the form of an **acuracy map**, that predicts the increase of accuracy for different possible saccades. 

Like in mammals, the full visual field is stongly compressed using a retinotopic log-polar encoding.  
This accuracy map is organized radially, with a higher spatial definition at the center than at the periphery. 

This allows to implement a simple accuracy-seeking policy, that drives the eye toward regions with higher visual information. 
This drives the eye toward a new position where the target is categorized from the new foveal data.
 
To learn such dual network we use the success (or not) of this classification to backpropagate the error gradient back in the Where network, in a supervised way.


""")

####################### SLIDE LIGHTNING ##################################
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'lightning-results.svg')],
            title='Visual search as active inference', height=s.meta['height']*height_ratio),
    notes="""
(from left to right)

1. The full visual field

2. After a log polar encoding, the peripheral target is less visible

3. this is the true acuracy map

4. this is the predicted acc map

5. this is the visual data collected at the fovea after the saccade.

Finally, we can quantitatively measure the information gain provided by this dual pathway architecture in function of the eccentricity.

- Considerable increase of the surface of the fovea

- Sub linear processing of the full image

- an increase of the information content, with now both the position and identity information  
    
""")

####################### OUTLINE ########################

title = meta['sections'][i_section]

s.add_slide_outline(i_section,
notes="""
During this talk, I will briefly motivate the study, then detail the formalization path that we have taken here. Then we will present some results of our framework applied on modelling sacades towards visual objects and finally offer some perspectives in the conclusion.


Let's first state the problem faced when adressing visual search in computer vision
""")


####################### SLIDE 2 : GENERAL MOTIVATION #########################

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'CNS-2-general-A.svg')],
    title='Computer vision', height=s.meta['height']*height_ratio),
notes="""
* (OBJECTIVE)

Past 5-10 years have seen a huge development of machine learning/deep learning based image processing, 
indeed artificial vision has been revolutioned by the incredible capability of convolution-based deep networks to capture the semantic content of images/photographs. 
Their success relies on a reduction of parameter complexity through weight sharing  in convolutional neural networks applied over the full image. 
In order to increase the recognition capability, there has been an inflation in the number of layers needed to process the pixel information. 
Finally, the processing of large images can be done at a cost that scales quadratically with the image resolution. 
All regions, even the “boring” ones are systematically scanned and processed in parallel fashion at high computational cost.

TODO : put in words
Typical ML processing :
- bounding boxes around objects of interest
- (at best) Linear scaling in #pixels

""")


####################### SLIDE 2bis : GENERAL MOTIVATION #########################

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'CNS-2-general-B.svg')],
    title='Human vision', height=s.meta['height']*height_ratio),
notes="""
* (OBJECTIVE)

In contrast, when human vision is considered, things work quite differently.
Indeed, human (and animal) vision rely on a non uniform sensor (the retina) that has a very high resolution at the center of fixation and a very poor resolution at the periphery.

Crucially,  human vision is **dynamic**. The scanning of a full visual scene is not done in parallel but sequentially saccade after saccade, and only scene-relevant regions of interest are scanned through saccades. This implies a **decision process** at each step that decides **where to look next**.

We propose here that such a strategy ("non uniform" convolution) allows for an economic processing of images by processing independently the position from the category of objects

""")


#s.add_slide(content=s.content_figures(
#[os.path.join(figpath_talk, 'fig_intro.jpg')],
#        title=title + '- Attention', height=s.meta['height']*height_ratio),
#notes="""
#On the machine learning side, There has been lot of efforts to address the scaling shortcoming.
#
#Shortcuts proposed in the literature:
#- bounding boxes (yolo, fast-RCNN)
#- affine/geometric transform (transformer networks)
#- attention networks : Mnih et al, Recurrent Models of Visual Attention, NIPS 2014 (non
#
#""")

####################### SLIDE 3 : MODELLING #########################

s.add_slide(content=s.content_figures(
#[os.path.join(figpath_talk, 'CNS - Modelling - I.svg')],
  [os.path.join(figpath_talk, 'CNS - Modelling - I.png')],
        title='Statistical Viewpoint', height=s.meta['height']*height_ratio),
notes="""
This kind of reasoning can be captured by a statistical framework called a POMDP (partially observed Markov Decision Process) where the cause of a visual field is couple made of a viewpoint and scene elements. Changing the viewpoint will conduct to a different scene rendering. Knowing the current view, you need to choose the next viewpoint that will help you to disambiguate the scene.

In a classic inference framework, a (generative) model tells how typically looks the visual field knowing the scene elements and a certain viewpoint . Using bayes rule, you may then infer the scene elements from the current view point (model inversion).

The more viewpoints you have, the more certain you are about the content of the scene.

""")
####################### SLIDE 4 : MODELLING (CONTINUED) #########################
# author, year, journal, title='', url=None
bib = s.content_bib("Laurent Itti and Christof Koch", "2000", "Vision Research", url="http://ilab.usc.edu/publications/doc/Itti_Koch00vr.pdf")

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS - Modelling - II.svg')],
        title='Attention vs. Scene Understanding', height=s.meta['height']*height_ratio),
notes="""

Given a generative model of the environment, one can define a quantity called the bayesian surprise that tells how different is the visual data from your initial guess.
Itti and Koch predict that that the eye is attracted by the bayesian surprise, i.e. by the regions of the image that depart the most from the baseline image statistics.
This allows to define salient regions in an image and draw saliency maps over an image that can predict where the eye is attracted the most.  This may explain up to 50% of the human scan path, but it is purely phenomenological.


- Laurent Itti and Christof Koch. **A saliency-based search mechanism
    for overt and covert shifts of visual attention**. In: Vision
    Research 40.10-12 (2000), pp. 1489--1506.
- M. Kümmerer, L. Theis, and M. Bethge **Deep Gaze I: Boosting
    Saliency Prediction with Feature Maps Trained on ImageNet** ICLR
    Workshop, 2015


Top down : (sequential decision)

A more detailed modelling originally proposed by Najemnik and Geisler proposes a sequential model of natural vision in a visual search task. Given a generative model of the visual field (an ideal observer that knows everything about how the visual data is generated), and given a statistics over the hypothesis space (Where is Waldo?), the model decides **where to look next** : choose the next viewpoint that will provide the best **information gain**. The selection is reiterated several times until enough evidence is gathered.

In general, the active inference setup means using a generative model to quantify the benefit of doing a certain action (changing viewpoint) to reduce the **posterior entropy** given an history of past actions (viewpoints), that corresponds to a better understanding of the visual scene.




- J Najemnik and Wilson S. Geisler. **Optimal eye movement
        strategies in visual search**. In: Nature reviews. Neuroscience
        434 (2005)
- Nicholas J Butko and Javier R Movellan. **Infomax control of eye
        movements**. In: Autonomous Mental Development, IEEE
        Transactions on 2.2 (2010)
- Fu, J., Zheng, H., & Mei, T. (2017). Look closer to see better: Recurrent attention convolutional neural network for fine-grained image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 4438-4446).
""")

s.close_section()

i_section = 1
#############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄     METHODS         🏄🏄🏄🏄🏄🏄🏄🏄
#############################################################################
#############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
Indeed, we will use the separation of the 2 problemes (where and what) as they are confronted to nuisances of different kinds


""")


url =  'full code @ <a href="https://github.com/SpikeAI/2020-09-14_IWAI/">github.com/SpikeAI/2020-09-14_IWAI/</a>'

####################### SLIDE B 0 ##################################

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-what-where-principles.svg' )],
    title='Principles for central and peripheric vision',
    height=s.meta['height']*height_ratio),
notes="""

So what we propose here is to go a little further in a biomimetic implementation of an artificial vision system.
(Why : biomimetic systems are the result of a continual optimization throughout ages of evolution: they optimize signal processing under strong material and energy constraints, for specific surfival purposes.)

Objective : build an effective artificial foveal vision
We concentrate her on the foveal vision case


What is specific with foveal vision?
Foveal vision is a trick that was selected by natural selection : a compromise between resource saving and accuracy (budgeted vision)
The fovea that concentrates most of the photoreceptors, represents less than 2% of the total visual field
In a foveal vision setting, the current view may allow you to tell there is an object of interest in your peripheral vision (for instance a face),that you can not identify, and you need to make a saccade to
identify the person.

So in order to analyze a complex visual scene, there are two types of processing that need to be done. On the one side, you need  to process in detail what is at the center of fixation, that is the region of interest currently processed. On the other side, you also need to analyze the surrounding part, even if the resolution is low, in order to choose what is the next position of fixation. This basically means making a choice of “what’s interesting next”. You do not necessarily need to know what it is, but you need to that it’s interesting enough, and of course you need to know what action to take to move the center of fixation at the right position.

If we consider now the information gain metric, it shows an interesting correspondence with the central/peripheral processing trade-off. In a sequential setup, the rightmost term can be interpreted as the current state if understanding before the saccade is actuated, that is the information present at the center of the retina -- and the left term can be seen as the future state of understanding after the saccade is executed, that relies on interpreting the peripheral information.

""")

####################### SLIDE B 1 ##################################

if not os.path.isfile('figures/film_FIX.png'):
    import sys
    sys.path.append('../WhereIsMyMNIST/figures')
    import matplotlib.pyplot as plt
    import numpy as np

    from main import init
    #args = init(filename='debug')
    args = init(filename='../WhereIsMyMNIST/2019-03-27')
    args.contrast = 0.5
    from display import Display
    d = Display(args)
    data, label = next(iter(d.loader_test))

    figsize = (16, 12) # (16, 10)
    N_plot = 12

    for i in range(N_plot):
        opts = dict(ms=24, markeredgewidth=1, alpha=.4)
        opts_save = dict(pad_inches=0.03) #
        data_fullfield, i_offset, j_offset = d.draw(data[i+42, 0, :, :].numpy())

        fig, ax = plt.subplots(1, 1, figsize=figsize)
        ax = d.show(ax, data_fullfield, do_cross=True)
        ax.plot([args.N_pic//2], [args.N_pic//2], '*r', **opts)
        ax.set_xticks([])
        ax.set_yticks([])
        fig.savefig(f'figures/film_display{i}.png', **opts_save)
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        ax = d.show(ax, data_fullfield, do_cross=True)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.plot([args.N_pic//2+j_offset], [args.N_pic//2+i_offset], '*r', **opts)
        ax.arrow(args.N_pic//2, args.N_pic//2, j_offset, i_offset, width=.3, color='r',
                 head_width=4., length_includes_head=True, edgecolor='k')
        fig.savefig(f'figures/film_display{i}_SAC.png', **opts_save)
        plt.close('all')

    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.imshow(.5 + np.zeros_like(data_fullfield), cmap=plt.gray(), vmin=0, vmax=1)
    ax.plot([args.N_pic//2], [args.N_pic//2], '+', color='b', ms=24, markeredgewidth=4)
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig('figures/film_FIX.png', **opts_save)

    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.imshow(.5 + np.zeros_like(data_fullfield), cmap=plt.gray(), vmin=0, vmax=1)
    ax.text(args.N_pic//2, args.N_pic//2, '?', color='b', fontsize=42, ha='center', va='center')
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig('figures/film_ANS.png', **opts_save)

for i in [0, 4, 8, 9]:
    s.add_slide(image_fname='figures/film_FIX.png')
    s.add_slide(image_fname=f'figures/film_display{i}.png')
    s.add_slide(image_fname=f'figures/film_display{i}_SAC.png')
    s.add_slide(image_fname='figures/film_ANS.png')

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'fig_intro.jpg')],
        title=title + " - ''Experimental'' setup", height=s.meta['height']*height_ratio*.8),
notes="""


We reproduce in simulation the conditions of a psychophysic experiment.

The problem is to identify a digit that is placed at random over a noisy background, that is : finding the target identity. The agent fixates the center of the screen should give an answer about which digit was present in the image.
This corresponds to a classic environment control in psychophysic experiments.
Different parameters are controlled, such as the target eccentricity, the background noise and the contrast, in order to var the difficulty of the task.

(B) the agent can make a saccade, in which case the center of fixation moves toward the expected location of the target.

(C) The agent subjective perception is shown on the lower right part. The larger the target eccentrity, the more difficult the identifiction. There is a range of eccentricities for wich it is impossible to identify the target from a single glance, so that a sacade is necessary to issue a propoer response.


""")

####################### SLIDE B 1.5 ##################################

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-what-where.svg')],
        title=title + ": What/Where separation", height=s.meta['height']*height_ratio),
notes="""
Consider our simplified visual scene containing a non-centered digit over a noisy background. We consider a separate processing of the central part of the visual field and the periphery, corresponding to a central and peripheral processing consistently with information-gain based action selection.

We consider in our setup a slight simplification, that is sampling the prior and the posterior on the true label.
The information gain becomes the difference of the future accuracy and the central accuracy.
The accuracy here takes the role of a proxy for the posterior entropy.
Importantly, the future accuracy is a score that does not predict the future label. It just tells how correct the response will be while doing saccade a.

The separation into current accuracy and future accuracy is reminiscent of the What/where visual processing separation observed in monkeys and humans... with a separate processing of the object detailed shape and identity through the ventral pathway and the visuo-spatial information through the dorsal pathway.
Here we interpret the what/where separation in a slightly different manner, with the what devoted to analyzing the central part of the visual field, and the where devoted to choosing the next saccade.
The "Where" is not exactly where but rather: where should I look next in order to increase my accuracy?
""")



####################### SLIDE B 2, 3 & 4 ##################################
subtitle = [': Computational Graph', ': What', ': Where']
for i, fname in enumerate(['CNS-what-where-diagram', 'CNS-what-diagram', 'CNS-where-diagram']):
    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, fname + '.svg')],
            title=title + subtitle[i], height=s.meta['height']*height_ratio),
    notes="""

    COMPUTATIONAL GRAPH :
    Here is the general computational graph of our active vision system.
    Two streams of information are separated from the visual primary layers, one stream for processing the central pixels only, the other for processing the periphery with a logpolar encoding. The two streams converge toward a decision layer that compares the central and the peripheral acuracy, in order to decide wether to issue a saccadic or a categorical response. If a saccade is produced, then the center of vision is displaced toward the region that shows the higher accuracy on the accuracy map.

    WHAT :
    At the core of the vision system is the identification module (the what).   The what pathway is a classic convolutional clasifier.
It shows some translation invariance. It can quantify its uncertainty. It monitors the where pathway.

    TODO: mettre le résultat de l'accuracy map pour faire la transition?

    WHERE :
    Here we make the assumption that the same logpolar compression pattern is conserved from the retina up to the primary motor layers.
    **Each possible future saccade has an expected accuracy, that can be trained from the what pathway output**. To accelerate the training, we use a shortcut that is training the network on a translated accuracy map (with logpolar encoding). The ouput is thus a **logpolar accuracy map**, that tells for each possible visuo-motor displacement the value of the future accuracy.
    Thus, the saccadic motor ouput (colliculus) shows a similar log-polar compression than the visual input. The saccades are more precise at short than at long distance (and severals accades may be necessary to precisely reach distant targets).
    """)

s.close_section()

i_section = 2
#############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 RESULTS  🏄🏄🏄🏄🏄🏄🏄🏄
#############################################################################
#############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
Indeed, t...
""")

#for kind in ['correct', 'error']:
s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-saccade-' + str(idx) + '.png') for idx in [8, 20] ],
        title=title + ': success', height=s.meta['height']*.5, transpose=True),
notes="""

TODO Manu : générer images correctes avec leur saccades + incorrectes (fake)

""")

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-saccade-' + str(idx) + '.png') for idx in [46, 47, 32] ],
        title=title + ': failure', height=s.meta['height']*.6, transpose=True),
notes="""

TODO Manu : générer images correctes avec leur saccades + incorrectes (fake)

TODO Manu : je mettrais plus d'exemple de fakes

""")


if False:
    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'fig_result_robust_contrast_linear_0.7_1.svg'),
    os.path.join(figpath_talk, 'CNS-results-contrast.svg') ],
    title='Results', height=s.meta['height']*height_ratio, transpose=True,
    fragment=True, list_of_weights=[1., 2.]),
    notes="""
    TODO Manu : insérer résultats avec différents contrastes

    """)

else:
    s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'fig_result_robust_contrast_linear_0.7_1.svg') ],
    title=title + ': one saccade', height=s.meta['height']*.5, transpose=True),
    notes="""
    TODO Manu : insérer résultats avec différents contrastes

    """)


    s.add_slide(content=s.content_figures(
    [#os.path.join(figpath_talk, 'fig_result_robust_contrast_linear_0.7_1.png'),
    os.path.join(figpath_talk, 'CNS-results-contrast.svg') ],
    title=title + ': role of contrast', height=s.meta['height']*height_ratio, transpose=True),
    notes="""
    TODO Manu : insérer résultats avec différents contrastes

    """)


s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-results-saccades.svg') ],
title=title + ': more saccades', height=s.meta['height']*height_ratio, transpose=True),
notes="""
TODO Manu : insérer résultats avec différents contrastes

""")

s.add_slide(

 content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-IG-action-selection.svg') ],
     title="IG-based selection of action",height=s.meta['height']*height_ratio),
           notes = """
           done
           """)

s.close_section()


#############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
#############################################################################
#############################################################################
i_section = 3

s.open_section()

s.add_slide_outline(i_section,
notes="""
Indeed, we will use the separation of the 2 problemes (where and what) as they are confronted to nuisances of different kinds


Open questions:
- centering / log polar
- IG décision : fixation/following or saccade. After some Time the info gain is zéro:  it is not interesting any more to issue a saccade regarding this particular target.
- multi - targets? Maximizing info gain on multiple targets/ddls. Illustration with z1, z2 axis
- overt/covert attention
- free energy extension? Combination of info gain and predictive coding. 1. Maximize predicted info gain. 2. Read data. 3. Optimize predictive coding.

* Thanks for your attention!

""")


s.add_slide(content="""
## Main results:
- A new interpretation of Information Gain in visuo-motor action selection :
  - Center-surround interpretation
  - An effective decoding scheme with strong bandwidth reduction
  - Information-gain based selection of action (saccade/pursuit)
- A sub-linear object detection for image processing:
  - A full log-polar processing pathway (from early vision toward action selection)
  - Sequential info gain converges to zero: in practice 2-3 saccades are enough
  - Ready for up-scaling
- Object identity-based monitoring of action
  - Dorsal = ''actor'' (where to look next?)
  - Ventral = ''critic'' (for what to see?)
""", md=True)

s.add_slide(content="""
## Limits and Open questions
- Importance of centering objects:
  - Central object referential
  - log polar scale/rotation invariance
  - (feedback) prediction
- Information Gain-based decision :
  - Sequential info gain converges to zero: in practice 2-3 saccades are enough
  - Pursuit vs. saccade.
  - Maximizing info gain on multiple targets/ddls.
    - Overt/covert attention
    - Inhibition of return
""", md=True)

#
# s.add_slide(content="""
# # Bayesian Online Changepoint Detector
#
# * an implementation of
# [Adams &amp; MacKay 2007 "Bayesian Online Changepoint Detection"](http://arxiv.org/abs/0710.3742)
# in Python.
#
# ````
# @TECHREPORT{ adams-mackay-2007,
# AUTHOR = "Ryan Prescott Adams and David J.C. MacKay",
# TITLE  = "Bayesian Online Changepoint Detection",
# INSTITUTION = "University of Cambridge",
# ADDRESS = "Cambridge, UK",
# YEAR = "2007",
# NOTE = "arXiv:0710.3742v1 [stat.ML]",
# URL = "http://arxiv.org/abs/0710.3742"
# }
# ````
#
# * adapted from https://github.com/JackKelly/bayesianchangepoint by Jack Kelly (2013) for a binomial input.
#
# * This code is based on the  [MATLAB implementation](http://www.inference.phy.cam.ac.uk/rpa23/changepoint.php) provided by Ryan Adam. Was available at http://hips.seas.harvard.edu/content/bayesian-online-changepoint-detection
#
# * full code @ https://github.com/laurentperrinet/bayesianchangepoint
#
# """, notes='TODO Manu update with perspectives', md=True)

s.add_slide(content=intro,
            notes="""
* Thanks for your attention!
""")


s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio*.9) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes="All the material is available online - please flash this code this leads to a page with links to further references and code - TODO : use ArXiV instead ")

s.close_section()

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
if slides_filename is None:
    with open("README.md", "w") as text_file:
        text_file.write("""\
# {title}

* What:: talk @ [{conference} ({short_conference})]({conference_url})
* Who:: {author}
* Where: {location}, see {url}
* When: {DD:02d}/{MM:02d}/{YYYY}, time: {time_start}-{time_end}

* What:
  * Slides @ https://laurentperrinet.github.io/{tag}
  * Code for slides @ https://github.com/laurentperrinet/{tag}/
  * Abstract: {abstract}

""".format(**meta))

    with open("/tmp/talk.bib", "w") as text_file:
        text_file.write("""\
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}",
    Title = "{title}",
    Abstract = "{abstract}",
    Url = "{url}",
    Year = "{YYYY}",
    Date = "{YYYY}-{MM:02d}-{DD:02d}",
    location = "{location}",
    projects = "{projects}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_start}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_end}",
    url = "{url}",
    url_slides = "https://laurentperrinet.github.io/{tag}",
    url_code = "https://github.com/laurentperrinet/{tag}/",
}}

""".format(**meta))

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
