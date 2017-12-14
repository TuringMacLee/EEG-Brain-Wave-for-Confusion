import string
from fuzzywuzzy import fuzz

def calibrate_school(university_list, school):
    exclude = set(string.punctuation)
    school = ''.join(ch for ch in school if ch not in exclude)
    school.replace('  ', '')
    if school.encode('utf-8') in university_list.keys():
        return university_list[school]
    else:
        scores = {}
        for uni in university_list:
            scores[uni] = fuzz.partial_ratio(school, uni)
        choice = max(scores, key=scores.get)
        return university_list[choice]

def calibrate_degree(degree):
    if degree.find('M') != -1 or degree.find('m') != -1:
        return 1
    elif degree.find('D') != -1 or degree.find('d') != -1:
        return 2
    else:
        print degree
        exit(0)

def calibrate_result(result):
    if result.find('A') != -1 or result.find('a') != -1 or result.find('O') != -1 or result.find('o') != -1:
        return 1
    elif result.find('R') != -1 or result.find('r') != -1:
        return 0
    else:
        print result
        exit(0)

def calibrate_year(year):
    try:
        return int(year)
    except ValueError:
        print year
        exit(0)

def calibrate_toefl(toefl):
    toefl_total = 0.0
    if  toefl == None:
        toefl = [0, 0, 0, 0]
    elif len(toefl) == 5:
        toefl_total = toefl[0]
        toefl = toefl[1 : 5]
    elif len(toefl) == 4:
        toefl_total = sum(toefl)
    elif len(toefl) == 0:
        toefl = [0, 0, 0, 0]
    elif len(toefl) == 1:
        toefl_total = toefl[0]
        toefl = [0, 0, 0, 0]
    else:
        print toefl
        exit(0)
    return toefl_total, toefl

def calibrate_gre(gre):
    gre_total = 0.0
    if  gre == None:
        gre = [0, 0, 0]
    elif len(gre) == 4:
        gre_total = gre[0]
        gre = gre[1 : 4]
    elif len(gre) == 3:
        gre_total = sum(gre)
    elif len(gre) == 0:
        gre = [0, 0, 0]
    elif len(gre) == 1:
        gre_total = gre[0]
        gre = [0, 0, 0]
    else:
        print gre
        exit(0)
    return gre_total, gre