# 我形我塑
## EDGE &mdash; 开源舞蹈动作生成模型代码精读

+ 原项目链接: https://github.com/Stanford-TML/EDGE
+ [原项目README](README_Original.md)
+ 作业Github链接: https://github.com/kasaki0900/software-homework

### 1. 为什么选用EDGE
本小组成员在大创项目中使用过EDGE开源代码，
对该项目结构、代码风格以及运行环境有一定了解；
且对代码的部分功能进行过测试、应用和优化。
  
### 2. 项目功能
EDGE代码功能主要包括训练和生成。
+ 运行train.py脚本可以下载作者提供的视频数据集，并基于此训练集优化模型参数。


+ 运行test.py脚本进行生成测试，输入参数指定路径下的所有wav音频文件，
为每段音频生成一段相匹配的舞蹈动作(.pkl格式)，
不选用--no_render参数时还会为每段动作生成一段演示视频(音频视频结合)。


+ 运行SMPL-to-FBX/Convert.py脚本
可以将生成的.pkl文件转换成主流动画软件可用的.fbx文件
该脚本来自项目 https://github.com/softcat477/SMPL-to-FBX


+ 顺序运行demo.ipynb，
可从网络上下载音频文件并直接生成.fbx动作文件，快速体验舞蹈生成功能。


### 3. 作业内容
本项目对EDGE源代码进行了解读和标注。

由于EDGE原作者在代码功能的底层实现部分已经进行了非常细致的注释，
故本项目的标注主要集中在代码的顶层架构，即EDGE.py脚本。
对于底层实现部分则在大部分python文件开头说明了该模块的主要功能和应用场景，
并补充了个别注释。
