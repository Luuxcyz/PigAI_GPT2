# PigAI_GPT2

![](https://latex.codecogs.com/svg.latex?\rm%20PigAI\\_GPT_2) 批改网写作助手

## :carousel_horse: 服务条款

> 1. 本项目软件及源码禁止在国内网络环境大范围传播；
> 2. 本项目开源免费，请不要滥用接口；
> 3. 禁止任何人使用本项目及其分支提供任何形式的收费服务。

## :eagle: 快速上手

- 本项目`文本生成`内核分为![](https://latex.codecogs.com/svg.latex?\rm%20Core-Ord)与![](https://latex.codecogs.com/svg.latex?\rm%20Core-NLP)，深度学习内核暂未开源（将在今后版本发布）；
- 本项目使用`Python3`编写，短期内无“软化”动机，故需您在使用该脚本前熟悉`Python`编程环境并具备一定的`debug`能力。

### 【方案一】用户

1. **配置账号信息**

    在`/PigAI_GPT2_src/config.yaml`中配置账号信息

    - 强制填写用户名、密码与作文号，信息填写有误或残缺将无法正常启动项目；
    - 其中，`class_name`班级名称若不填写将不会在提交任务时选择班级（非强制填写项）；

```yaml
users:
  - user:
      # 登陆账号：邮箱或者手机号:字符串
      username: 'your username'
      # 账号密码：字符串
      password: 'your password'
      # 班级，请自行打开批改网，看看自己的班级全称：字符串
      class_name: your class name
      # 作文号，支持多篇作文并发，pids len ∈[1,∞）List[str]
      pids: [ '1586732' ]
```

2. **配置`Chromedriver`**

    请确保您已安装[`Chrome`谷歌浏览器](https://www.google.com/intl/zh-CN/chrome/)并配置适应您计算机操作系统的对应版本的[`chromedriver`驱动器](http://npm.taobao.org/mirrors/chromedriver/)

    - 请将正确版本的`chromedriver`放置在路径`./PigAI_GPT2_src/middleware/`之下

    ```python
    # 如果您是windows系统，应下载.exe文件并放置在上文所示路径中
    if 'win' in sys.platform:
        CHROMEDRIVER_PATH = os.path.join(ROOT_DIR_MIDDLEWARE, 'chromedriver.exe')
    elif 'linux' in sys.platform:
        CHROMEDRIVER_PATH = os.path.join(ROOT_DIR_MIDDLEWARE, 'chromedriver')
    ```

3. **确保网络通畅，拉取项目第三方依赖**

    请将`PigAI_GPT2_src`作为您工程文件的根目录，使用如下`Terminal`指令在当前环境下拉取第三方依赖。

    ```shell
    pip install -r requirements.txt
    ```

    ```sh
    # 若您网络状况较差请使用这条指令
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

4. **Enjoy it♂**

    更多疑问请在`issue`中提出或通过`email`私信作者。

    - **历史操作**

        成功运行后，可在`./PigAI_GPT2_src/database/action_history.csv`中查看历史操作。

    - **查看评测**

        成功运行后，可在`./PigAI_GPT2_src/database/paper_score/`中查看以`.mhtml`文件封装的评测结果页面。若您第一次打开这种格式的文件，请<kbd>右键</kbd>目标文件后，在<kbd>打开方式</kbd>中选择以`Chrome`、`Edge`等浏览器启动。

    - **文本长度**

        ```python
        # ---------------------------------------------------
        # TODO (√)TexLen -- 文本词数区间起点
        # 合成的文章词数不会小于TexLen，一般情况下会超出20至80个词。
        # 建议区间 TEXT_LENGTH∈[120, 460]
        # ---------------------------------------------------
        TEXT_LENGTH = 320
        ```

### 【方案二】开发者

> 本项目基于`Windows10`环境开发

- [查看项目流程图](https://github.com/QIN2DIM/PigAI_GPT2/tree/main/depot/flowchart.md)（更新中...）
- 请fork项目后继续开发:clinking_glasses:

## :video_game: 进阶玩法

### :balance_scale: 服务器部署

> 将项目部署至容器，客户端只需输入账号信息及作文号既可完成作文提交任务。

- （更新中...）

### :alien:混淆神经网络![](https://latex.codecogs.com/svg.latex?(\rm ONN))

> 一种基于回文并序自然语言阅读理解的深度学习模型（尝试适配分布式异构计算）

- （更新中...）

##  :small_red_triangle: 注意事项

- **屎山**

    本项目当前版本源码藕合度极高（本意在防止开发者恶意篡改源码用来攻击网站）。作者将在未来版本中把`批改网模拟登陆`的爬虫脚本和`阅读理解+文本生成`的深度学习模型完全解耦（毕竟这本来就是不同的任务模块）;

- **睿智**

    - 本项目深度学习内核暂未开源，当前版本使用的仍是随机语句组合方案![](https://latex.codecogs.com/svg.latex?(Core-\rm Ord));
    - <u>深度学习内核</u>生成的文本具有极强的倾略性，实测分数（批改网打分）均分保持在96.43左右，而使用<u>普通核心</u>则能达到78~89的平均范围，极少数情况出现`异常作文`；

- **提醒**

    未使用深度学习内核的脚本生成的文章与作文题目没有任何关系！应付一下平时的作业即可，请不要在利益相关的生产活动中使用！

## :loudspeaker: 更新日志

- **2020.12.26 v_0.1.1-beta**
    - 更新`README`；
    - 重构项目文档树。

## :world_map: 开源计划

- [x] 批改网自动登录脚本（登录、跳转、作文填写、班级选择、任务提交、数据持久）
    - 数据持久采用`csv + mhtml`方案
    - 自动登录采用`Python3 + Selenium`方案

- [ ] 多种阅读理解模型介绍
- [ ] 多种文本生成模型介绍
- [ ] 基于[**DIKW智慧图谱**](http://www.yucongduan.org/)技术的`智能决策+智能应答`解决方案介绍

## :email: 联系我们

> 本项目由海南大学机器人与人工智能协会数据挖掘小组(`A-RAI.DM`)提供维护

- [**Email**](mailto:RmAlkaid@outlook.com?subject=CampusDailyAutoSign-ISSUE) **||** [**Home**](https://a-rai.github.io/)

## :link: 参考资料

[^Latex-Markdown渲染]: https://latex.codecogs.com/

