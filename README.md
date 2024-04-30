## 项目介绍

这是我和我的另一位小组成员为《唐诗宋词人文解读》通识课的交叉作业编写的一个项目， 它实现了以下几个功能：

1. 根据用户填入的信息匹配与它最相似的诗人

2. 用户可输入标题， 该应用将模仿 （1） 中的诗人的风格进行作诗

3. 用户可指定关键词， 该应用将生成一首相关的唐诗 / 宋词

其中， 我负责：

1. 爬虫

2. 编写 “根据用户填入的信息匹配与它最相似的诗人”部分的匹配规则

3. 编写网页前端

4. 用 python flask 框架写网页后端

5. 租服务器并部署

我的同学负责了生成诗词算法的部分，他比较懂 NLP。

### 使用方式

请先安装依赖：

``` shell
./data/poet_gene/make_env_2.sh
./data/poem_gene/make_env.sh
```

然后可以使用以下命令本地部署：

```shell
./data/run_script.sh
```

### 文件架构

```
./
├── README.md
├── data #data 中包含了 web 应用的所有主程序。
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── app.cpython-310.pyc
│   │   ├── backend.cpython-310.pyc
│   │   └── poetplus.cpython-310.pyc
│   ├── app.py #这是 web 应用后端主程序
│   ├── backend.py #app.py 调用的一个库，封装了匹配规则
│   ├── nohup.out
│   ├── output.pkl #把爬虫结果存在了 .pkl 文件里面
│   ├── poem_gene #这部分是生成 poem_gene 的代码
│   │   ├── __pycache__
│   │   │   └── sequential_generate.cpython-310.pyc
│   │   ├── make_env.sh
│   │   ├── sequential_generate.py
│   │   └── sequential_generator
│   │       ├── README.md
│   │       ├── added_tokens.json
│   │       ├── config.json
│   │       ├── model.safetensors
│   │       ├── model.safetensors_Zone.Identifier
│   │       ├── runs
│   │       │   ├── Dec19_23-57-09_c60f44f3a10e
│   │       │   │   └── events.out.tfevents.1703030304.c60f44f3a10e.492.1
│   │       │   ├── Dec20_00-02-51_c60f44f3a10e
│   │       │   │   └── events.out.tfevents.1703030578.c60f44f3a10e.492.2
│   │       │   ├── Dec20_00-05-13_c60f44f3a10e
│   │       │   │   └── events.out.tfevents.1703030724.c60f44f3a10e.492.3
│   │       │   └── Dec20_00-08-19_c60f44f3a10e
│   │       │       └── events.out.tfevents.1703030909.c60f44f3a10e.492.4
│   │       ├── special_tokens_map.json
│   │       ├── tokenizer.json
│   │       ├── tokenizer_config.json
│   │       ├── training_args.bin
│   │       └── vocab.txt
│   ├── poet_gene #这个也是生成 poem_gene 的代码
│   │   ├── __pycache__
│   │   │   └── poet_generate.cpython-310.pyc
│   │   ├── chinese-poem-t5-v2
│   │   │   ├── README.md
│   │   │   ├── config.json
│   │   │   ├── pytorch_model.bin
│   │   │   ├── special_tokens_map.json
│   │   │   ├── spiece.model
│   │   │   └── tokenizer_config.json
│   │   ├── make_env_2.sh
│   │   └── poet_generate.py
│   ├── poetplus.py #一个辅助 module
│   ├── run_script.sh #本地部署的脚本
│   └── templates #这部分是前端 html + js ＋ css
│       ├── index.html
│       ├── main.html
│       ├── poem.html
│       ├── poem_result.html
│       ├── poet_result.html
│       ├── task3rd.html
│       └── task3rd_result.html
└── data-processing #这个是爬虫文件夹
    ├── author_info.pkl
    ├── author_info2.pkl
    ├── author_info3.pkl
    ├── author_info_final.pkl
    ├── authors_set.pkl
    ├── fetching.py
    ├── fetching2.py
    ├── fetching3.py
    ├── main.py #爬虫的主文件
    ├── my_json.py
    ├── output.pkl
    ├── output.txt
    ├── output1.txt
    ├── output2.txt
    ├── output2pickle.py
    ├── output3.txt
    ├── poems.pkl
    ├── poet.py
    └── transform.py #格式转换的代码
```


···························································

补充一下我当时写的小总结， 可能比较简略：

# 总步骤


1. 使用 python 编写爬虫程序。 先爬出诗人列表， 再根据诗人列表爬百度百科爬取信息。
2. 使用 python 程序对爬下来的数据做格式统一。 数据存储在一个 .pkl 文件里。
3. 编写网页后端， 使用 python 实现。 具体而言， 我们使用了 flask 框架， 主要逻辑即为根据用户输入的信息在数据库中匹配查找。
4. 编写网页前端。 使用 html / javascript 实现。 这里 javascript 为网页的输入框添加了粒子特效和淡入特效。
5. 本地部署应用程序。
6. 租用服务器， 使用服务器部署应用程序。 
7. 对后端逻辑进行参数调整和性能调优。

## 前端部分

写 html css javascript
javascript写了粒子特效和淡入特效
然后调整模块
学到了html的结构、 跳转方式， 以及后端怎么把参数传进去

```cpp
render_template('poem_result.html', line1=line1, line2=line2, line3=line3, line4=line4, line5=line5, line6=line6)
```

写javascript函数比如

```cpp
<script>

         // JavaScript function to go back to the previous page

         function goBack() {

            window.history.go(-4);

        }

    </script>
```
这样就可以跳转到前第4个页面

## 后端部分

用的是 python flask 框架

