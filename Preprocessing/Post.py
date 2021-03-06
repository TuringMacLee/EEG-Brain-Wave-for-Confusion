class Post():
    '''
    Store info for each post in the data
    '''

    def __init__(self, school='', degree='', major='', result='', year=0, semester='', date='', toefl_total=0, toefl_reading = 0, toefl_listening = 0, toefl_speaking = 0, toefl_writing = 0, toefl=[0,0,0,0], gre_total=0, gre_verbal=0, gre_quantity=0, gre_writing=0, gre=[0,0,0,0], undergraduate='', under_major='', gpa=0, gpa_ranking='', others='', url=''):
        self.school = school #ranking
        self.degree = degree #1:master 2:phd
        self.major = major
        self.result = result #1:admission or offer 0:refuse
        self.year = year #year with int
        self.semester = semester
        self.date = date
        self.toefl_total = toefl_total #total score, float
        self.toefl_reading = toefl_reading
        self.toefl_listening = toefl_listening
        self.toefl_speaking = toefl_speaking
        self.toefl_writing = toefl_writing
        self.toefl = toefl  #list of floats, [reading listening speaking writing]
        self.gre_total = gre_total #total score, float
        self.gre_verbal = gre_verbal
        self.gre_quantity = gre_quantity
        self.gre_writing = gre_writing
        self.gre = gre #list of floats, [verbal quantity writing]
        self.undergraduate = undergraduate
        self.under_major = under_major
        self.gpa = gpa #trans into [0-1]
        self.gpa_ranking = gpa_ranking #trans into [0-1]
        self.others = others
        self.url = url

    def __str__(self):
        return u"school:{0}\ndegree:{1}\nmajor:{2}\nresult:{3}\nyear:{4}\nsemester:{5}\ndate:{6}\ntoefl:{7}\ngre:{8}\nundergraduate:{9}\nunder_major:{10}\ngpa:{11}\n\ngpa_ranking:{12}\nothers:{13}\nurl:{14}\n".format(self.school, self.degree, self.major, self.result, self.year, self.semester, self.date, self.toefl, self.gre, self.undergraduate, self.under_major, self.gpa, self.gpa_ranking, self.others, self.url)