# 课程结课作业 - 可视化代码审查工具

## 项目简介

本项目是一个集成多个代码审计工具的可视化代码审查工具，使用技术栈包括 Vue 3、一个 UI 库（脚手架见[Vue Argon Dashboard 2](http://demos.creative-tim.com/vue-argon-dashboard/?ref=readme-vad) ）、Flask 和 SQLite / MySQL。



### 功能特性

- 通过 web 端提交程序
- 配置用户个人需要的审计策略（如审计项目、LLM 总结、检测力度等策略的组合）
- 生成审计报告供用户参考、修改
- 通过 web 查看近期用户使用频率、历史记录等



## 项目部署

### 手动部署

>Flask 默认运行在本地 10262 
>
>Vue3 默认运行在本地 10265
>
>Mysql(若启用) 默认运行在 3306

#### 后端部署

1. 克隆后端代码仓库到本地：
    ```bash
    git clone <后端仓库URL>
    ```

2. 进入后端目录：
    ```bash
    cd api
    ```

3. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

4. 运行后端程序：
    ```bash
    python app.py
    ```

#### 前端部署

1. 克隆前端代码仓库到本地：
    ```bash
    git clone <前端仓库URL>
    ```

2. 进入前端目录：
    ```bash
    cd CodeOptUI
    ```

3. 安装依赖：
    ```bash
    npm install
    ```

4. 调试前端程序：
    ```bash
    npm run serve
    ```

5. 构建前端程序：
    ```bash
    npm run build
    ```

6. 其他脚本：
    - 代码检查：
        ```bash
        npm run lint
        ```
    - 代码格式化：
        ```bash
        npm run prettify
        ```

### Docker 镜像部署

> **注意：** 该部分部署尚未完成。

## 项目功能和界面展示

（此部分请根据项目的具体功能和界面截图进行补充）

1. **功能一：**

    - 用户认证：用户登录后凭借服务器提供的jwt访问服务器资源，以保证用户身份的合法

    ![image-20240705170031487](/img/image-20240705170031487.png)

2. **功能二：**
    - 代码提交、后台轮询任务并检测
    - ![image-20240705170315646](/img/image-20240705170315646.png)

3. **功能三：**

    - 代码报告生成
    - ![image-20240705170619541](/img/image-20240705170619541.png)

4. **功能四**

    - 历史提交记录查看
    - ![image-20240705170426016](/img/image-20240705170426016.png)

5. **功能五**

    - 近期提交数据overview
    - ![image-20240705170721090](/img/image-20240705170721090.png)

6. 定制个性化检测策略、大模型参数

    - 设置策略组合

    ![image-20240705170837939](/img/image-20240705170837939.png)

    - （optional）若大模型可用...

    ![image-20240705170804803](/img/image-20240705170804803.png)

    

## 许可协议

