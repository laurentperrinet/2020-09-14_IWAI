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

try:
    from academic import slugify
    slugified = slugify(tag)
except:
    slugified = '2019-07-15-cns'

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_px = 80
height_ratio = .7

meta = dict(
 embed = False,
 draft = DEBUG, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 reveal_path='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.7.0/',
 #reveal_path='https://s3.amazonaws.com/hakim-static/reveal-js/',
 theme='simple',
 bgcolor="white",
 author='Emmanuel Daucé, Pierre Albigès & Laurent Perrinet',
 author_link=f'<a href="https://laurentperrinet.github.io/talk/{slugified}/">Emmanuel Daucé, Pierre Albigès & Laurent Perrinet</a>',
 short_title='Learning where to look: a foveated visuomotor control model',
 title='Learning where to look: a foveated visuomotor control model',
 conference_url='https://www.cnsorg.org/cns-2019',
 short_conference='28th Annual Computational Neuroscience Meeting',
 conference='CNS*2019',
 location='Barcelona (Spain)',
 abstract="""In computer vision, the visual search task consists in extracting a scarce and specific visual information (the ``target'') from a large and crowded visual display. This task is usually implemented by scanning the different possible target identities at all possible spatial positions, hence with strong computational load. The human visual system employs a different strategy, combining a foveated sensor with the capacity to rapidly move the center of fixation using saccades. Saccade-based visual exploration can be idealized as an inference process, assuming that the target position and category are independently drawn from a common generative process. Knowing that process, visual processing is then separated in two specialized pathways, the "where" pathway mainly conveying information about target position in peripheral space, and the "what" pathway mainly conveying information about the category of the target. We consider here a dual neural network architecture learning independently where to look and then at what to see. This allows in particular to infer target position in retinotopic coordinates, independently to its category. This framework was tested on a simple task of finding digits in a large, cluttered image. Simulation results demonstrate the benefit of specifically learning where to look before actually knowing the target category. The approach is also energy-efficient as it includes the strong compression rate performed at the sensor level, by retina and V1 encoding, which is preserved up to the action selection level, highlighting the advantages of bio-mimetic strategies with regards to traditional computer vision when computing resources are at stake.""",
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 projects='spikeai',
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
Fredo = s.content_imagelet(os.path.join(url_people, 'frédéric-chavane/avatar.png'), height_px)
Python = s.content_imagelet('https://www.python.org/static/community_logos/python-powered-h-140x182.png', height_px)
s.meta['Acknowledgements'] =f"""
<small>
<h5>Acknowledgements:</h5>
<ul>
    <li>Rick Adams and Karl Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
    <li>Jean-Bernard Damasse and Laurent Madelain - ANR REM</li>
    <li>Frédéric Chavane - INT</li>
</ul>
<BR>
{Rick}{Karl}{JB}{LM}{Anna}{Fredo}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
<BR>
    This work was supported by the <a href="https://laurentperrinet.github.io/project/pace-itn/">PACE-ITN Project</a>.
</small>

"""
i_section = 0
#############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Learning where to look 🏄🏄🏄🏄🏄🏄🏄🏄
#############################################################################
s.open_section()
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
intro += s.content_imagelet('http://laurentperrinet.github.io/slides.py/figures/troislogos.png', s.meta['height']*.2, embed=False) #bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>

{Acknowledgements}
""".format(**meta)
#############################################################################
# s.add_slide(content=intro)
#
# s.add_slide(content=s.content_figures(
#     #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
#     [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
#     height=s.meta['height']*1.),
#     #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
#     notes="""
# Check-list:
# -----------
#
# * (before) bring VGA adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
#  """)
#
# s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
#             notes="All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

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
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU


""")



####################### OUTLINE ########################

title = meta['sections'][i_section]

s.add_slide_outline(i_section,
notes="""


""")


####################### SLIDE 2 : GENERAL MOTIVATION #########################

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'CNS-general-I.svg')],
    title='Computer vision', height=s.meta['height']*.825),
notes="""
* (OBJECTIVE)

Past 5-10 years have seen a huge development of machine learning/deep learning based image processing, indeed artificial vision has been revolutioned by
the incredible capability of convolution-based deep networks to capture the semantic content of images/photographs. Their success relies on a reduction of parameter complexity
through weight sharing convolutional neural networks applied over the full image. In order to increase the recognition capability, there has been an inflation in the number of layers needed
to process the pixel information. Finally, the processing of large images can be done at a cost that scales quadratically with the image resolution. All regions, even the “boring” ones are
systematically scanned and processed in parallel fashion at high computational cost.

Typical ML processing :
- bounding boxes around objects of interest
- (at best) Linear scaing in #pixels 

""")
    

####################### SLIDE 2bis : GENERAL MOTIVATION #########################

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'CNS-general-II.svg')],
    title='Human vision', height=s.meta['height']*.825),
notes="""
* (OBJECTIVE)


When human vision is considered, the things work quite differently.
Human (and animal) vision rely on a non isotropic sensor (the retina) that has a very high resolution at the center of fixation and a very poor
resolution at the periphery. 

Most importantly, the human vision is **dynamic**. The scanning of a full visual scene is not done in parallel but sequentially, and only scene-relevant regions of interest are scanned through saccades. This implies a **decision process** at each step that decides **where to look next**.

("non isotropic" convolution) 

""")
    

#s.add_slide(content=s.content_figures(
#[os.path.join(figpath_talk, 'fig_intro.jpg')],
#        title=title + '- Attention', height=s.meta['height']*.825),
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
[os.path.join(figpath_talk, 'CNS - Modelling - I.svg')],
        title='Statistical Viewpoint', height=s.meta['height']*.825),
notes="""
This kind of reasoning can be captured by a statistical framework called a POMDP (partially observed Markov Decision Process) where the cause of a visual scene is couple made of 
a viewpoint and scene elements. Changing the viewpoint will conduct to a different scene rendering. Knowing the current view, you need to choose the next viewpoint that will help you to 
disambiguate the scene. 


In a classic inference framework, a (generative) model tells how typically looks the visual field knowing the scene elements and a certain viewpoint . Using bayes rule, you may then infer the scene elements from the 
current view point (model inversion).  

The more viewpoints you have, the more certain you are about the content of the scene.

""")
####################### SLIDE 4 : MODELLING (CONTINUED) #########################

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS - Modelling - II.svg')],
        title='Attention vs. Scene Understanding', height=s.meta['height']*.825),
notes="""

When you have a generative model of the environment, there is an important quantity called the bayesian surprise that tells how different is the visual data from your initial guess. 
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


url =  'full code @ <a href="https://github.com/SpikeAI/2019-07-15_CNS/">github.com/SpikeAI/2019-07-15_CNS/</a>'

####################### SLIDE B 0 ##################################

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-what-where-principles.svg' )],
    title='Principles for central and peripheric vision', 
    height=s.meta['height']*.825),
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

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'fig_intro.jpg')],
        title=title + " - ''Experimental'' setup", height=s.meta['height']*.825),
