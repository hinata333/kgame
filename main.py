import streamlit as st
from PIL import Image

# 469
# 10 2 8　進数
# 4(4) 6(110) 9(11)
##################################################################
st.title('Quiz')
st.write('    ')


st.write('-'*60)
q_1 = st.button('Category 1')
morse_code1_1 = ['?', '?', '?', '?', '?']
morse_code1_2 = ['?', '?', '?', '?', '?']
st.write('###### ・工藤新一と毛利蘭は高校何年生？', unsafe_allow_html=True)
col1_1, col1_2, col1_3 = st.columns(3)
with col1_1: elem1_1 = st.checkbox('１年', value=False)
with col1_2: elem1_2 = st.checkbox('２年', value=False) #正解
with col1_3: elem1_3 = st.checkbox('３年', value=False)
if elem1_2: morse_code1_1[0] = '・'
if elem1_2: morse_code1_2[0] = 'ー'

st.write('    ')
st.write('###### ・コナンの年齢は何歳？', unsafe_allow_html=True)
col2_1, col2_2, col2_3 = st.columns(3)
with col2_1: elem2_1 = st.checkbox('6歳', value=False)
with col2_2: elem2_2 = st.checkbox('7歳', value=False) #正解
with col2_3: elem2_3 = st.checkbox('8歳', value=False)
if elem2_2: morse_code1_1[1] = 'ー'
if elem2_2: morse_code1_2[1] = 'ー'

st.write('    ')
st.write('###### ・コナンが眠らせて推理をしたことがない人物は次の中で誰？', unsafe_allow_html=True)
col3_1, col3_2, col3_3 = st.columns(3)
with col3_1: elem3_1 = st.checkbox('鈴木園子（すずきそのこ）', value=False)
with col3_2: elem3_2 = st.checkbox('遠山和葉（とおやまかずは）', value=False) #正解
with col3_3: elem3_3 = st.checkbox('妃英理（きさきえり）', value=False)
if elem3_2: morse_code1_1[2] = 'ー'
if elem3_2: morse_code1_2[2] = 'ー'

st.write('    ')
st.write('###### ー毛利蘭の両親が別居するきっかけとなった大喧嘩の理由は？', unsafe_allow_html=True)
col4_1, col4_2, col4_3 = st.columns(3)
with col4_1: elem4_1 = st.checkbox('母の手料理がまずいから', value=False) #正解
with col4_2: elem4_2 = st.checkbox('父が酔っ払うから', value=False)
with col4_3: elem4_3 = st.checkbox('子育てについての意見が分かれたから', value=False)
if elem4_1: morse_code1_1[3] = 'ー'
if elem4_1: morse_code1_2[3] = 'ー'


st.write('    ')
st.write('###### ・高木刑事とラブラブの佐藤刑事。そんな彼女の初恋の相手は？   ※難問')
col5_1, col5_2, col5_3 = st.columns(3)
with col5_1: elem5_1 = st.checkbox('冴羽遼', value=False)
with col5_2: elem5_2 = st.checkbox('アムロ・レイ', value=False)
with col5_3: elem5_3 = st.checkbox('ルパン三世', value=False) #正解
if elem5_3: morse_code1_1[4] = 'ー'
if elem5_3: morse_code1_2[4] = 'ー'

morse_code1_1 = ''.join(morse_code1_1)
morse_code1_2 = ''.join(morse_code1_2)

st.write('    ')
if st.button('採点'):
    st.write(f'# 「　　　a = :red[{morse_code1_1}]　　　　」')
    st.write(f'# 「　　　b = :red[{morse_code1_2}]　　　　」')
    st.write(f'#  　　　　Key： ab　　　　　')




st.write('-'*60)
q_2 = st.button('Category 2')
morse_code_2 = ['?', '?', '?', '?', '?']
st.write('###### ・水無怜奈 （みずなしれな）のコードネームは「キール」ですが、彼女の本当の正体は？', unsafe_allow_html=True)
col2_1_1, col2_1_2, col2_1_3 = st.columns(3)
with col2_1_1: elem2_1_1 = st.checkbox('CIA諜報員', value=False) #正解
with col2_1_2: elem2_1_2 = st.checkbox('FBI諜報員', value=False) 
with col2_1_3: elem2_1_3 = st.checkbox('公安警察', value=False)
if elem2_1_1: morse_code_2[0] = '・'

