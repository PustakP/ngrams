import random


set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
# same as paper, ive used 26 letter and a space


# count the frequency of each letter in the bible
dict = {}

with open('bible_formatted.txt', 'r') as file:
    text = file.read()

for i in text:
    if i.lower() in dict:
        dict[i.lower()] += 1
    else:
        dict[i.lower()] = 1

#print(dict)
# ^ used to get the following result:

freq = {' ': 751013, 'i': 193926, 'n': 225026, 't': 317696, 'h': 282657, 'e': 412160, 'b': 48853, 'g': 55279, 'o': 243143, 'd': 158086, 'c': 55056,
        'r': 170301, 'a': 275701, 'v': 30362, 'w': 65478, 's': 189997, 'u': 83462, 'f': 83534, 'm': 79929, 'k': 22281, 'p': 43248, 'l': 129919,
        'y': 58568, 'x': 1478, 'j': 8880, 'z': 2972, 'q': 964}

# frequency of each letter in the bible

def zerogram():
    return random.choice(set)

def unigram(n):
    return random.choices(set, weights=freq.values(), k=n)

#0 and 1st order of approximation

# to make bigram, we will have to make a dictionary of the bigrams in the bible

# bigram_dict = {}

# # counting bigrams
# for i in range(len(text)-1):
#     bigram = text[i:i+2].lower()
#     if bigram in bigram_dict:
#         bigram_dict[bigram] += 1
#     else:
#         bigram_dict[bigram] = 1

# # print bigram_dict
# print(bigram_dict)


# after above, we have our bigram dictionary-

