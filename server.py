# encoding:utf8
from flask import Flask, render_template
import simplejson
import os
from docutils.core import publish_parts

root = os.path.dirname(__file__)


app = Flask(__name__)

@app.route('/')
def home():
    filename = 'index.html'
    return render_template(filename)

@app.route('/item')
def json():
    return simplejson.dumps({
        'title': 'the best post ever',
        'text': publish_parts('''Lòrem ípsum dolór sit ámet, éa dicàt elaboraret vim, mea ád quaeque vocibùs blandít. In aequé nominavi luptatum vél. Ex quando doctùs disputàndo vìs. Ad aliquíp propríae vim, his scripta sèntentiae no. Mel eu ìnani integre disputationi.

Qúaèque dolorùm ìnèrmís ex meá, praèsént électram scrìpserit his ut, pùtant fìerent te per. Nàm pericula quaérendum liberavisse ad, per id impetus accusámus comprehensam. Cibo aeqúè ét quo, sólet labitùr aliquando his éì. Veritus euripìdìs vim àn, vócìbus rectèque mea ád. Vim út ullum eloquentiam, ímpedit liberavisse accommodare id dúo. Harúm áffert dèséruisse án vél, sumo summó probatús èos cu.

Audire nùsquam civibús ea sed. Làbore sapientem prí eu. Vix àùtém omnìum qùalísqùe id, tollit effícìendì interpretarís per id. In nèc duis periculis, case appetere ín nec. Nec an natum dignissim, ex vél própriàe lùcilius, nam id meís utroque scaevola.

Sìt in everti scaevolà elèífènd. Nam cu exerci malorum èloqùèntiam, solet opórterè no vím. No vis ígnòta ratìònìbus, vìs justo democritum te, sonet blàndít salutatus tè pro. Cúm et àmet vìdisse, éx nec sìnt quálisque, màlis aeque méi èa.

Eum nobis cómmodo át. Eu usù eligendi mandamus, postulant complectìtur né mel. Rèqùé prìncipes sed àd, et nostro commune insolens vis. Éú decorè doctus argumentum eós, àt cònsul partém dicunt nam. Mei éu nolùisse democritùm.

In érror omniúm vìm. Pútent platonem definitionem pró eu. Cum út omníum délèctus màlùissèt, ùt vis trítani adipìsci deterruisset. Tè álià nominaví appéllantur usu, vitáe nónumes vís eí. Nè sint aliquam qùi, àd ìntegre voluptua dissentiunt ius, no vis dícàt nonumes. Soleàt pertinax splendide dúo in. Èssent áppètere ad cum.

Cu mea tollít céteros, persìus nòstrud delicatíssimi eù íus. Fièrént vituperata éx mel. Ne persiús iuvaret sea, ne nèc àpèirian tempórìbùs, nec verterem vòlutpat postúlànt an. Sed decore eligendi ùt, tritani dolorem pétentium has ad, éam ad ullum libris. Nè sapèrèt hàbemus cùm, sed neglègentur theóphrastùs eí, vix in alii unum.

Prì labitur féugait nè. Cu laboramus nécessitatibùs sít. Nec id facilisis dèfinítìonèm. Id éos adhuc nemoré. Nò his harum tincídunt. Ad has illum possìt, ad nàm làóreet impedit.

Lègimús vivendo principes vim te, hinc rébum út has, làbòre deléniti periculis no qui. Nec tota vóluptua pertinax ne, òdíò nìsl múndi ùsù no. Tàntàs mòlèstìae similique nec at, ad quó ípsum bonórum rationìbus, cum eì fugit senténtìàe. Eú úsu próbo urbanitás, ìus scrìpta delenitì ratiònibús an, in partém ridens meliore mèl. Pro nulla vocibus cu, facér latìne inimìcus èt vim, nèmore nomìnavi est ne. Id solét fuìsset mel, án dùò probo vèniam, unum omnés dèlicátissimi éx prò.

Ad pèr liber scripta volutpat, èx pro níbh accòmmòdárè. Sadipscing sùscipiantur sed ìd, quo nó alia òmnium scriptórèm, víx quaèqùe mnesarchum ei. Èum ùt malórùm ancillaè. Eì meis sempèr has. Rébum perpetua malùissét vel an. In illud nihil hónestàtis méi, no altera invidunt pri. Nihil tation quidam pér in, clíta cetéròs nec cu.''', writer_name='html')['html_body']
    })

if __name__ == '__main__':
    app.run(debug=True)
