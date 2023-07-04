import streamlit as st

data = [[69202,"天野悠貴","B",2,2], [68206,"大西海斗","C",3,3], [67903,"加藤拓也","E",5,5], [66803,"河口淑乃","F",1,6], [67902,"北井真佑子","D",2,7], 
        [64211,"小森紀明","H",3,8], [62204,"譽田豊","I",4,9], [89003,"齊内直文","J",5,10], [69203,"範國正拓","A",1,1], [54302,"福田夏","B",2,2], 
        [67210,"堀田優介","C",3,3], [69205,"矢野敬将","D",4,4], [65201,"吉岡汰玖哉","E",5,5]]

question = [[1, '逆さにすると、重さが減る海の生き物は？', 'いるか'], [2, '「ま」を収納すると出てくる動物は？', 'しまうま'], 
            [3, 'いつも昼まで寝過ごしてしまう鳥は？', 'あひる'], [4, '２匹集まると動きが遅くなる魚は？', 'たら'], [5, '植物を育てるのが苦手な鳥は？', 'からす']]

#st.write(data[0][0])
#st.header('DKSオールスター感謝祭')

st.title('🎉DKSフェスタへようこそ！')

if 'no' not in st.session_state: 
	st.session_state.no = "" #countがsession_stateに追加されていない場合，0で初期化

if 'a_no' not in st.session_state: 
	st.session_state.a_no = "" #countがsession_stateに追加されていない場合，0で初期化

st.write("❶ 従業員番号を入力してください😆")

code = st.text_input('半角英数字のみ可')
if st.button('入力'):
    for i in range(len(data)):
        if code == str(data[i][0]):
            st.session_state.no = i
            st.text('\n')
            
if st.session_state.no != "":
    st.write(data[st.session_state.no][1] + "さん、ようこそ！")
    st.write("❷ 次のなぞなぞを解いて自分のチームにたどり着こう🎈")
    for n in range(len(question)):
        if  data[st.session_state.no][3] == question[n][0]:
            st.session_state.a_no = n
            st.text('\n')
            q = question[n][1]
            st.code(q, language='python')

    if st.session_state.a_no != "":
        answer = st.text_input('答えを全角ひらがなで')
        if st.button('答え合わせ'):
            if answer != question[st.session_state.a_no][2]:
                st.write("残念…不正解です…別の回答を入れてみよう！")
            else:
                st.write("大正解！！！！！！！！")
                st.text('\n')
                st.write("❸ チームの情報を覚えておこう🙌")
                st.markdown(str(data[st.session_state.no][1]) + "さんのチーム番号は [**" + str(data[st.session_state.no][4]) + "**]！")
                st.markdown("チームの役割は [**" + str(data[st.session_state.no][2]) + "**] です。")
                st.write("\n")
                st.write("忘れずに覚えておいてね！")







