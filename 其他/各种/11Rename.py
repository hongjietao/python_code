import os
n = [311709001307, 311709000423, 311709001222, #学号
     311709000303, 311709001022, 311709000824,
     311709000710, 311709000705, 311709001227,
     311709000508, 311709001310, 311709001003,
     311709001011, 311709001110, 311709000422,
     311703030305, 311705000820, 311709001212,
     311709000910, 311709001303, 311709001317,
     311709000912, 311709000114, 311702050202,
     311709000525, 311709000219, 311709000511,
     311709001103, 311707010214, 311709001123,
     311709001029, 311609000501, 311709001223]

name1 = ['陈永强', '邓哲理', '付  润', '高佳豪', '何俊飞',
         '黄秋钊', '金佳佳', '李鸣霄', '李硕晨', '李腾宇',
         '李志斌', '卢艳军', '罗思超', '马瑞柯', '马嵛森',
         '汤迎新', '陶鸿杰', '王金发', '王珂珂', '王顺达',
         '王顺强', '王子韧', '武茁壮', '席  康', '熊家辉',
         '于发林', '袁惠娟', '张华山', '张静怡', '张蓬勃',
         '张晓庆', '张晓雯', '赵  辉']


i=0
path = ( r'C:\Users\Administrator\Desktop\计算机1704\b')  # 一定要加r转义 单引号
filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
for files in filelist:  # 遍历所有文件
    i = i+1
    # print(files)
    Olddir=os.path.join(path,files) #  原来的文件路径
    filename=os.path.splitext(files)[0]  #  文件名
    #filetype = os.path.splitext(files)[1];  # 文件扩展名
    filetype='.jpg'
    Newdir=os.path.join(path,('计算机1704'+str(name1[i])+'b')+filetype) #  新的文件路径
    os.rename(Olddir,Newdir) #  重命名
    print(i)