notes="""


We reproduce in simulation the conditions of a psychophysic experiment.

The problem is to identify a digit that is placed at random over a noisy background, that is : finding the target identity. The agent fixates the center of the screen should give an answer about which digit was present in the image.
This corresponds to a classic environment control in psychophysic experiments.  
Different parameters are controlled, such as the target eccentricity, the background noise and the contrast, in order to var the difficulty of the task.

(B) the agent can make a saccade, in which case the center of fixation moves toward the expected location of the target. 

(C) The agent subjective perception is shown on the lower right part. The larger the target eccentrity, the more difficult the identifiction. There is a range of eccentricities for wich it is impossible to identify the target from a single glance, so that a sacade is necessary to issue a propoer response.



TODO-LAurent = génére les frames pour un "film"

""")

####################### SLIDE B 1.5 ##################################

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-what-where.svg')],
        title=title + ": What/Where separation", height=s.meta['height']*.825),
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
            title=title + subtitle[i], height=s.meta['height']*.825),
    notes="""
    
    COMPUTATIONAL GRAPH :
    Here is the general computational graph of our active vision system.
    Two streams of information are separated from the visual primary layers, one stream for processing the central pixels only, the other for processing the periphery with a logpolar encoding. The two streams converge toward a decision layer that compares the central and the peripheral acuracy, in order to decide wether to issue a saccadic or a categorical response. If a saccade is produced, then the center of vision is displaced toward the region that shows the higher accuracy on the accuracy map.
    
    WHAT :
    At the core of the vision system is the identification module (the what).   The what pathway is a classic convolutional clasifier.
It shows some translation invariance. It can quantify its uncertainty. It monitors the where pathway.
    
    WHERE : 
    Here we make the assumption that the same logpolar compression pattern is conserved from the retina up to the primary motor layers. 
    Each possible future saccade has an expected accuracy, that can be trained from the what pathway output. To accelerate the training, we use a shortcut that is training the network on a translated accuracy map (with logpolar encoding). The ouput is thus a **logpolar accuracy map**, that tells for each possible visuo-motor displacement the value of the future accuracy. 
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
        title=title + ': success', height=s.meta['height']*.6, transpose=True),
notes="""