使用 @app.route()处理路由：
```cpp
@app.route('/', methods=['GET', 'POST'])

def main():

    return render_template('main.html')

  

@app.route('/poet', methods=['GET', 'POST'])

def index():

    return render_template('index.html')

  

@app.route('/poem', methods=['GET', 'POST'])

def poem():

    return render_template('poem.html')


@app.route('/poem/result', methods=['POST'])

def poem_result():

    if request.method == 'POST':
    ...
```

主函数：
```cpp
if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 80, debug = False)
    //host = '0, 0, 0, 0' 就表示接收所有IP地址的请求， port80是程序运行的端口
```

可以 flask run 本地部署

然后还可以用flask的session存变量：

```python
  

        session['name'] = name  # 将名字存储在会话中

        session['results'] = results

        session['rank'] = rank
```

```python
if request.method == 'POST':

        name = session.get('name', '')  # 从会话中获取名字数据

        title = request.form.get('title')
```

判断匹配的逻辑 

1. 词向量匹配（本地部署） 
2.  字符串距离

## 服务器部署

### 困难

阿里云服务器安全组设置有误
域名无法解析：实际上是没有备案

app.run(host = )
这个host最开始写成了127.0.0.1,但是实际上，它应该能接受来自任意IP地址的请求，所以写成0.0.0.0才对

## 远程连接服务器：
ssh username@remote_host

## 传输文件：

scp /path/to/local/file username@remote_host:/path/to/destination

例如：scp -r * root@121.196.238.115:/home

## 查看端口使用情况

lsof -i :port

例如：
```
root@iZbp1bsqqw1p1a6ocxgq5xZ:/home/poem/data# lsof -i :80
COMMAND      PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
AliYunDun   1316 root   12u  IPv4  518890      0t0  TCP iZbp1bsqqw1p1a6ocxgq5xZ:36154->100.100.30.27:http (ESTABLISHED)
gunicorn  190250 root    5u  IPv4 1724009      0t0  TCP *:http (LISTEN)
gunicorn  190533 root    5u  IPv4 1724009      0t0  TCP *:http (LISTEN)
gunicorn  205202 root    5u  IPv4 1724009      0t0  TCP *:http (LISTEN)
gunicorn  205219 root    5u  IPv4 1724009      0t0  TCP *:http (LISTEN)
gunicorn  205443 root    5u  IPv4 1724009      0t0  TCP *:http (LISTEN)
```

## 查看进程情况

top命令

## kill进程

kill PID

强制： kill -9 PID

## 服务器上使用 code 命令

需要添加系统变量

sudo ln -s /usr/bin/code /usr/local/bin/code

### WSGI：

`gunicorn`: 这是一个Python的WSGI (Web Server Gateway Interface) HTTP服务器，用于运行Python Web应用程序。它是一个高性能的HTTP服务器，常用于部署Flask、Django等Web应用。

解释这个命令：

```
nohup gunicorn -w 4 -b 0.0.0.0:80 app:app &
```

- `nohup`: 用于在终端关闭后继续运行命令，即使终端被关闭也不会中断进程。这个命令通常用于在后台运行长时间执行的任务。
    
- `gunicorn`: 这是一个Python的WSGI (Web Server Gateway Interface) HTTP服务器，用于运行Python Web应用程序。它是一个高性能的HTTP服务器，常用于部署Flask、Django等Web应用。
    
- `-w 4`: 指定了启动的Worker进程数量，这里设置为4个Worker进程。Worker进程负责处理来自客户端的请求，多个Worker进程可以提高服务器的并发处理能力。
    
- `-b 0.0.0.0:80`: 指定了服务器的监听地址和端口号。`0.0.0.0`表示监听所有可用的网络接口，`80`表示监听的端口号为80。这样配置后，服务器将监听来自所有网络接口的HTTP请求，并在80端口上进行处理。
    
- `app:app`: 指定了要运行的应用程序。在这里，`app`指的是应用程序的模块名或者对象名，`app`后面的`app`表示应用程序对象。这种形式通常在Flask等Web框架中使用，其中`app`是应用程序对象的名称。
    
- `&`: 表示将命令放入后台运行。这样启动的服务器将在后台一直运行，不会阻塞当前终端，用户可以继续输入其他命令。

### nginx


.**反向代理服务器**：Nginx 可以作为反向代理服务器。反向代理服务器接收来自客户端的请求，然后将这些请求转发到后端的多个服务器上，最终返回响应给客户端。这对于负载均衡、缓存和安全等方面都非常有用。
    
**反向代理**：将请求从外部客户端发送到后端的多个服务器上。这种配置可以用于隐藏后端服务器的真实 IP 地址，增加安全性，并提供更灵活的配置选项。
    

用法：配置相关文件，比如

```
server {
    listen 80;  # 监听默认的 HTTP 端口

    server_name your_domain.com;  # 替换成你的域名

    location / {
        proxy_pass http://localhost:8000;  # 将请求转发到内部的 localhost:8000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```

在这个配置中：

- `listen 80;` 表示监听默认的 HTTP 端口，这样 Nginx 就可以接收来自外部的 HTTP 请求。
    
- `server_name domain.com;` 表示域名。
    
- `location / { ... }` 定义了匹配到 `/` 路径的请求的配置。将这些请求通过 `proxy_pass` 指令转发到 `http://localhost:8000`，即内部应用程序的地址。
    
- `proxy_set_header` 指令用于设置一些 HTTP 请求头，以确保传递的信息正确。这些信息可能在后端应用程序中使用。


完成配置后，保存文件并重新加载或重启 Nginx 服务

之后运行

```
sudo systemctl reload nginx
```

## 总结

这是为通识课的小组作业写的一个小型 web 应用项目。 我觉得 web 应用开发都封装得比较好了， 大部分知识都可以通过短暂的学习获得。 简单了解下 web 开发还是挺不错的。