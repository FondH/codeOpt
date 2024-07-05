"""
应用程序路由总结及功能介绍

1. Overview Blueprint

- Blueprint: overview_blueprint

- 路由:
  - `/api/submit_overview`
    - 方法: GET
    - 功能: 提交并获取过去7天的提交数据概览。
    - 要求: 需要 JWT 认证。
    - 返回: 包含提交日期的标签和数据，以及总提交数。

  - `/api/submit_recent`
    - 方法: GET
    - 功能: 获取最近15天的提交记录。
    - 要求: 需要 JWT 认证。
    - 返回: 最近提交记录列表，最多返回最近10条记录。

  - `/api/view-report/<task_id>`
    - 方法: GET
    - 功能: 查看特定任务的报告。
    - 要求: 需要 JWT 认证。
    - 返回: 任务报告数据。

2. Auth Blueprint

- Blueprint: auth_blueprint

- 路由:
  - `/api/register`
    - 方法: POST
    - 功能: 注册新用户。
    - 要求: 提供用户名、邮箱和密码。
    - 返回: 注册成功或失败的消息。

  - `/api/login2`
    - 方法: POST
    - 功能: 用户登录。
    - 要求: 提供用户名和密码。
    - 返回: 用户信息和访问令牌。

  - `/updateUserinfo`
    - 方法: POST
    - 功能: 更新用户信息。
    - 要求: 提供用户名和需要更新的信息。
    - 返回: 更新成功或失败的消息。

  - `/profile`
    - 方法: GET, POST
    - 功能: 获取用户的个人信息。
    - 要求: 需要 JWT 认证。
    - 返回: 用户个人信息。

3. Task Blueprint

- Blueprint: task_blueprint

- 路由:
  - `/api/submit-code`
    - 方法: POST
    - 功能: 提交代码进行检测。
    - 要求: 提供用户ID、文件及相关信息。
    - 返回: 任务创建成功或失败的消息。

  - `/api/task-status/<task_id>`
    - 方法: GET
    - 功能: 获取特定任务的状态。
    - 要求: 提供任务ID。
    - 返回: 任务状态信息。

  - `/api/tasks/<task_id>/cancel`
    - 方法: POST
    - 功能: 取消特定任务。
    - 要求: 提供任务ID。
    - 返回: 任务取消成功的消息。

  - `/api/tasks/<task_id>/details`
    - 方法: GET
    - 功能: 获取特定任务的详细信息。
    - 要求: 提供任务ID。
    - 返回: 任务详细信息。

  - `/api/task_table`
    - 方法: GET
    - 功能: 获取用户的所有任务及其结果。
    - 要求: 需要 JWT 认证。
    - 返回: 用户的任务列表及结果。

  - `/api/available-models`
    - 方法: GET
    - 功能: 获取可用模型列表。
    - 要求: 无。
    - 返回: 模型列表。

4. Admin Blueprint

- Blueprint: admin_blueprint

- 路由:
  - `/getusers`
    - 方法: GET
    - 功能: 获取所有用户信息。
    - 要求: 无。
    - 返回: 用户信息列表。

  - `/getdetections`
    - 方法: GET
    - 功能: 获取所有检测信息。
    - 要求: 无。
    - 返回: 检测信息列表。

  - `/gettasks`
    - 方法: GET
    - 功能: 获取所有任务信息。
    - 要求: 无。
    - 返回: 任务信息列表。

  - `/proc/<task_id>`
    - 方法: GET
    - 功能: 处理特定任务。
    - 要求: 提供任务ID。
    - 返回: 无。
"""

# 你的其他 app.py 内容在这里
from api import app

if __name__ == '__main__':
    # rs = detect('G:\\My_Projects\\codeopt\\api\\files\\Tencent.txt', 'c',1)
    # print(rs)
    if __name__ == '__main__':
        app.run(
            host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG']
        )