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
1. （已修复）虽然editor.md能支持katex解析，但是测试了一天发现博客里还是不能解析md里的公式，katex、latex虽然语法不一样，但是都可以用\$\$...\$\$ 做分界符，这是一个在本地latex和博客katex都兼容的方法，我用python脚本进行了替换，但是最后卡在了博客在转化为html时，会少一个'\\' 导致katex语法错误  不知道哪里把'\\'给转义掉了一个。
   - 修改了editormd.js的源码，其中调用katex的渲染接口只有两处，都是editormd.katex.render(xx, xx); 修改这两处即可，根据个人实践（能力和时间有限），第一处是影响无UI把katex渲染到HTML的，第二处是影响可视化编辑器的渲染结果。则修改第一处render调用即可，可以加上第三个参数(katex的配置文件-json对象)，并在渲染之前对输入的delimiter内的katex源码，进行过滤转换，把\&lt;、\&gt;、\&amp;(本人新增)，都转换为原始符号(至于为什么不是原始符号而是HTML中的那种形式，没有花时间追究，根据源码应该是由于先把md转换为HTML了，过程中可能会自动把上面相关符号转为\&xxx;转义的形式)；
     - xxx.replace(/\&amp;/g, "&")
   - 解决了\<br>标签无法解析的问题，不知道为何katex源码里还会带有HTML的换行标签，会导致解析错误(无论throwOnError为true还是false)，可能的原因还是md转为HTML时把在本地编辑器里输入的换行给无差别翻译成了\<br>标签，包括了katex源码中的这种回车换行。
     - xxx.replace(/\<br>/g, " ").replace(/\\\\\(?![A-z])/g, "\\\\\\\\")，注意js里也会转义'\\'

2. （已修复）本地Typora的Latex语法和blog中的Katex语法解析的兼容问题。我的思路有两个，一个是如第一条问题所述，全都用\$\$做界定符来识别Tex源码，同时把行内的一些短小的，比如\$2\$,\$A\$这种，给她去掉\$，以普通文本显示，这样能减少公式块，让页面好看一点，不过说到底这种方式还是曲线救国的方式，不是最佳选择。第二个是尝试能否应用katex官网的 *Auto*-render *Extension*  ，其可以实现自定义delimiter，以解决该问题。

   - 第一种方式可采用根目录下的脚本：dealwith\$-reg.py
   - （无效）第二种方式尝试修改源码如下：

   ```javascript
   //可能是因为时机不对，在配置auto-render应该在dom初次加载完成的时候，目前这些修改的位置似乎都已经过了这个阶段。
   //modified in editormd.js, //js_autoRender-->editormd.loadKaTeX-->this.loadKaTeX-->katexHandle
   //修改了katex的版本，使用最新的0.15版本。原本是0.3。
           editormd.katexURL  = {
               css : "//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.1/katex.min",
               js  : "//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.1/katex.min",
               js_autoRender : "//cdn.jsdelivr.net/npm/katex@0.15.3/dist/contrib/auto-render.min",
           };
   
   //THEN
           editormd.loadKaTeX = function (callback) {
               // editormd.loadCSS(editormd.katexURL.css, function(){
               //     editormd.loadScript(editormd.katexURL.js, callback || function(){});
               // });
               editormd.loadCSS(editormd.katexURL.css, function(){
                   editormd.loadScript(editormd.katexURL.js, function(){
                        editormd.loadScript(editormd.katexURL.js_autoRender, callback || function(){});
                   });
               });
           };
   
   //THEN
           if (settings.autoLoadKaTeX && !editormd.$katex && !editormd.kaTeXLoaded)
           {
               this.loadKaTeX(function() {
                   editormd.$katex      = katex;
                   editormd.kaTeXLoaded = true;
                   katexHandle();
               });
           }
           else
           {
               katexHandle();
           }
           
   //THEN
           var katexHandle = function() {
               //添加的 auto-render (js_autoRender后续脚本)，配合的监听器
               document.addEventListener("DOMContentLoaded", function() {
                   renderMathInElement(document.body, {
                       // customised options
                       // • auto-render specific keys, e.g.:
                       delimiters: [
                           {left: '$$', right: '$$', display: true},
                           {left: '$', right: '$', display: false},
                           {left: '\\(', right: '\\)', display: false},
                           {left: '\\[', right: '\\]', display: true}
                       ],
                       // • rendering keys, e.g.:
                       throwOnError : false
                   });
               });    
   
   
               div.find("." + editormd.classNames.tex).each(function(){
                   var tex  = $(this);                    
                   //<br>\begin{aligned}<br>A \cdot A^{-1} = I & = A^{-1} \cdot A\<br>(AB) \cdot (B^{-1}A^{-1}) & = I\<br>\textrm{则} AB \textrm{的逆矩阵为} & B^{-1}A^{-1}<br>\end{aligned}<br>
                   katex.render(tex.html().replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&").replace(/<br>/g, " ").replace(/\\(?=[ ])/g, "\\\\"), tex[0], {
                       "displayMode":true,
                       "throwOnError":false
                   });                    
                   tex.find(".katex").css("font-size", "1.6em");
               });
           };
   ```