bigram_freq = {' i': 42362, 'in': 46967, 'n ': 55184, ' t': 146189, 'th': 160780, 'he': 130175, 'e ': 155552, ' b': 32865, 'be': 19144, 'eg': 2391, 'gi': 2888, 'nn': 1195, 'ni': 4007, 'ng': 20613, 'g ': 13772, ' g': 15762, 'go': 8951, 'od': 7713, 'd ': 107814, ' c': 22078, 'cr': 1910, 're': 40718, 'ea': 21273, 'at': 31930, 'te': 15848, 'ed': 23293, ' h': 51874, 'av': 8119, 've': 22708, 'en': 30054, ' a': 93533, 'an': 76664, 'nd': 64507, ' e': 12102, 'ar': 21248, 'rt': 7251, 'h ': 33378, ' w': 44503, 'wa': 10370, 'as': 17703, 's ': 66468, 'wi': 14532, 'it': 25097, 'ho': 19882, 'ou': 31361, 'ut': 11672, 't ': 69283, ' f': 26610, 'fo': 16885, 'or': 35411, 'rm': 1336, 'm ': 21425, ' v': 2469, 'vo': 1210, 'oi': 2360, 'id': 9831, ' d': 17735, 'da': 7849, 'rk': 1710, 'kn': 1950, 'ne': 16289, 'es': 26206, 'ss': 7439, ' u': 17022, 'up': 5801, 'po': 5487, 'on': 26185, 'nt': 23803, 'fa': 4800, 'ac': 6384, 'ce': 8919, ' o': 50107, 'of': 38231, 'f ': 36876, 'de': 13013, 'ee': 11540, 'ep': 4441, 'p ': 3962, ' s': 54339, 'sp': 4014, 'pi': 1943, 'ir': 8180, 'ri': 13966, ' m': 27897, 'mo': 7524, 'ov': 4012, 'ew': 3036, 'er': 45956, 'rs': 8213, 'sa': 15293, 'ai': 13710, ' l': 19960, 'le': 18132, 'et': 14988, 'li': 8134, 'ig': 5385, 'gh': 7955, 'ht': 6578, 'aw': 2446, 'w ': 5703, 'ha': 44948, 'oo': 5191, 'di': 5553, 'iv': 5219, 'vi': 4365, 'tf': 289, 'fr': 4659, 'ro': 13205, 'om': 12174, 'ca': 8817, 'al': 27157, 'll': 25877, 'ay': 9802, 'y ': 37696, ' n': 15683, 'ta': 7146, 'ev': 6858, 'rn': 4727, 'we': 10809, 'fi': 4818, 'st': 20110, 'a ': 9981, 'ma': 12406, 'am': 10446, 'me': 19064, 'mi': 5544, 'ds': 4041, 'ad': 7651, 'wh': 13569, 'hi': 33316, 'ic': 8120, 'ch': 13126, 'eu': 534, 'un': 15799, 'r ': 39250, 'ab': 5603, 'bo': 4237, 'so': 11426, 'o ': 33537, 'em': 11607, 'se': 23724, 'ec': 5395, 'co': 10689, 'ga': 5608, 'to': 29295, 'og': 806, 'ge': 4853, 'ru': 3315, ' p': 16390, 'pl': 4998, 'la': 8343, 'dr': 3998, 'ry': 3472, 'ap': 2214, 'pp': 1096, 'pe': 7170, 'ft': 3325, 'br': 5039, 'gr': 3191, 'ra': 10146, 'rb': 458, 'b ': 1434, ' y': 10598, 'yi': 1863, 'ie': 7021, 'el': 14052, 'ld': 8686, 'gs': 2806, 'ui': 1710, 'tr': 5667, 'af': 2027, 'is': 27963, ' k': 6127, 'ki': 4938, 'os': 5385, 'si': 5867, 'ts': 5099, 'lf': 1362, 'ug': 3432, 'rh': 260, 'rd': 14186, 'gn': 704, 'ns': 8382, 'ys': 2032, 'ye': 7497, '  ': 7607, 'tw': 2233, 'wo': 5791, ' r': 8963, 'ul': 5054, 'ya': 363, 'ls': 3480, 'tu': 2458, 'dt': 1382, 'ur': 10645, 'bu': 6485, 'tl': 1344, 'ly': 3663, 'gc': 24, 'if': 4367, 'fe': 4899, 'ow': 8404, 'wl': 408, 'l ': 29139, 'fl': 1594, 'eo': 4730, 'op': 4083, 'tm': 261, 'ei': 7935, 'bl': 3098, 'fu': 1373, 'mu': 1391, 'lt': 4146, 'ti': 9195, 'ip': 1274, 'il': 13291, 'tt': 3476, 'sk': 505, 'us': 11917, 'ak': 5179, 'ke': 8563, 'im': 9954, 'ag': 3722, 'ik': 946, 'do': 6079, 'io': 5029, 'sh': 20474, 'lo': 14553, 'wn': 2325, 'dh': 456, 'dm': 732, 'su': 3579, 'ub': 1298, 'bd': 58, 'du': 869, 'ue': 1316, 'no': 14536, 'yl': 390, 'eh': 3233, 'ol': 6104, 'i ': 9414, 'yo': 5363, 'u ': 7833, 'dw': 1202, 'sl': 1110, 'sv': 18, 'ix': 342, 'xt': 197, 'hu': 2848, 'k ': 4957, 'nc': 4234, 'ct': 1437, 'au': 3472, 'ey': 9025, 'ef': 5293, 'ot': 12169, 'tc': 625, 'db': 380, 'pu': 1768, 'dg': 1278, 'pa': 4617, 'na': 5492, 'mp': 1435, 'ah': 4952, 'iu': 104, 'um': 1303, 'ny': 1815, 'yx': 12, 'x ': 343, 'ih': 170, 'ia': 3198, 'dd': 570, 'ek': 1168, 'hg': 90, 'oe': 1086, 'sy': 610, 'yr': 492, 'ph': 3074, 'hr': 3268, 'ok': 2358, 'mm': 1637, 'lp': 307, 'nh': 902, 'pt': 2302, 'ib': 1152, 'bs': 572, 'cl': 1886, 'my': 4767, 'yf': 201, 'lc': 227, 'rp': 527, 'bt': 135, 'dy': 495, 'uc': 1401, 'ty': 3411, 'lb': 201, 'oh': 865, 'sb': 424, 'ba': 3250, 'yw': 199, 'ms': 1659, 'lv': 1386, 'pr': 6140, 'lk': 639, 'hy': 5322, 'td': 139, 'gu': 800, 'cu': 1675, 'nm': 134, 'rr': 1452, 'yd': 106, 'sw': 1985, 'oa': 1860, 'fs': 199, 'df': 321, 'bi': 1749, 'oc': 1202, 'ff': 2775, 'ck': 2268, 'wr': 938, 'yc': 168, 'cc': 1170, 'mt': 342, 'gt': 661, 'va': 1989, 'hm': 286, 'nb': 248, 'nv': 158, 'nf': 435, 'ku': 36, 'eb': 1702, 'ci': 2542, 'uj': 4, 'ja': 1121, 'ae': 2861, ' z': 840, 'zi': 597, ' j': 7131, 'ju': 1939, 'dl': 636, 'rg': 857, 'aa': 1167, 'sn': 615, 'dc': 244, 'yy': 35, 'fm': 148, 'hw': 206, 'mf': 202, 'wt': 88, 'lw': 192, 'dn': 662, 'nl': 548, 'nu': 765, 'ua': 969, 'tg': 100, 'oy': 774, 'rf': 487, 'iw': 120, 'uf': 275, 'by': 3030, 'hf': 202, 'hs': 664, 'ws': 622, 'sg': 316, 'ex': 774, 'xc': 279, 'gl': 986, 'pw': 77, 'mb': 1622, 'sr': 2683, 'hc': 97, 'ps': 450, 'nw': 222, 'lu': 589, 'kt': 66, 'sm': 942, 'rv': 1888, 'eq': 149, 'qu': 964, 'ud': 2510, 'rl': 1002, 'nk': 953, 'kw': 40, 'dj': 125, 'hk': 36, 'az': 714, 'z ': 223, 'iz': 242, 'zr': 132, 'mr': 98, 'gd': 454, 'ln': 167, 'ob': 1379, 'uh': 74, 'ej': 410, 'je': 3537, 'ez': 565, 'ze': 827, 'rw': 328, 'za': 706, 'ax': 148, 'xa': 173, 'uz': 127, 'jo': 2273, 'lm': 323, 'kl': 188, 'hl': 186, 'sc': 1676, 'ml': 42, 'mn': 310, 'fh': 168, 'fc': 50, 'hd': 135, 'gy': 774, 'yp': 938, 'oj': 217, 'ao': 342, 'ox': 184, 'xe': 345, 'ks': 819, 'zz': 230, 'zo': 101, 'mh': 70, 'tn': 445, 'fn': 62, 'hb': 357, 'fz': 30, 'ii': 11, 'ka': 264, 'zu': 45, 'hp': 98, 'wf': 67, 'yn': 147, 'gg': 119, 'rc': 1434, 'iq': 338, 'sd': 376, 'ym': 176, 'bm': 24, 'mc': 174, 'lh': 134, 'c ': 181, 'yt': 349, ' q': 267, 'hh': 234, 'gm': 456, 'dv': 165, 'tb': 338, 'wm': 20, 'mw': 108, 'yu': 53, 'wc': 13, 'cy': 410, 'md': 34, 'yh': 166, 'hj': 55, 'ji': 10, 'yb': 143, 'dk': 45, 'rj': 63, 'gp': 40, 'lg': 110, 'ww': 24, 'sf': 282, 'fg': 120, 'nq': 117, 'dp': 147, 'kr': 31, 'mg': 33, 'aj': 49, 'cs': 4, 'kb': 24, 'np': 108, 'wd': 44, 'fb': 117, 'gf': 69, 'uu': 8, 'tp': 149, 'bb': 373, 'yv': 20, 'py': 86, 'nr': 105, 'xp': 79, 'fy': 302, 'yg': 115, 'uk': 170, 'zp': 52, 'uw': 28, 'fj': 163, 'nj': 272, 'dz': 26, 'ko': 209, 'oz': 88, 'bz': 9, 'kc': 54, 'fp': 41, 'wk': 7, 'hn': 241, 'uy': 66, 'tj': 56, 'gj': 15, 'uv': 2, 'zb': 6, 'hz': 25, 'wb': 95, 'fw': 57, 'lr': 95, 'wg': 14, 'xo': 2, 'km': 42, 'gw': 55, 'sz': 7, 'bh': 53, 'oq': 4, 'bn': 110, 'zh': 13, 'lz': 21, 'pf': 17, 'vy': 85, 'mk': 8, 'uo': 46, 'fd': 50, 'xb': 1, 'sq': 27, 'gb': 54, 'tv': 11, 'wu': 5, 'pn': 5, 'yk': 24, 'vu': 4, 'kh': 12, 'kf': 21, 'yj': 20, 'bw': 8, 'tk': 36, 'sj': 26, 'tq': 6, 'ij': 191, 'wp': 9, 'pb': 13, 'zn': 8, 'rz': 35, 'xh': 43, 'hq': 22, 'zm': 12, 'kk': 43, 'mz': 5, 'mq': 2, 'wy': 18, 'lj': 13, 'hv': 8, 'zl': 6, 'gk': 35, 'wv': 1, 'ky': 8, 'pd': 4, 'zj': 1, 'zk': 4, 'kd': 3, 'dq': 4, 'zd': 1, 'fk': 15, 'mj': 23, 'pc': 5, 'xi': 11, 'bc': 1, 'kp': 5, 'xl': 2, 'xs': 2, 'pm': 19, 'gq': 1, 'wj': 6, 'aq': 10, 'cq': 17, 'zc': 1, 'kv': 3, 'kj': 4, 'gz': 1, 'nz': 2, 'fv': 8, 'vs': 1, 'bk': 2, 'zt': 3, 'gv': 7, 'zg': 4, 'rx': 15, 'bg': 1, 'bj': 35, 'tz': 5, 'pj': 1, 'mv': 4, 'bf': 1, 'bv': 5, 'pv': 1, 'cw': 4, 'pk': 3, 'kg': 1, 'cn': 1, 'ux': 2, 'xw': 1, 'tx': 1, 'pg': 10}

