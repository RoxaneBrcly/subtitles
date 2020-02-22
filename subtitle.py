# class for subtitle object, including method to display them in .ssa format
class Subtitle:
    def __init__(self, start, end, style, text):
        self.start = start
        self.end = end
        self.style = style
        self.text = text

    def display(self):
        effect = 'fad,{\move(1800,800,572,800,0,700)} {\an7}' # the effect depends on the language, left-to-right or right-to-left;
        # for the purpose of testing, will be using right-to-left
        # this effect was manually programmed in .ssa
        display = '\n' + 'Dialogue: Marked=0,' + self.start + ',' + self.end + ',' + self.style + ',' + effect + self.text
        return display

# Open the ttml file
def get_xml(file_name):
    xml_file = open(file_name + '.xml')
    content = xml_file.read()
    xml_file.close()
    return content

# Create a txt file with only the subtitles
def get_subtitles():
    xml_file = get_xml('SWIhack_copypaste_clean.mp4')
    subtitles = xml_file.split('\n')
    return subtitles

# function to pull data from the TTML tags - 
def retrieve_data():
    subtitles = get_subtitles()
    template = open('template.ass', 'a')
    for subtitle in subtitles:
        if (subtitle.find('<p begin') != -1):
            attributes = subtitle.split('"')
            start = attributes[1]
            start = '0:00:0' + start.replace('s', '')
            end = attributes[5]
            end = '0:00:0' + end.replace('s', '')
            style = 'StyleWhite,NTP,0,0,0,'
            text = attributes[6]
            text = text.replace('>', '', 1)
            text = text.replace('</p>', '')
            print(text)
            ass_object = Subtitle(start, end, style, text)
            ass_subtitle = ass_object.display()
            template.write(ass_subtitle)
    template.close()
    template = open('template.ass', 'r')
    ass_content = template.read()
    template.close()
    return ass_content

retrieve_data()