st.write('    ')
st.write('###### ・組織のナンバー2である「ラム」の特徴として、当てはまるものは次の内どれ？', unsafe_allow_html=True)
col2_2_1, col2_2_2, col2_2_3 = st.columns(3)
with col2_2_1: elem2_2_1 = st.checkbox('いつも仮面をつけている', value=False)
with col2_2_2: elem2_2_2 = st.checkbox('片腕が義手', value=False) 
with col2_2_3: elem2_2_3 = st.checkbox('片目が義眼', value=False) #正解
if elem2_2_3: morse_code_2[1] = '・'

st.write('    ')
st.write('###### ・毛利探偵事務所の1階にある喫茶店の名前は？', unsafe_allow_html=True)
col2_3_1, col2_3_2, col2_3_3 = st.columns(3)
with col2_3_1: elem2_3_1 = st.checkbox('ポアロ', value=False) #正解
with col2_3_2: elem2_3_2 = st.checkbox('アポロ', value=False) 
with col2_3_3: elem2_3_3 = st.checkbox('ポピア', value=False)
if elem2_3_1: morse_code_2[2] = 'ー'

st.write('    ')
st.write('###### ・工藤新一が好きな食べ物は？', unsafe_allow_html=True)
col2_4_1, col2_4_2, col2_4_3 = st.columns(3)
with col2_4_1: elem2_4_1 = st.checkbox('アップルパイ', value=False) 
with col2_4_2: elem2_4_2 = st.checkbox('レモンパイ', value=False) #正解
with col2_4_3: elem2_4_3 = st.checkbox('苺タルト', value=False)
if elem2_4_2: morse_code_2[3] = 'ー'


st.write('    ')
st.write('###### ・工藤新一が苦手な食べ物は？   ※難問')
col2_5_1, col2_5_2, col2_5_3 = st.columns(3)
with col2_5_1: elem2_5_1 = st.checkbox('レーズン', value=False) #正解
with col2_5_2: elem2_5_2 = st.checkbox('アーモンド', value=False)
with col2_5_3: elem2_5_3 = st.checkbox('にんじん', value=False) 
if elem2_5_1: morse_code_2[4] = 'ー'

morse_code_2 = ''.join(morse_code_2)

st.write('    ')
if st.button('採点 '):
    st.write(f'# 「　　　c = :red[{morse_code_2}]　　　　」')
    st.write(f'#  　　　　Key： c　　　　　')


st.write('-'*60)


q_3 = st.button('Category 3')
morse_code_3 = ['?', '?', '?', '?', '?']
st.write('###### ・去年の玉村町花火大会はいつ？', unsafe_allow_html=True)
col3_1_1, col3_1_2, col3_1_3 = st.columns(3)
with col3_1_1: elem3_1_1 = st.checkbox('7/15', value=False) 
with col3_1_2: elem3_1_2 = st.checkbox('7/16', value=False) #正解
with col3_1_3: elem3_1_3 = st.checkbox('7/17', value=False) 
if elem3_1_2: morse_code_3[0] = 'ー'

st.write('    ')
st.write('###### ・喫茶日向の開店日はいつ？', unsafe_allow_html=True)
col3_2_1, col3_2_2, col3_2_3 = st.columns(3)
with col3_2_1: elem3_2_1 = st.checkbox('7/16 ', value=False)
with col3_2_2: elem3_2_2 = st.checkbox('7/17 ', value=False) 
with col3_2_3: elem3_2_3 = st.checkbox('7/18 ', value=False) #正解
if elem3_2_3: morse_code_3[1] = 'ー'

st.write('    ')
st.write('###### ・あんなが喫茶日向で最初に注文したメニューは何？', unsafe_allow_html=True)
col3_3_1, col3_3_2, col3_3_3 = st.columns(3)
with col3_3_1: elem3_3_1 = st.checkbox('ナポリタン', value=False)
with col3_3_2: elem3_3_2 = st.checkbox('クリームソーダ', value=False)  #正解
with col3_3_3: elem3_3_3 = st.checkbox('アイス（たまごボーロ添え）', value=False)
if elem3_3_2: morse_code_3[2] = 'ー'

