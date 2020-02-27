# Animated subtitles
Python program to convert a .xml subtitle file into a .ssa, including animations, for 'handsome' overlay text that we can then burn into a video

Desired outcome: instead of making the overlay text in Adobe Premiere, read it from a simple subtitle file attached to a video. For the purpose of the Swihack, the result should look like this: http://www.swissinfo.ch/eng/multimedia/becoming-astronauts_a-space-boot-camp-in-the-alps/45565898 - but the effects can be modified.

Use: This is helpful if the video has to be translated, and even more so into a language such as Arabic, that Premiere doesn't render correctly if the initial project was in another language.

After translating the subtitles, you can burn them into the video using, for instance, https://handbrake.fr/

# Files
  
  Swihack.xml: example subtitles in xml format, including start and end timecode and some styling
  
  Template.ass: this template includes several stylings from line 22 to 30. These can be adapted easily (font, colour, etc.).
On line 14 and 15, info on the audio and video files related

  Subtitles.py: the subtitles from the xml file will be formatted to fit ssa/ass format and will be added to the template.
The animation is added directly in the python file on line 10, and can be modified there. To adapt the animation effect, look up http://docs.aegisub.org/3.2/ASS_Tags/