def bigram(n):
    # zeroth order approximation
    result = [random.choice(set)]
    
    # context
    for _ in range(n-1):
        prc = result[-1]
        # list of possible characters
        nextc = []
        weights = []
        for bigram in bigram_freq:
            if bigram.startswith(prc):
                nextc.append(bigram[1])
                weights.append(bigram_freq[bigram])
        
        # if no bigram exists
        if not nextc:
            result.append(random.choice(set))
        else:
            result.append(random.choices(nextc, weights=weights)[0])
    
    return result


# 2nd order approx using bigrams

# to make trigram, same process
trigram_dict = {}

for i in range(len(text)-2):
    trigram = text[i:i+3].lower()
    if trigram in trigram_dict:
        trigram_dict[trigram] += 1
    else:
        trigram_dict[trigram] = 1

# this is too big to print, and takes only 1 second to run so i will use it by calculating frequency each time.

def trigram(n):
    if n < 2:
        return bigram(n)  # incase parameters are trash
    
    # start with bigram
    result = bigram(2)
    
    # same process
    for _ in range(n-2):
        prev_two_chars = ''.join(result[-2:])
        nextc = []
        weights = []
        for tri in trigram_dict:
            if tri.startswith(prev_two_chars):
                nextc.append(tri[2])
                weights.append(trigram_dict[tri])
        
        if not nextc:
            # birgam if no trigram
            prc = result[-1]
            nextc = []
            weights = []
            for bi in bigram_freq:
                if bi.startswith(prc):
                    nextc.append(bi[1])
                    weights.append(bigram_freq[bi])
            
            if not nextc:
                result.append(random.choice(set))
            else:
                result.append(random.choices(nextc, weights=weights)[0])
        else:
            result.append(random.choices(nextc, weights=weights)[0])
    
    return result

