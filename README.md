# 视觉语言模型水印保护系统（前端原型）

## 运行方法

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动后端（仅用于前端静态页面展示）：
   ```bash
   python app.py
   ```
3. 浏览器访问：http://localhost:5000

4. 界面展示

- 登录
  ![示例图片](image/图文溯源_登录.png)
- 注册
  ![示例图片](image/图文溯源_注册.png)
- 使用 VLM 进行 Q&A
  ![示例图片](image/图文溯源_模型服务.png)
- 水印验证（针对推理阶段）
  ![示例图片](image/图文溯源_模型保护.png)
- 水印验证（针对模型）
  ![示例图片](image/图文溯源_内容保护.png)
