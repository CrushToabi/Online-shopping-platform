#coding:utf-8
from django.db import models
from .model import BaseModel
from datetime import datetime

class shangjia(BaseModel):
	__doc__ = u'''shangjia'''
	__tablename__ = 'shangjia'
	__loginUser__='zhanghao'
	__authTables__={}
	__authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	zhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='账号' )
	mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
	shangjiaxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商家姓名' )
	xingbie=models.CharField ( max_length=255,null=False, unique=False, verbose_name='性别' )
	touxiang=models.TextField   ( null=False, unique=False, verbose_name='头像' )
	youxiang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='邮箱' )
	lianxidianhua=models.CharField ( max_length=255,null=False, unique=False, verbose_name='联系电话' )
	money=models.FloatField ( null=False, unique=False,verbose_name='余额' )
	class Meta:
		db_table = 'shangjia'
		verbose_name = verbose_name_plural = '商家'

class yonghu(BaseModel):
	__doc__ = u'''yonghu'''
	__tablename__ = 'yonghu'
	__loginUser__='yonghuming'
	__authTables__={}
	__authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__loginUserColumn__='yonghuming'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	yonghuming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
	mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
	xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
	touxiang=models.TextField   ( null=False, unique=False, verbose_name='头像' )
	xingbie=models.CharField ( max_length=255,null=False, unique=False, verbose_name='性别' )
	youxiang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='邮箱' )
	shouji=models.CharField ( max_length=255,null=False, unique=False, verbose_name='手机' )
	money=models.FloatField ( null=False, unique=False,verbose_name='余额' )
	class Meta:
		db_table = 'yonghu'
		verbose_name = verbose_name_plural = '用户'

class aboutus(BaseModel):
	__doc__ = u'''aboutus'''
	__tablename__ = 'aboutus'
	__authTables__={}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
	subtitle=models.CharField ( max_length=255,null=False, unique=False, verbose_name='副标题' )
	content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
	picture1=models.TextField   ( null=False, unique=False, verbose_name='图片1' )
	picture2=models.TextField   ( null=False, unique=False, verbose_name='图片2' )
	picture3=models.TextField   ( null=False, unique=False, verbose_name='图片3' )
	class Meta:
		db_table = 'aboutus'
		verbose_name = verbose_name_plural = '关于我们'

class address(BaseModel):
	__doc__ = u'''address'''
	__tablename__ = 'address'
	__authTables__={}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='用户id' )
	address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
	name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
	phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
	isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='是否默认地址[是/否]' )
	class Meta:
		db_table = 'address'
		verbose_name = verbose_name_plural = '地址'

class bangzhu(BaseModel):
	__doc__ = u'''bangzhu'''
	__tablename__ = 'bangzhu'
	__authTables__={}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	wenti=models.CharField ( max_length=255,null=False, unique=False, verbose_name='问题' )
	fengmiantupian=models.TextField   ( null=False, unique=False, verbose_name='封面图片' )
	bangzhuhuida=models.TextField   ( null=False, unique=False, verbose_name='帮助回答' )
	fabushijian=models.DateField   (  null=True, unique=False, verbose_name='发布时间' )
	class Meta:
		db_table = 'bangzhu'
		verbose_name = verbose_name_plural = '帮助'

class cart(BaseModel):
	__doc__ = u'''cart'''
	__tablename__ = 'cart'
	__authTables__={}
	__authSeparate__='是'#后台列表权限
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	tablename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品表名' )
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='用户id' )
	goodid=models.BigIntegerField  ( null=False, unique=False,verbose_name='商品id' )
	goodname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
	picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
	buynumber=models.IntegerField  (  null=True, unique=False,verbose_name='购买数量' )
	price=models.FloatField ( null=False, unique=False,verbose_name='单价' )
	discountprice=models.FloatField ( null=False, unique=False,verbose_name='会员价' )
	zhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商户名称' )
	goodtype=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品类型' )
	class Meta:
		db_table = 'cart'
		verbose_name = verbose_name_plural = '购物车表'

class chat(BaseModel):
	__doc__ = u'''chat'''
	__tablename__ = 'chat'
	__authTables__={}
	__foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='用户id' )
	adminid=models.BigIntegerField  ( null=False, unique=False,verbose_name='管理员id' )
	ask=models.TextField   ( null=False, unique=False, verbose_name='提问' )
	reply=models.TextField   ( null=False, unique=False, verbose_name='回复' )
	isreply=models.IntegerField  (  null=True, unique=False,verbose_name='是否回复' )
	class Meta:
		db_table = 'chat'
		verbose_name = verbose_name_plural = '联系我们'

class chathelper(BaseModel):
	__doc__ = u'''chathelper'''
	__tablename__ = 'chathelper'
	__authTables__={}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	ask=models.CharField ( max_length=255,null=False, unique=False, verbose_name='提问' )
	reply=models.TextField   ( null=False, unique=False, verbose_name='回复' )
	class Meta:
		db_table = 'chathelper'
		verbose_name = verbose_name_plural = '聊天助手表'

class messages(BaseModel):
	__doc__ = u'''messages'''
	__tablename__ = 'messages'
	__authTables__={}
	__hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
	__foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='留言人id' )
	username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
	avatarurl=models.TextField   ( null=False, unique=False, verbose_name='头像' )
	content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
	cpicture=models.TextField   ( null=False, unique=False, verbose_name='留言图片' )
	reply=models.TextField   ( null=False, unique=False, verbose_name='回复内容' )
	rpicture=models.TextField   ( null=False, unique=False, verbose_name='回复图片' )
	class Meta:
		db_table = 'messages'
		verbose_name = verbose_name_plural = '留言交流'

