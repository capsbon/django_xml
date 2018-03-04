部署环境
	CentOS 7.3
	python 3.5

■部署服务
按照以下的顺序进行部署：
1 以root账户登陆
2 解压Maximum.tar文件至/home/Maximum目录
3 cd /home/Maximum
4 安装所需要的的库
  pip install -r requirements.txt
5 启动项目
  python manage.py runserver 0:8000
  
■主要功能：
1.读取服务器上MySQL数据库数据并展示
2.修改展示数据并上传至MySQL数据库
3.数据修改需要进行登录，提供登录以及登出功能
  登录所需用户名/密码：admin/123456
4.修改完成提交后会显示修改后的数据并提示
5.点击export按钮会将MySQL数据库中数据转存到csv文件中并提供下载功能

■介绍：
目前项目运行在我自己的服务器上
地址：http://173.199.118.8:8000/vacancies
可以随时访问查看效果