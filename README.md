# 🚀🚀🚀auto-youth-study
- 👍青年大学习自动完成观看记录，秒完成脚本

## 🚀使用方法和说明
- 只需要修改代码第46行的mid值即可
- 获取mid的方法见后面
- 仅限广东地区

## 思路
- 通过抓包软件去分析

最终在这个URL
```
https://youthstudy.12355.net/apih5/api/young/course/chapter/saveHistory
```
里面保存观看记录
> 拿到token(X-Litemall-Token)和章节id(ChapterId)就可以去save了  post
- 章节id可以直接get获取   get
- token获取方法：
    - 需要获取mid  (登录时候必要的)
    - 通过mid获取sign   get
    - 通过sign获取token   post


## 2种获取mid的方法
- 可以通过抓包的形式，可以参考这个[抓包分析](https://www.zhouxuebin.club/blog/2021/06/01/qndxx/)
- 也可以通过下面这种比较方便的方法：
  - 1 微信公众号打开广东共青团
  - 2 点击下面的智慧团建，随便点个进去系统，比如组织转接或者团员报到
  - 3 点击认证资料
  - 4 点击生成电子团员证
  - 5 点击最下方的生成按钮
  - 6 在团员证页面复制链接，得到：```https://tuan.12355.net/wechat/view/information/member_certification_generated.html?memberId=xxxxxxx&showMemberAdditionNames=&showMemberRewardIds=&isShowAllFee=true```
  - 7 然后6中的```memberId=xxxxxxx```的```xxxxxxx```就是你的mid 

- 把mid黏贴到代码里面主函数的mid那里就可以跑代码了
```python
if __name__ == '__main__':
    mid = 'xxxxxxx'
```


## 原理
- 一般来说，每次观看完视频，在```我的```那里的记录可以看到自己的观看记录，而系统导出的谁已学和谁未学就是根据这个观看记录来判断的
- 只要用你的微信号登上去，点击开始学习，看个几秒视频，然后退出去，就会有保存观看记录了
- 所以原理就是只要模拟手动保存观看记录即可，也就是说本质上不需要全部看完整个视频才有记录，看了一两秒即可退出就是已学的状态了
- 而实际上需要完成界面的截图，那玩意是上面的人怕你没学才让你发的，吓唬你的，实际上不需要截图这种东西


## 注意
- mid包含个人的信息，请大家自己保护好自己的mid不要泄露
- 代码仅供大家私用和学习，不可用于违法交易

## Link
- 每天自动跑一次，可以在github actions自己配置一下，[参考我这个版本](https://github.com/JimouChen/auto-youth-study-gd)
    - mid值在Settings —— Secrets可以自己添加键值对，这样只有自己可以看到，别人是看不到的
- Go语言版实现的[参考我这个版本](https://github.com/JimouChen/auto-youth-study-go)

