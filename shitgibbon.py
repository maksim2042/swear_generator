import pronouncing as p
from random import choice
from flask import Flask

app = Flask(__name__)

p.init_cmu()
swear = 'twat,fart,balls,snatch,pecker,dork,poon,dingle,tit,suck,snot,shit,piss,fuck,cunt,dick,cock,wad,cum,jizz,crap,pussy,fag,slut,douche,ass'.split(',')


two_syllable = []
ing = []

for w in p.pronunciations:
	first_syl = w[1].split(' ')[0]

	gerund = True if w[1].endswith('IH0 NG') else False

	pho = [syl for syl in w[1].split(' ') if len(syl)==3]
	if not pho:
		continue 
		
	if pho[0][-1]=='1' and len(pho)==2 and w[0][-1]!='s' and len(first_syl)==1 and not gerund:
		two_syllable.append(w)

	if len(pho)==2 and gerund and len(first_syl)==1:
		ing.append(w)


def make_word():
	return(choice(swear)+choice(ing)[0]+" "+choice(swear)+choice(two_syllable)[0])


@app.route('/')
def index():
	words = [make_word() for _ in range(10)]
	return('<p>'.join(words))

if __name__ == "__main__":
	app.run(host='0.0.0.0', use_reloader=True, port=3000)


#w =['','Happy', 'Birthday', 'to', 'you', 'dear', 'Jackie']
#print('\n'.join([str([w[int(z)] for z in l]) for l in [((i==2) and (str(int(x)+22))) or str(int(x)) for i,x in enumerate([''.join(map(str,range(5)))]*4)]]))
