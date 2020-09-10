__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
import os
################################################################################
class Slide:
    def __init__(self, contents=[], subtitles=[], fontsizes=[],
                 type='text', color='white', bg_color='black', duration=1):
        self.type = type
        self.subtitles = subtitles
        self.duration = duration
        self.contents = contents
        self.fontsizes = fontsizes
        self.color = color
        self.bg_color = bg_color

################################################################################
# http://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html
from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip
################################################################################
class Deck:
    def __init__(self,
                 videoname = "video-abstract", fps = 3,
                 figpath = 'figures',
                 H=500, W=800, border_ratio=1.618*2):

        # self.W = W
        # self.H = H
        self.H_fig, self.W_fig = int(H-H/border_ratio), int(W-W/border_ratio)

        self.videoname = videoname
        self.gifname = videoname + ".gif"
        self.figpath = figpath
        self.fps = fps


        self.txt_opts = dict(font="Open-Sans-Regular", align='center',
                             color='white',
                             size=(W,H), method='caption')
        #self.txt_opts = dict(fontsize=65, bg_color='white', align='center', **opt_st)
        self.sub_opts = dict(font="Open-Sans-SemiBold", fontsize=28, align='South',
                                #bg_color='white',
                                color='yellow',
                                size=(W,H), method='caption')

    def compositing(self, slides):
        t = 0
        clips = []
        for slide in slides:
            # contains figures or text
            if len(slide.contents)>0:
                sub_duration = slide.duration / len(slide.contents)
                for i_, content in enumerate(slide.contents):
                    if slide.type == 'text':
                        if len(slide.fontsizes)==0:
                            fontsize = 35 # default
                        elif len(slide.fontsizes)==1:
                            fontsize = slide.fontsizes
                        else:
                            fontsize = slide.fontsizes[i_]

                        clip = TextClip(content, bg_color=slide.bg_color,
                                        fontsize=fontsize, **self.txt_opts)
                    else:
                        # drawing the list of figures
                        clip = ImageClip(os.path.join(self.figpath, content))
                    # time
                    clip = clip.set_start(t).set_duration(sub_duration)
                    # space
                    clip = clip.resize(height=self.H_fig, width=self.W_fig)
                    clip = clip.set_pos('center')

                    clips.append(clip)
                    t += sub_duration

            if len(slide.subtitles)>0:
                # overlaying subtitles
                t -= slide.duration # be kind, rewind
                sub_duration = slide.duration / len(slide.subtitles)
                for subtitle in slide.subtitles:
                    sub = TextClip(subtitle, **self.sub_opts)
                    # time
                    sub = sub.set_start(t).set_duration(sub_duration)
                    # space
                    sub = sub.resize(height=self.H_fig, width=self.W_fig)
                    sub = sub.set_pos('center')

                    clips.append(sub)
                    t += sub_duration
            else:
                print('no subtitle', slide.contents)

        return clips

    def compiling(self, clips):
        # Compostiting all clips
        video = CompositeVideoClip(clips)
        print('Writing', self.videoname + '.mp4')
        video.write_videofile(self.videoname + '.mp4', fps=self.fps)
        print('Writing', self.gifname)
        video.write_gif(self.gifname, fps=self.fps)
        from pygifsicle import optimize
        optimize(self.gifname)
        print('Done')
