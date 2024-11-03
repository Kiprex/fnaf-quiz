from cProfile import label
import traceback
import pdb
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import winsound
import time

current_ambient = 1
answ_meta = 10

winsound.PlaySound("assets\\main_menu.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

bg1_width, bg1_height, bg1_channels, bg1_data = dpg.load_image(r"assets\background1.jpg")
bg2_width, bg2_height, bg2_channels, bg2_data = dpg.load_image(r"assets\background2.jpg")
bg3_width, bg3_height, bg3_channels, bg3_data = dpg.load_image(r"assets\background3.jpg")
scr_width, scr_height, scr_channels, scr_data = dpg.load_image(r"assets\scr.jpg")
answ_width, answ_height, answ_channels, answ_data = dpg.load_image(r"assets\answers_field.png")


dpg.create_context()

global_var = 1

answers = {
    1: ['how many nights', '3', '5', '7', '10', 2],
    2: ['what cafe', 'vkusno i tochka', "Freddy Fazbear's Pizza", 'KFC','Pizza Hut', 2],
    3: ['kem rabotaet glavniy geroi', 'cleaner', 'powar', 'oxrannik', 'policeman', 3],
    4: ['kto protivniki', 'people', 'zombi', 'animatroniki', 'ghosts', 3],
    5: ['fnaf netu v', 'films', 'books', 'comics', 'music', 4],
    6: ["chika's pat", 'cat', 'pizza', 'keks', 'cyplyonok', 3],
    7: ['zvuk priblizhenia animatronika', 'music', 'laugh', 'footsteps', 'zvonok', 3],
    8: ['kakoy resurs nado controlirovat', 'hp', 'energy', 'time', 'food', 2],
    9: ['chem opredelyat gde animatroniki', 'lazer detectors', 'cameras', 'sounds', 'lights', 2],
    10: ['kogo ozvuchival sozdatel', 'freddy', 'oxrannik', 'chel iz zvonka', 'keks', 3],
    11: ['skok chelovek sozdavali igru', '1', '3', '10', '80', 1],
    12: ['kakie functsii u animatronikov', 'razvlekat detey', 'obuchat detey', 'powara', 'decor', 1],
    13: ['kakaoy personazh byl sozdan po koshmarnomu snu odnogo iz sozdateley', 'bonni', 'chika', 'foxy', 'freddy', 1],
    14: ['v kakom godu vishla pervaya igra?', '2006', '2010', '2014', '2017', 3],
    15: ['pochemu pizzeria zakrylas', 'malo deneg', 'malo popularnosti', 'negativnie otzyvi', 'rebranding', 3]
    }
with dpg.texture_registry():
    bg1 = dpg.add_static_texture(bg1_width, bg1_height, bg1_data)
    bg2 = dpg.add_static_texture(bg2_width, bg2_height, bg2_data)
    bg3 = dpg.add_static_texture(bg3_width, bg3_height, bg3_data)
    scr = dpg.add_static_texture(scr_width, scr_height, scr_data)
    texture_answer_field = dpg.add_static_texture(answ_width, answ_height, answ_data)
    qbg = dpg.add_static_texture(dpg.load_image(r"assets\question_bg.png")[0], dpg.load_image(r"assets\question_bg.png")[1], dpg.load_image(r"assets\question_bg.png")[3])
    
    begin = dpg.load_image(r"assets\begin.jpg")
    begin_tex = dpg.add_static_texture(begin[0], begin[1], begin[3])

    start_s = dpg.load_image(r"assets\startscreen.png")
    start_tex = dpg.add_static_texture(start_s[0], start_s[1], start_s[3])

    end1 = dpg.load_image(r"assets\endscreen1.jpg")
    end1_tex = dpg.add_static_texture(end1[0], end1[1], end1[3])

    end2 = dpg.load_image(r"assets\endscreen2.png")
    end2_tex = dpg.add_static_texture(end2[0], end2[1], end2[3])

    q1 = dpg.load_image(r"assets\qss\q1.jpg")
    q1_tex = dpg.add_static_texture(q1[0], q1[1], q1[3])
    q2 = dpg.load_image(r"assets\qss\q2.jpg")
    q2_tex = dpg.add_static_texture(q2[0], q2[1], q2[3])
    q3 = dpg.load_image(r"assets\qss\q3.jpg")
    q3_tex = dpg.add_static_texture(q3[0], q3[1], q3[3])
    q4 = dpg.load_image(r"assets\qss\q4.jpg")
    q4_tex = dpg.add_static_texture(q4[0], q4[1], q4[3])
    q5 = dpg.load_image(r"assets\qss\q5.jpg")
    q5_tex = dpg.add_static_texture(q5[0], q5[1], q5[3])
    q6 = dpg.load_image(r"assets\qss\q6.jpg")
    q6_tex = dpg.add_static_texture(q6[0], q6[1], q6[3])
    q7 = dpg.load_image(r"assets\qss\q7.jpg")
    q7_tex = dpg.add_static_texture(q7[0], q7[1], q7[3])
    q8 = dpg.load_image(r"assets\qss\q8.jpg")
    q8_tex = dpg.add_static_texture(q8[0], q8[1], q8[3])
    q9 = dpg.load_image(r"assets\qss\q9.jpg")
    q9_tex = dpg.add_static_texture(q9[0], q9[1], q9[3])
    q10 = dpg.load_image(r"assets\qss\q10.jpg")
    q10_tex = dpg.add_static_texture(q10[0], q10[1], q10[3])
    q11 = dpg.load_image(r"assets\qss\q11.jpg")
    q11_tex = dpg.add_static_texture(q11[0], q11[1], q11[3])
    q12 = dpg.load_image(r"assets\qss\q12.jpg")
    q12_tex = dpg.add_static_texture(q12[0], q12[1], q12[3])
    q13 = dpg.load_image(r"assets\qss\q13.jpg")
    q13_tex = dpg.add_static_texture(q13[0], q13[1], q13[3])
    q14 = dpg.load_image(r"assets\qss\q14.jpg")
    q14_tex = dpg.add_static_texture(q14[0], q14[1], q14[3])
    q15 = dpg.load_image(r"assets\qss\q15.jpg")
    q15_tex = dpg.add_static_texture(q15[0], q15[1], q15[3])


    q11 = dpg.load_image(r"assets\qs\q1_1.jpg")
    q1_1_tex = dpg.add_static_texture(q11[0], q11[1], q11[3])
    q12 = dpg.load_image(r"assets\qs\q1_2.jpg")
    q1_2_tex = dpg.add_static_texture(q12[0], q12[1], q12[3])
    q13 = dpg.load_image(r"assets\qs\q1_3.jpg")
    q1_3_tex = dpg.add_static_texture(q13[0], q13[1], q13[3])
    q14 = dpg.load_image(r"assets\qs\q1_4.jpg")
    q1_4_tex = dpg.add_static_texture(q14[0], q14[1], q14[3])
    q21 = dpg.load_image(r"assets\qs\q2_1.jpg")
    q2_1_tex = dpg.add_static_texture(q21[0], q21[1], q21[3])
    q22 = dpg.load_image(r"assets\qs\q2_2.jpg")
    q2_2_tex = dpg.add_static_texture(q22[0], q22[1], q22[3])
    q23 = dpg.load_image(r"assets\qs\q2_3.jpg")
    q2_3_tex = dpg.add_static_texture(q23[0], q23[1], q23[3])
    q24 = dpg.load_image(r"assets\qs\q2_4.jpg")
    q2_4_tex = dpg.add_static_texture(q24[0], q24[1], q24[3])
    q31 = dpg.load_image(r"assets\qs\q3_1.jpg")
    q3_1_tex = dpg.add_static_texture(q31[0], q31[1], q31[3])
    q32 = dpg.load_image(r"assets\qs\q3_2.jpg")
    q3_2_tex = dpg.add_static_texture(q32[0], q32[1], q32[3])
    q33 = dpg.load_image(r"assets\qs\q3_3.jpg")
    q3_3_tex = dpg.add_static_texture(q33[0], q33[1], q33[3])
    q34 = dpg.load_image(r"assets\qs\q3_4.jpg")
    q3_4_tex = dpg.add_static_texture(q34[0], q34[1], q34[3])
    q41 = dpg.load_image(r"assets\qs\q4_1.jpg")
    q4_1_tex = dpg.add_static_texture(q41[0], q41[1], q41[3])
    q42 = dpg.load_image(r"assets\qs\q4_2.jpg")
    q4_2_tex = dpg.add_static_texture(q42[0], q42[1], q42[3])
    q43 = dpg.load_image(r"assets\qs\q4_3.jpg")
    q4_3_tex = dpg.add_static_texture(q43[0], q43[1], q43[3])
    q44 = dpg.load_image(r"assets\qs\q4_4.jpg")
    q4_4_tex = dpg.add_static_texture(q44[0], q44[1], q44[3])
    q51 = dpg.load_image(r"assets\qs\q5_1.jpg")
    q5_1_tex = dpg.add_static_texture(q51[0], q51[1], q51[3])
    q52 = dpg.load_image(r"assets\qs\q5_2.jpg")
    q5_2_tex = dpg.add_static_texture(q52[0], q52[1], q52[3])
    q53 = dpg.load_image(r"assets\qs\q5_3.jpg")
    q5_3_tex = dpg.add_static_texture(q53[0], q53[1], q53[3])
    q54 = dpg.load_image(r"assets\qs\q5_4.jpg")
    q5_4_tex = dpg.add_static_texture(q54[0], q54[1], q54[3])
    q61 = dpg.load_image(r"assets\qs\q6_1.jpg")
    q6_1_tex = dpg.add_static_texture(q61[0], q61[1], q61[3])
    q62 = dpg.load_image(r"assets\qs\q6_2.jpg")
    q6_2_tex = dpg.add_static_texture(q62[0], q62[1], q62[3])
    q63 = dpg.load_image(r"assets\qs\q6_3.jpg")
    q6_3_tex = dpg.add_static_texture(q63[0], q63[1], q63[3])
    q64 = dpg.load_image(r"assets\qs\q6_4.jpg")
    q6_4_tex = dpg.add_static_texture(q64[0], q64[1], q64[3])
    q71 = dpg.load_image(r"assets\qs\q7_1.jpg")
    q7_1_tex = dpg.add_static_texture(q71[0], q71[1], q71[3])
    q72 = dpg.load_image(r"assets\qs\q7_2.jpg")
    q7_2_tex = dpg.add_static_texture(q72[0], q72[1], q72[3])
    q73 = dpg.load_image(r"assets\qs\q7_3.jpg")
    q7_3_tex = dpg.add_static_texture(q73[0], q73[1], q73[3])
    q74 = dpg.load_image(r"assets\qs\q7_4.jpg")
    q7_4_tex = dpg.add_static_texture(q74[0], q74[1], q74[3])
    q81 = dpg.load_image(r"assets\qs\q8_1.jpg")
    q8_1_tex = dpg.add_static_texture(q81[0], q81[1], q81[3])
    q82 = dpg.load_image(r"assets\qs\q8_2.jpg")
    q8_2_tex = dpg.add_static_texture(q82[0], q82[1], q82[3])
    q83 = dpg.load_image(r"assets\qs\q8_3.jpg")
    q8_3_tex = dpg.add_static_texture(q83[0], q83[1], q83[3])
    q84 = dpg.load_image(r"assets\qs\q8_4.jpg")
    q8_4_tex = dpg.add_static_texture(q84[0], q84[1], q84[3])

    q91 = dpg.load_image(r"assets\qs\q9_1.jpg")
    q9_1_tex = dpg.add_static_texture(q91[0], q91[1], q91[3])
    q92 = dpg.load_image(r"assets\qs\q9_2.jpg")
    q9_2_tex = dpg.add_static_texture(q92[0], q92[1], q92[3])
    q93 = dpg.load_image(r"assets\qs\q9_3.jpg")
    q9_3_tex = dpg.add_static_texture(q93[0], q93[1], q93[3])
    q94 = dpg.load_image(r"assets\qs\q9_4.jpg")
    q9_4_tex = dpg.add_static_texture(q94[0], q94[1], q94[3])
    q101 = dpg.load_image(r"assets\qs\q10_1.jpg")
    q10_1_tex = dpg.add_static_texture(q101[0], q101[1], q101[3])
    q102 = dpg.load_image(r"assets\qs\q10_2.jpg")
    q10_2_tex = dpg.add_static_texture(q102[0], q102[1], q102[3])
    q103 = dpg.load_image(r"assets\qs\q10_3.jpg")
    q10_3_tex = dpg.add_static_texture(q103[0], q103[1], q103[3])
    q104 = dpg.load_image(r"assets\qs\q10_4.jpg")
    q10_4_tex = dpg.add_static_texture(q104[0], q104[1], q104[3])
    q111 = dpg.load_image(r"assets\qs\q11_1.jpg")
    q11_1_tex = dpg.add_static_texture(q111[0], q111[1], q111[3])
    q112 = dpg.load_image(r"assets\qs\q11_2.jpg")
    q11_2_tex = dpg.add_static_texture(q112[0], q112[1], q112[3])
    q113 = dpg.load_image(r"assets\qs\q11_3.jpg")
    q11_3_tex = dpg.add_static_texture(q113[0], q113[1], q113[3])
    q114 = dpg.load_image(r"assets\qs\q11_4.jpg")
    q11_4_tex = dpg.add_static_texture(q114[0], q114[1], q114[3])
    q121 = dpg.load_image(r"assets\qs\q12_1.jpg")
    q12_1_tex = dpg.add_static_texture(q121[0], q121[1], q121[3])
    q122 = dpg.load_image(r"assets\qs\q12_2.jpg")
    q12_2_tex = dpg.add_static_texture(q122[0], q122[1], q122[3])
    q123 = dpg.load_image(r"assets\qs\q12_3.jpg")
    q12_3_tex = dpg.add_static_texture(q123[0], q123[1], q123[3])
    q124 = dpg.load_image(r"assets\qs\q12_4.jpg")
    q12_4_tex = dpg.add_static_texture(q124[0], q124[1], q124[3])
    q131 = dpg.load_image(r"assets\qs\q13_1.jpg")
    q13_1_tex = dpg.add_static_texture(q131[0], q131[1], q131[3])
    q132 = dpg.load_image(r"assets\qs\q13_2.jpg")
    q13_2_tex = dpg.add_static_texture(q132[0], q132[1], q132[3])
    q133 = dpg.load_image(r"assets\qs\q13_3.jpg")
    q13_3_tex = dpg.add_static_texture(q133[0], q133[1], q133[3])
    q134 = dpg.load_image(r"assets\qs\q13_4.jpg")
    q13_4_tex = dpg.add_static_texture(q134[0], q134[1], q134[3])
    q141 = dpg.load_image(r"assets\qs\q14_1.jpg")
    q14_1_tex = dpg.add_static_texture(q141[0], q141[1], q141[3])
    q142 = dpg.load_image(r"assets\qs\q14_2.jpg")
    q14_2_tex = dpg.add_static_texture(q142[0], q142[1], q142[3])
    q143 = dpg.load_image(r"assets\qs\q14_3.jpg")
    q14_3_tex = dpg.add_static_texture(q143[0], q143[1], q143[3])
    q144 = dpg.load_image(r"assets\qs\q14_4.jpg")
    q14_4_tex = dpg.add_static_texture(q144[0], q144[1], q144[3])
    q151 = dpg.load_image(r"assets\qs\q15_1.jpg")
    q15_1_tex = dpg.add_static_texture(q151[0], q151[1], q151[3])
    q152 = dpg.load_image(r"assets\qs\q15_2.jpg")
    q15_2_tex = dpg.add_static_texture(q152[0], q152[1], q152[3])
    q153 = dpg.load_image(r"assets\qs\q15_3.jpg")
    q15_3_tex = dpg.add_static_texture(q153[0], q153[1], q153[3])
    q154 = dpg.load_image(r"assets\qs\q15_4.jpg")
    q15_4_tex = dpg.add_static_texture(q154[0], q154[1], q154[3])

label1 = answers[global_var][1]
label2 = answers[global_var][2]
label3 = answers[global_var][3]
label4 = answers[global_var][4]
current_bg = 'back1'

def answer(sender, app_data, user_data):
    global global_var, answers
    if answers[global_var][5] == user_data:
        dpg.set_value(score, int(dpg.get_value(score)) + answ_meta)
        winsound.PlaySound(r"assets\right.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(1)
        winsound.PlaySound(f"assets\\ambient{current_ambient}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    else:
        disable_all()
        dpg.configure_item('scr', show=True)
        winsound.PlaySound(r"assets\pyym.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(2)
        enable_all()
        dpg.configure_item('scr', show=False)
        winsound.PlaySound(f"assets\\ambient{current_ambient}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    next_q()

def win():
   disable_all()
   dpg.set_global_font_scale(5) 
   dpg.configure_item('score', show=True)
   dpg.configure_item('score_t', show=True)
   dpg.configure_item('end1', show=True)
   winsound.PlaySound(f"assets\\endscreen1.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
   time.sleep(8)
   dpg.configure_item('score', show=False)
   dpg.configure_item('score_t', show=False)
   dpg.set_global_font_scale(1)
   dpg.configure_item('end1', show=False)
   dpg.configure_item('end2', show=True)
   dpg.configure_item('veronika', show=True)
   dpg.configure_item('artem', show=True)
   dpg.configure_item('egor', show=True)
   dpg.configure_item('ilya', show=True)
   winsound.PlaySound(f"assets\\endscreen2.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def disable_all():
    dpg.configure_item('btn1', show=False)
    dpg.configure_item('btn2', show=False)
    dpg.configure_item('btn3', show=False)
    dpg.configure_item('btn4', show=False)
    dpg.configure_item('tex_answ_f', show=False)
    dpg.configure_item('qbg', show=False)
    dpg.configure_item(current_bg, show=False)
    dpg.configure_item('qs', show=False)

def enable_all():
    dpg.configure_item('btn1', show=True)
    dpg.configure_item('btn2', show=True)
    dpg.configure_item('btn3', show=True)
    dpg.configure_item('btn4', show=True)
    dpg.configure_item('tex_answ_f', show=True)
    dpg.configure_item('qbg', show=True)
    dpg.configure_item(current_bg, show=True)
    dpg.configure_item('qs', show=True)

def start_game():
    enable_all()
    dpg.configure_item('123', show=False)
    dpg.configure_item('begin', show=False)
    dpg.configure_item('start_b', show=False)
    winsound.PlaySound(f"assets\\ambient{current_ambient}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

def next_q():
    global global_var, answers, current_ambient, current_bg, answ_meta
    if global_var < len(answers):
        global_var += 1
        if global_var != 1:
            dpg.configure_item(f'q{global_var}', show=True)
            for i in range(4):
                dpg.configure_item(f'q{global_var}_{i + 1}', show=True)
    else:
        win()
    if global_var == 6:
        current_ambient += 1
        answ_meta = 20
        winsound.PlaySound(f"assets\\ambient{current_ambient}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        current_bg = 'back2'
        dpg.configure_item('back1', show=False)
        dpg.configure_item('back2', show=True)
    elif global_var == 11:
        answ_meta = 30
        current_ambient += 1
        winsound.PlaySound(f"assets\\ambient{current_ambient}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        current_bg = 'back3'  
        dpg.configure_item('back2', show=False)
        dpg.configure_item('back3', show=True)


with dpg.window(width=300, tag="Primary Window", autosize=True, no_title_bar=True):
    
    dpg.add_image(scr, show=False, tag='scr')
    dpg.add_image(bg1, show=False, tag='back1')
    dpg.add_image(end1_tex, show=False, tag='end1')
    dpg.add_image(end2_tex, show=False, tag='end2')
    dpg.add_image(bg2, show=False, tag='back2')
    dpg.add_image(bg3, show=False, tag='back3')
    score_t = dpg.add_text('Your score:', tag='score_t', pos=(20, 30), show=False)
    score = dpg.add_text(0, tag='score', pos=(430, 30), show=False)
    dpg.add_image(qbg, tag='qbg', pos=(0, 180))
    dpg.add_image(texture_answer_field, tag='tex_answ_f', pos=(740, 180))

    b1 = dpg.add_button(pos=(907, 330), label=label1, tag='btn1', user_data=1, callback=answer, width=260, height=50)
    b1 = dpg.add_button(pos=(907, 395), label=label2, tag='btn2', user_data=2, callback=answer, width=260, height=50)
    b2 = dpg.add_button(pos=(907, 460), label=label3, tag='btn3', user_data=3, callback=answer, width=260, height=50)
    b3 = dpg.add_button(pos=(907, 525), label=label4, tag='btn4', user_data=4, callback=answer, width=260, height=50)

    dpg.add_text('Veronika - nothing', tag='veronika', pos=(230, 30), show=False)
    dpg.add_text('Artem - designer', tag='artem', pos=(430, 30), show=False)
    dpg.add_text('Egor - developer', tag='egor', pos=(620, 30), show=False)
    dpg.add_text('Ilya - captain', tag='ilya', pos=(850, 30), show=False)
    
    with dpg.group(tag='qs'):
        dpg.add_image(q1_tex, show=True, tag='q1', pos=(210, 335))
        dpg.add_image(q2_tex, show=False, tag='q2', pos=(210, 335))
        dpg.add_image(q3_tex, show=False, tag='q3', pos=(210, 335))
        dpg.add_image(q4_tex, show=False, tag='q4', pos=(210, 335))
        dpg.add_image(q5_tex, show=False, tag='q5', pos=(210, 335))
        dpg.add_image(q6_tex, show=False, tag='q6', pos=(210, 335))
        dpg.add_image(q7_tex, show=False, tag='q7', pos=(210, 335))
        dpg.add_image(q8_tex, show=False, tag='q8', pos=(210, 335))
        dpg.add_image(q9_tex, show=False, tag='q9', pos=(210, 335))
        dpg.add_image(q10_tex, show=False, tag='q10', pos=(210, 335))
        dpg.add_image(q11_tex, show=False, tag='q11', pos=(210, 335))
        dpg.add_image(q12_tex, show=False, tag='q12', pos=(210, 335))
        dpg.add_image(q13_tex, show=False, tag='q13', pos=(210, 335))
        dpg.add_image(q14_tex, show=False, tag='q14', pos=(210, 335))
        dpg.add_image(q15_tex, show=False, tag='q15', pos=(210, 335))


        dpg.add_image(q1_1_tex, show=True, tag='q1_1', pos=(909, 332))
        dpg.add_image(q1_2_tex, show=True, tag='q1_2', pos=(909, 397))
        dpg.add_image(q1_3_tex, show=True, tag='q1_3', pos=(909, 462))
        dpg.add_image(q1_4_tex, show=True, tag='q1_4', pos=(909, 527))
        dpg.add_image(q2_1_tex, show=False, tag='q2_1', pos=(909, 332))
        dpg.add_image(q2_2_tex, show=False, tag='q2_2', pos=(909, 397))
        dpg.add_image(q2_3_tex, show=False, tag='q2_3', pos=(909, 462))
        dpg.add_image(q2_4_tex, show=False, tag='q2_4', pos=(909, 527))
        dpg.add_image(q3_1_tex, show=False, tag='q3_1', pos=(909, 332))
        dpg.add_image(q3_2_tex, show=False, tag='q3_2', pos=(909, 397))
        dpg.add_image(q3_3_tex, show=False, tag='q3_3', pos=(909, 462))
        dpg.add_image(q3_4_tex, show=False, tag='q3_4', pos=(909, 527))
        dpg.add_image(q4_1_tex, show=False, tag='q4_1', pos=(909, 332))
        dpg.add_image(q4_2_tex, show=False, tag='q4_2', pos=(909, 397))
        dpg.add_image(q4_3_tex, show=False, tag='q4_3', pos=(909, 462))
        dpg.add_image(q4_4_tex, show=False, tag='q4_4', pos=(909, 527))
        dpg.add_image(q5_1_tex, show=False, tag='q5_1', pos=(909, 332))
        dpg.add_image(q5_2_tex, show=False, tag='q5_2', pos=(909, 397))
        dpg.add_image(q5_3_tex, show=False, tag='q5_3', pos=(909, 462))
        dpg.add_image(q5_4_tex, show=False, tag='q5_4', pos=(909, 527))
        dpg.add_image(q6_1_tex, show=False, tag='q6_1',  pos=(909, 332))
        dpg.add_image(q6_2_tex, show=False, tag='q6_2', pos=(909, 397))
        dpg.add_image(q6_3_tex, show=False, tag='q6_3', pos=(909, 462))
        dpg.add_image(q6_4_tex, show=False, tag='q6_4', pos=(909, 527))
        dpg.add_image(q7_1_tex, show=False, tag='q7_1', pos=(909, 332))
        dpg.add_image(q7_2_tex, show=False, tag='q7_2', pos=(909, 397))
        dpg.add_image(q7_3_tex, show=False, tag='q7_3', pos=(909, 462))
        dpg.add_image(q7_4_tex, show=False, tag='q7_4', pos=(909, 527))
        dpg.add_image(q8_1_tex, show=False, tag='q8_1', pos=(909, 332))
        dpg.add_image(q8_2_tex, show=False, tag='q8_2', pos=(909, 397))
        dpg.add_image(q8_3_tex, show=False, tag='q8_3', pos=(909, 462))
        dpg.add_image(q8_4_tex, show=False, tag='q8_4', pos=(909, 527))
        dpg.add_image(q9_1_tex, show=False, tag='q9_1', pos=(909, 332))
        dpg.add_image(q9_2_tex, show=False, tag='q9_2', pos=(909, 397))
        dpg.add_image(q9_3_tex, show=False, tag='q9_3', pos=(909, 462))
        dpg.add_image(q9_4_tex, show=False, tag='q9_4', pos=(909, 527))
        dpg.add_image(q10_1_tex, show=False, tag='q10_1', pos=(909, 332))
        dpg.add_image(q10_2_tex, show=False, tag='q10_2', pos=(909, 397))
        dpg.add_image(q10_3_tex, show=False, tag='q10_3', pos=(909, 462))
        dpg.add_image(q10_4_tex, show=False, tag='q10_4', pos=(909, 527))
        dpg.add_image(q11_1_tex, show=False, tag='q11_1', pos=(909, 332))
        dpg.add_image(q11_2_tex, show=False, tag='q11_2', pos=(909, 397))
        dpg.add_image(q11_3_tex, show=False, tag='q11_3', pos=(909, 462))
        dpg.add_image(q11_4_tex, show=False, tag='q11_4', pos=(909, 527))
        dpg.add_image(q12_1_tex, show=False, tag='q12_1', pos=(909, 332))
        dpg.add_image(q12_2_tex, show=False, tag='q12_2', pos=(909, 397))
        dpg.add_image(q12_3_tex, show=False, tag='q12_3', pos=(909, 462))
        dpg.add_image(q12_4_tex, show=False, tag='q12_4', pos=(909, 527))
        dpg.add_image(q13_1_tex, show=False, tag='q13_1', pos=(909, 332))
        dpg.add_image(q13_2_tex, show=False, tag='q13_2', pos=(909, 397))
        dpg.add_image(q13_3_tex, show=False, tag='q13_3', pos=(909, 462))
        dpg.add_image(q13_4_tex, show=False, tag='q13_4', pos=(909, 527))
        dpg.add_image(q14_1_tex, show=False, tag='q14_1', pos=(909, 332))
        dpg.add_image(q14_2_tex, show=False, tag='q14_2', pos=(909, 397))
        dpg.add_image(q14_3_tex, show=False, tag='q14_3', pos=(909, 462))
        dpg.add_image(q14_4_tex, show=False, tag='q14_4', pos=(909, 527))
        dpg.add_image(q15_1_tex, show=False, tag='q15_1', pos=(909, 332))
        dpg.add_image(q15_2_tex, show=False, tag='q15_2', pos=(909, 397))
        dpg.add_image(q15_3_tex, show=False, tag='q15_3', pos=(909, 462))
        dpg.add_image(q15_4_tex, show=False, tag='q15_4', pos=(909, 527))
    disable_all()
    dpg.add_image(start_tex, show=True, tag='123')
    dpg.add_button(pos=(320, 500), label='Begin', tag='start_b', callback=start_game, width=100, height=100)
    dpg.add_image(begin_tex, show=True, tag='begin', pos=(322, 502))

dpg.create_viewport(x_pos=50, y_pos=50, title='Custom Title', width=1280, height=720, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()