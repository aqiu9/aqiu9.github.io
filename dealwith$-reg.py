
import re,os

rootdir=r"E:\00xx\Js_psxb\aqiu9.github.io\blog\major\linear-algebra_MIT\docs"  #注意字符串前r的作用 有时候没r就会有问题

# content = "$Ax=\lambda x$你 $ax=1$和 $$ax=a$$"
# ret0 = re.sub(r'(?<!\$)(\$)([^\\，。\u4e00-\u9fff]+)(\$)(?!\$)', r'\2', content)
# print("ret0="+ret0)
# ret1 = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', r'$$\1$$', ret0)
# print("ret1="+ret1)

# exit()
def modify_file(filepath):
        with open(filepath, 'r', encoding='utf-8-sig') as f:
                print(filepath)
                content = f.read()
                print("content="+content)
        with open(filepath, 'w', encoding='utf-8-sig') as f:
                # content = "$Ax=\lambda x$你 $ax=1$和 $$ax=a你好$$"
                ret0 = re.sub(r'(?<!\$)(\$)([^\\，\$。^_\u4e00-\u9fff]+)(\$)(?!\$)', r'\2', content)
                print("ret0="+ret0)
                ret1 = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', r'$$\1$$', ret0)
                # print("ret1="+ret1)
                f.write(ret1)
                f.close()

for pwd, dirnames, filenames in os.walk(rootdir):  #pwd is the directory, dirnames and filenames are Recursively!!
    for fname in filenames:
        print("fname=%s" % fname)
        if(fname.endswith(".md")):
            modify_file(pwd+"\\"+fname)