# 3rd order approx using trigrams



# attempting word level approximation

# making a dictionary of words
word_dict = {}

for i in text.split():
    if i.lower() in word_dict:
        word_dict[i.lower()] += 1
    else: 
        word_dict[i.lower()] = 1

# print(word_dict)
#  too big to print, will use as is

def word_zerogram():
    return " ".join(random.choice(list(word_dict.keys())))

def word_unigram(n):
    return " ".join(random.choices(list(word_dict.keys()), weights=word_dict.values(), k=n))

# code below is reused from bigram


bigram_word_dict = {}

# counting word bigrams
words = text.split()
for i in range(len(words)-1):
    word1 = words[i].lower()
    word2 = words[i+1].lower()
    bigram_word = (word1, word2)  # use tuple for word pairs
    if bigram_word in bigram_word_dict:
        bigram_word_dict[bigram_word] += 1
    else:
        bigram_word_dict[bigram_word] = 1


def word_bigram(n):
    # taking a random word
    result = [random.choice(list(word_dict.keys()))]
    
    for _ in range(n-1):
        prw = result[-1]
        nxtw = []
        weights = []
        
        # looking for all piars
        for (w1, w2) in bigram_word_dict:
            if w1 == prw:
                nxtw.append(w2)
                weights.append(bigram_word_dict[(w1, w2)])
        
        # random word if no bigram (first order)
        if not nxtw:
            result.append(random.choice(list(word_dict.keys())))
        else:
            result.append(random.choices(nxtw, weights=weights)[0])
    
    return " ".join(result)


#main

c = int(input("enter number of characters/words: "))

mode = input("enter mode (0 for zeroth order, 1 for first order, 2 for second order, 3 for third order, 4 for word zeroth order, 5 for word first order, 6 for word second order): ")
 
if mode == "0":
    print(''.join(zerogram(c)))
elif mode == "1":
    print(''.join(unigram(c)))
elif mode == "2":
    print(''.join(bigram(c)))
elif mode == "3":
    print(''.join(trigram(c)))
elif mode == "4":
    print(word_zerogram())
elif mode == "5":
    print(word_unigram(c))
elif mode == "6":
    print(word_bigram(c))
else:
    print("invalid mode")
