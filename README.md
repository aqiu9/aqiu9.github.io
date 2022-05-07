**改编于TinyBlog —>** https://github.com/YangHanqing/tinyblog、https://github.com/eastzq/eastzq.github.io

### About
1. 博客地址：https://aqiu9.github.io
2. 递归blog目录生成**.md**的文件树，支持搜索文章。
3. 图片默认是放在md文件所在的目录 or ./assets文件夹。加载时自动替换图片url。故不依赖文件服务器。
4. 支持锚点定位和文章链接。
5. 使用editormd插件。把md文档转换成html，目录自动生成。
6. 使用gitalk集成评论功能。
7. 使用config.json作为顶级配置文件，方便修改关键参数。
8. 采用混淆后的js支持简单的文件or文件夹的**访问控制**。

### config.json
1. 想开启评论功能需要配置clientID clientSecret commentRepo三项属性。
   
   详见gitalk文档 https://github.com/gitalk/gitalk/blob/master/readme-cn.md
   

### TODO
1. 虽然editor.md能支持katex解析，但是测试了一天发现博客里还是不能解析md里的公式，katex、latex虽然语法不一样，但是都可以用$$...$$ 做分界符，这是一个在本地latex和博客katex都兼容的方法，我用python脚本进行了替换，但是最后卡在了博客在转化为html时，会少一个'\' 导致katex语法错误  不知道哪里把\给转义掉了一个
  
CNMD！！！  