class news(BaseModel):
	__doc__ = u'''news'''
	__tablename__ = 'news'
	__authTables__={}
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
	introduction=models.TextField   ( null=False, unique=False, verbose_name='简介' )
	picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
	content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
	class Meta:
		db_table = 'news'
		verbose_name = verbose_name_plural = '商城资讯'

class orders(BaseModel):
	__doc__ = u'''orders'''
	__tablename__ = 'orders'
	__authTables__={'zhanghao':'shangjia',}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	orderid=models.CharField ( max_length=255,null=False, unique=False, verbose_name='订单编号' )
	tablename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品表名' )
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='用户id' )
	goodid=models.BigIntegerField  ( null=False, unique=False,verbose_name='商品id' )
	goodname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
	picture=models.TextField   ( null=False, unique=False, verbose_name='商品图片' )
	buynumber=models.IntegerField  (  null=True, unique=False,verbose_name='购买数量' )
	price=models.FloatField ( null=False, unique=False,verbose_name='价格' )
	discountprice=models.FloatField ( null=False, unique=False,verbose_name='折扣价格' )
	total=models.FloatField ( null=False, unique=False,verbose_name='总价格' )
	discounttotal=models.FloatField ( null=False, unique=False,verbose_name='折扣总价格' )
	type=models.IntegerField  (  null=True, unique=False,verbose_name='支付类型' )
	status=models.CharField ( max_length=255,null=False, unique=False, verbose_name='状态' )
	address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
	tel=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
	consignee=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
	remark=models.CharField ( max_length=255,null=False, unique=False, verbose_name='备注' )
	logistics=models.TextField   ( null=False, unique=False, verbose_name='物流' )
	zhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商户名称' )
	goodtype=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品类型' )
	class Meta:
		db_table = 'orders'
		verbose_name = verbose_name_plural = '订单'

class remenshangpin(BaseModel):
	__doc__ = u'''remenshangpin'''
	__tablename__ = 'remenshangpin'
	__authTables__={'zhanghao':'shangjia',}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	shangpinmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
	shangpinfenlei=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品分类' )
	tupian=models.TextField   ( null=False, unique=False, verbose_name='图片' )
	pinpai=models.CharField ( max_length=255,null=False, unique=False, verbose_name='品牌' )
	zhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='账号' )
	shangjiaxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商家姓名' )
	shangjiariqi=models.DateField   (  null=True, unique=False, verbose_name='上架日期' )
	shangpinxiangqing=models.TextField   ( null=False, unique=False, verbose_name='商品详情' )
	onelimittimes=models.IntegerField  (  null=True, unique=False,verbose_name='单限' )
	alllimittimes=models.IntegerField  (  null=True, unique=False,verbose_name='库存' )
	clicktime=models.DateTimeField  (  null=True, unique=False,verbose_name='最近点击时间' )
	price=models.FloatField ( null=False, unique=False,verbose_name='价格' )
	class Meta:
		db_table = 'remenshangpin'
		verbose_name = verbose_name_plural = '热门商品'

class shangpinfenlei(BaseModel):
	__doc__ = u'''shangpinfenlei'''
	__tablename__ = 'shangpinfenlei'
	__authTables__={}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	shangpinfenlei=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品分类' )
	class Meta:
		db_table = 'shangpinfenlei'
		verbose_name = verbose_name_plural = '商品分类'

class storeup(BaseModel):
	__doc__ = u'''storeup'''
	__tablename__ = 'storeup'
	__authTables__={}
	__authSeparate__='是'#后台列表权限
	__foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='用户id' )
	refid=models.BigIntegerField  ( null=False, unique=False,verbose_name='商品id' )
	tablename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='表名' )
	name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
	picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
	type=models.CharField ( max_length=255,null=False, unique=False, verbose_name='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
	inteltype=models.CharField ( max_length=255,null=False, unique=False, verbose_name='推荐类型' )
	remark=models.CharField ( max_length=255,null=False, unique=False, verbose_name='备注' )
	class Meta:
		db_table = 'storeup'
		verbose_name = verbose_name_plural = '收藏表'

class youqinglianjie(BaseModel):
	__doc__ = u'''youqinglianjie'''
	__tablename__ = 'youqinglianjie'
	__authTables__={}
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	qiyemingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='企业名称' )
	tupian=models.TextField   ( null=False, unique=False, verbose_name='图片' )
	lianjiewangzhi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='链接网址' )
	lianxidianhua=models.CharField ( max_length=255,null=False, unique=False, verbose_name='联系电话' )
	class Meta:
		db_table = 'youqinglianjie'
		verbose_name = verbose_name_plural = '友情链接'

class discussremenshangpin(BaseModel):
	__doc__ = u'''discussremenshangpin'''
	__tablename__ = 'discussremenshangpin'
	__authTables__={}
	addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
	refid=models.BigIntegerField  ( null=False, unique=False,verbose_name='关联表id' )
	userid=models.BigIntegerField  ( null=False, unique=False,verbose_name='用户id' )
	avatarurl=models.TextField   ( null=False, unique=False, verbose_name='头像' )
	nickname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
	content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
	reply=models.TextField   ( null=False, unique=False, verbose_name='回复内容' )
	class Meta:
		db_table = 'discussremenshangpin'
		verbose_name = verbose_name_plural = '热门商品评论表'
