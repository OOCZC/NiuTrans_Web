def mtChinese(Chinese):
    import jieba
    seg_list = jieba.cut(Chinese, cut_all=False)
    with open("Chinese.txt", 'w') as f:
        for i in seg_list:
            f.write(i + " ")
    import subprocess, os
    os.chdir('/opt/niutrans/NiuTrans_1.3.1_Beta_source_code/scripts')
    subprocess.call(["perl", "/opt/niutrans/NiuTrans_1.3.1_Beta_source_code/scripts/NiuTrans-phrase-decoder-model.pl", "-test", "~/Github/niutrans_web/Chinese.txt", "-c", "/opt/niutrans/NiuTrans_1.3.1_Beta_source_code/work/NiuTrans.phrase.user.config", "-output", "~/Github/niutrans_web/English.txt"])
    #print("ooc")
    os.chdir('/home/ooc/Github/niutrans_web')
    with open("English.txt", 'r') as f:
        return f.read()