st.write('    ')
st.write('###### ・交際前にデートで行った湖の名前は？', unsafe_allow_html=True)
col3_4_1, col3_4_2, col3_4_3 = st.columns(3)
with col3_4_1: elem3_4_1 = st.checkbox('野尻湖', value=False) 
with col3_4_2: elem3_4_2 = st.checkbox('野反湖', value=False) #正解
with col3_4_3: elem3_4_3 = st.checkbox('野坂湖', value=False)
if elem3_4_2: morse_code_3[3] = '・'


st.write('    ')
st.write('###### ・玉村町花火大会の後に家まで送った際、シートベルトを外すまでの時間t(秒)は？ ※難問')
col3_5_1, col3_5_2, col3_5_3 = st.columns(3)
with col3_5_1: elem3_5_1 = st.checkbox('t < 3', value=False) #正解
with col3_5_2: elem3_5_2 = st.checkbox('3 ≦ t ≦ 10', value=False)
with col3_5_3: elem3_5_3 = st.checkbox('10 < t', value=False) 
if elem3_5_1: morse_code_3[4] = '・'

morse_code_3 = ''.join(morse_code_3)

st.write('    ')
if st.button('採点  '):
    st.write(f'# 「　　　d = :red[{morse_code_3}]　　　　」')
    st.write(f'#  　　　　Key： d　　　　　')



st.write('-'*60)
# 4869
# 10 2 8　進数
# 4(4) 6(110) 9(11)
##################################################################
code = st.button('Code')
st.write(f'#   　　「　4　→　ab　→　◯ 　」　')
st.write(f'#   　　「　1000　→　c　→　×　」　')
st.write(f'#   　　「　110　→　c　→　△　」　')
st.write(f'#   　　「　11　→　d　→　□ 　」　')
st.write(f'#   :red[　　　※Password: ◯×△□　]')

st.write('    ')
st.write('    ')
col_note, col_hint = st.columns(2)
with col_note:
  note = st.button('Note')
  st.write(f'##### 「　　　a = {morse_code1_1}　　　　」')
  st.write(f'##### 「　　　b = {morse_code1_2}　　　　」')
  st.write(f'#####  　　　※ Key： ab　　　　　')
  st.write(f'##### 「　　　c = {morse_code_2}　　　　」')
  st.write(f'#####  　　　※ Key： c　　　　　')
  st.write(f'##### 「　　　d = {morse_code_3}　　　　」')
  st.write(f'#####  　　　※ Key： d　　　　　')

with col_hint:
  hint = st.button('Open Hint')
  if hint:
    st.write(f'#####   （例1）　　　　（例2）')
    st.write(f'#####   ・2 → ab → 2　　・8 → ab → 8')
    st.write(f'#####   ・11 → c  → 3　　・100 → c  → 4')
    st.write(f'#####   ・10 → d  → 8　　・4 → d  → 4')

st.write('-'*60)
# password = st.number_input('※パスワードを入力してください。')
label = '※半角数字でパスワードを入力してください。'
col_n_1, col_n_2, col_n_3 = st.columns(3)
with col_n_1: select_number = st.number_input(label, 0, 10000, 0)
count = 0
if int(select_number) == 4869:
    st.balloons()

    st.write('    ')
    st.write('    ')
    l_1, l_2, l_3, l_4 = st.columns(4)
    with l_1: final_q = st.button('Final Question')
    with l_4: last_btn = st.button('※最後にClick!')

    image = Image.open('table.png')
    if last_btn:
      image = Image.open('table_2.png')
    st.image(image, caption='金庫の暗証番号を示しています。')

    hint = st.button('Open Hint ')
    if hint:
      st.write(f'（4, 8, 6, 9）　→　(行, 列)、(行, 列)、(行, 列)')


    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')
    # last_btn = st.button('※最後に押してね！')
    # if last_btn:
    #   image_2 = Image.open('table_2.png')
    #   st.image(image_2, caption='')


