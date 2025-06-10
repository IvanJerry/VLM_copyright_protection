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

4. 管理员界面

- 登录
  ![示例图片](image/login.png)
- 注册
  ![示例图片](image/register.png)
- 使用 VLM 进行 Q&A
  ![示例图片](image/image1.png)
- 模型切换
  ![示例图片](image/image2.png)
- 水印验证（针对内容）
  ![示例图片](image/image3.png)
- 水印验证（针对模型）
  ![示例图片](image/image3-1.png)
- 水印设置
  ![示例图片](image/image4.png)

5. 普通用户界面

- 使用 VLM 进行 Q&A
  ![示例图片](image/multi_task_user.png)
- 模型切换
  ![示例图片](image/model_user.png)
- 设置
  ![示例图片](image/setting_user.png)

## 说明

- 目前仅为前端界面原型，后端接口未实现。
- 颜色风格采用指定的 conic-gradient 渐变。
- 结构参考需求文档，后续可根据功能完善交互和数据。