TODO Manu : générer images correctes avec leur saccades + incorrectes (fake)

""")

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'CNS-saccade-' + str(idx) + '.png') for idx in [46, 32] ],
        title=title + ': failure', height=s.meta['height']*.6, transpose=True),
notes="""

TODO Manu : générer images correctes avec leur saccades + incorrectes (fake)

""")

s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, fname) for fname in ['fig_result_robust_contrast_linear_0.7_1.png',
                                                 'fig_result_robust_contrast_linear_0.5_1.png',
                                                 'fig_result_robust_contrast_linear_0.3_1.png']],
title=title, height=s.meta['height']*.5, transpose=True),
notes="""
TODO Manu : insérer résultats avec différents contrastes

""")

s.close_section()


#############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
#############################################################################
#############################################################################
s.open_section()

s.add_slide(content="""
# Bayesian Online Changepoint Detector

* an implementation of
[Adams &amp; MacKay 2007 "Bayesian Online Changepoint Detection"](http://arxiv.org/abs/0710.3742)
in Python.

````
@TECHREPORT{ adams-mackay-2007,
AUTHOR = "Ryan Prescott Adams and David J.C. MacKay",
TITLE  = "Bayesian Online Changepoint Detection",
INSTITUTION = "University of Cambridge",
ADDRESS = "Cambridge, UK",
YEAR = "2007",
NOTE = "arXiv:0710.3742v1 [stat.ML]",
URL = "http://arxiv.org/abs/0710.3742"
}
````

* adapted from https://github.com/JackKelly/bayesianchangepoint by Jack Kelly (2013) for a binomial input.

* This code is based on the  [MATLAB implementation](http://www.inference.phy.cam.ac.uk/rpa23/changepoint.php) provided by Ryan Adam. Was available at http://hips.seas.harvard.edu/content/bayesian-online-changepoint-detection

* full code @ https://github.com/laurentperrinet/bayesianchangepoint

""", notes='TODO Manu update with perspectives', md=True)

s.add_slide(content=intro,
            notes="""
open questions:
- centering / log polar
- IG décision : fixation/following or saccade. After some Time the info gain is zéro:  it is not interesting any more to issue a saccade regarding this particular target.
- multi - targets? Maximizing info gain on multiple targets/ddls. Illustration with z1, z2 axis
- overt/covert attention
- free energy extension? Combination of info gain and predictive coding. 1. Maximize predicted info gain. 2. Read data. 3. Optimize predictive coding. 

* Thanks for your attention!
""")


s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
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

* What:: talk @ [conference]({conference_url})
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
