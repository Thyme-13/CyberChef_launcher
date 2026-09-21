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

脚本所在目录放置 CyberChef 离线 HTML 文件：

```
CyberChef_launcher/
├── CyberChef_launcher.py    ← 本脚本
└── CyberChef_v11.4.0.html   ← CyberChef 离线版 HTML 文件（自行下载，不随仓库分发）
```

> `CyberChef_v11.4.0.html` 是 CyberChef 离线版产物（GCHQ 开源，Apache-2.0），体积较大且属第三方代码，建议从 [CyberChef 官方仓库](https://github.com/gchq/CyberChef) 构建后自行放置，不提交到本仓库。

## 使用方法

不想安装 Python 的话，可直接从 [Releases](https://github.com/你的用户名/CyberChef_launcher/releases) 下载打包好的 `CyberChef_launcher.exe`，双击即用，无需任何环境。exe 为 PyInstaller 单文件产物，随版本发布，不保存在源码仓库中。

使用源码运行：

```cmd
python CyberChef_launcher.py
```

启动后自动打开浏览器访问 `http://127.0.0.1:<端口>/CyberChef_v11.4.0.html`。

### 无窗口运行（Windows）

双击 `.py` 会短暂显示控制台窗口。需要完全无窗口时：

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
