# 视觉语言模型水印保护系统

## 🛡️ 系统简介

本系统为视觉语言模型（VLM）提供多模态图文水印保护解决方案，涵盖模型训练、推理、内容溯源等全过程，防止模型盗用与内容篡改，保障知识产权。

## ✨ 主要功能

- <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/lock.svg" width="18"/> **多模态水印嵌入与验证**：对模型输出内容进行水印嵌入、验证与溯源，保障原创性。
- <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/search.svg" width="18"/> **内容溯源与追踪**：支持对生成内容的溯源与追踪，提升安全性。
- <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/cogs.svg" width="18"/> **多模型管理与切换**：支持多模型的导入、切换与批量管理，灵活高效。
- <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/user-shield.svg" width="18"/> **用户权限与安全管理**：多级权限分配，安全高效的用户与角色管理。
- <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/chart-line.svg" width="18"/> **实时监控与统计分析**：提供丰富的统计报表与可视化分析，助力决策。

## 🚀 使用流程

1. <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/sign-in-alt.svg" width="16"/> 用户注册/登录系统
2. <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/cube.svg" width="16"/> 选择或导入视觉语言模型
3. <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/image.svg" width="16"/> 进行图文问答或内容生成
4. <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/stamp.svg" width="16"/> 对生成内容进行水印验证
5. <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free/svgs/solid/search.svg" width="16"/> 查看内容溯源与统计分析

## 🛠️ 运行方法

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动后端（仅用于前端静态页面展示）：
   ```bash
   python app.py
   ```
3. 浏览器访问：http://localhost:5000

## 🖼️ 界面预览

- <b>登录</b>

  ![登录](image/图文溯源_登录.png)

- <b>注册</b>

  ![注册](image/图文溯源_注册.png)

- <b>模型服务（Q&A）</b>

  ![模型服务](image/图文溯源_模型服务.png)

- <b>水印验证（推理阶段）</b>

  ![推理水印](image/图文溯源_模型保护.png)

- <b>水印验证（模型）</b>

  ![模型水印](image/图文溯源_内容保护.png)

---

> 如需技术支持或有建议，欢迎联系：1600029360@qq.com
