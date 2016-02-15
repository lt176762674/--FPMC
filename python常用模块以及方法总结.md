#python常用模块以及方法总结
##一、python执行系统命令
>三种方法：
>
>>os.system('命令')
>>
>>os.popen('命令')
>>
>>commands.getstatusoutput('命令')
>>

###比较三种方法的差异：
执行以下脚本：

    -*- coding: UTF-8 -*-
    import commands
    import os

    os.system('cat /proc/cpuinfo')

    os.popen('cat /proc/cpuinfo').read()
    #print output

    i = commands.getstatusoutput('cat /proc/cpuinfo')
    print i
    
输出结果：
![output logo](http://cl.ly/3A372S30163Q/download/Image%202016-02-16%20at%2012.37.44%20%E4%B8%8A%E5%8D%88.png)

**os.system()**:无法获取输出和返回值（别人的博客上写的，实际输出能看到，不知道为啥）
**os.popen().read()**:popen获得的返回值是.read()的对象
**commands.getstatusoutput()**:获得返回值并且能看到对应的结果码