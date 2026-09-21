# CyberChef Launcher

一个用于启动 CyberChef 本地离线版的 Python 脚本。
零第三方依赖，单文件即可运行。

## 功能

| 功能 | 说明 |
|------|------|
| 端口自适应 | 依次尝试 8000 / 5500 / 8080 / 8888 / 3000，首个能成功启动 HTTP 服务的端口即被采用 |
| 仅本地回环 | 强制绑定 `127.0.0.1`，避免局域网意外暴露 |
| 错误提示 | HTML 缺失、端口全占用、服务启动失败等通过弹窗提示（Windows `MessageBoxW`，非 Windows 回退 stderr） |
| 自动打开浏览器 | 服务启动后自动访问 CyberChef 离线页面 |

## 目录结构

将脚本放置于`CyberChef`根目录下，与`CyberChef_v11.4.0.html`同级：

```
CyberChef/
├── CyberChef_launcher.py / CyberChef_launcher.exe    ← 本脚本
└── CyberChef_v11.4.0.html   ← CyberChef 离线版 HTML 文件（自行下载，不随仓库分发）
```


## 使用方法

1. 直接从 [Releases](https://github.com/Thyme-13/CyberChef_launcher/releases) 下载 `CyberChef_launcher.exe`。

2. 使用源码运行：

```cmd
python CyberChef_launcher.py
```

启动后自动打开浏览器访问 `http://127.0.0.1:<端口>/CyberChef_v11.4.0.html`。

### 无窗口运行（Windows）

- 将文件后缀改为 `.pyw`（使用 `pythonw.exe` 运行，无控制台）；
- 或直接使用 Releases 中的 exe（已按无窗口方式打包）。


## 配置自定义

修改模块顶部常量：

```python
HTML_NAME = 'CyberChef_v11.4.0.html'
PORTS = (8000, 5500, 8080, 8888, 3000)
BIND_ADDR = '127.0.0.1'
```

## 兼容性

- 目标环境：Windows / macOS / Linux，Python 3.8+
- 依赖：仅标准库（`os`、`sys`、`subprocess`、`time`、`webbrowser`，Windows 下另用 `ctypes`）

## 许可

[MIT](LICENSE)
