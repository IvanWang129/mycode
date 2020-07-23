
paticipant = [{"name":"Ivan","DOB":"19841229","Elite":"N","Finish_Time":"148"},
              {"name":"Erick","DOB":"19811015","Elite":"Y","Finish_Time":"130"},
              {"name":"ZhaoYang","DOB":"19931016","Elite":"N","Finish_Time":"160"},
              {"name":"Yuting","DOB":"19831114","Elite":"Y","Finish_Time":"120"},
              {"name":"Fengfan","DOB":"19900708","Elite":"N","Finish_Time":"150"},
              {"name":"Sen","DOB":"19830108","Elite":"N","Finish_Time":"180"},
              {"name":"Shilei","DOB":"19891117","Elite":"N","Finish_Time":"200"},
              {"name":"Zhangkai","DOB":"19931204","Elite":"N","Finish_Time":"190"},
              {"name":"Wushuang","DOB":"19940704","Elite":"N","Finish_Time":"210"},
              {"name":"Hanxizhen","DOB":"19900605","Elite":"N","Finish_Time":"140"}
]

'''
for item in paticipant:
    print("姓名:"+item["name"]+"，出生日期:"+str(item["DOB"])+"，是否为精英选手:"+item["Elite"]+"，完赛时长:"+str(item["Finish_Time"])+"分钟")
'''

sorted_paticipant=sorted(paticipant,key=lambda paticipant:paticipant['Finish_Time'],reverse=False)
for item in sorted_paticipant:
    print ("姓名:"+item["name"]+"，出生日期:"+str(item["DOB"])+"，是否为精英选手:"+item["Elite"]+"，完赛时长:"+str(item["Finish_Time"])+"分钟")
