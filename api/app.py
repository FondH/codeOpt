"""
Ӧ�ó���·���ܽἰ���ܽ���

1. Overview Blueprint

- Blueprint: overview_blueprint

- ·��:
  - `/api/submit_overview`
    - ����: GET
    - ����: �ύ����ȡ��ȥ7����ύ���ݸ�����
    - Ҫ��: ��Ҫ JWT ��֤��
    - ����: �����ύ���ڵı�ǩ�����ݣ��Լ����ύ����

  - `/api/submit_recent`
    - ����: GET
    - ����: ��ȡ���15����ύ��¼��
    - Ҫ��: ��Ҫ JWT ��֤��
    - ����: ����ύ��¼�б���෵�����10����¼��

  - `/api/view-report/<task_id>`
    - ����: GET
    - ����: �鿴�ض�����ı��档
    - Ҫ��: ��Ҫ JWT ��֤��
    - ����: ���񱨸����ݡ�

2. Auth Blueprint

- Blueprint: auth_blueprint

- ·��:
  - `/api/register`
    - ����: POST
    - ����: ע�����û���
    - Ҫ��: �ṩ�û�������������롣
    - ����: ע��ɹ���ʧ�ܵ���Ϣ��

  - `/api/login2`
    - ����: POST
    - ����: �û���¼��
    - Ҫ��: �ṩ�û��������롣
    - ����: �û���Ϣ�ͷ������ơ�

  - `/updateUserinfo`
    - ����: POST
    - ����: �����û���Ϣ��
    - Ҫ��: �ṩ�û�������Ҫ���µ���Ϣ��
    - ����: ���³ɹ���ʧ�ܵ���Ϣ��

  - `/profile`
    - ����: GET, POST
    - ����: ��ȡ�û��ĸ�����Ϣ��
    - Ҫ��: ��Ҫ JWT ��֤��
    - ����: �û�������Ϣ��

3. Task Blueprint

- Blueprint: task_blueprint

- ·��:
  - `/api/submit-code`
    - ����: POST
    - ����: �ύ������м�⡣
    - Ҫ��: �ṩ�û�ID���ļ��������Ϣ��
    - ����: ���񴴽��ɹ���ʧ�ܵ���Ϣ��

  - `/api/task-status/<task_id>`
    - ����: GET
    - ����: ��ȡ�ض������״̬��
    - Ҫ��: �ṩ����ID��
    - ����: ����״̬��Ϣ��

  - `/api/tasks/<task_id>/cancel`
    - ����: POST
    - ����: ȡ���ض�����
    - Ҫ��: �ṩ����ID��
    - ����: ����ȡ���ɹ�����Ϣ��

  - `/api/tasks/<task_id>/details`
    - ����: GET
    - ����: ��ȡ�ض��������ϸ��Ϣ��
    - Ҫ��: �ṩ����ID��
    - ����: ������ϸ��Ϣ��

  - `/api/task_table`
    - ����: GET
    - ����: ��ȡ�û�����������������
    - Ҫ��: ��Ҫ JWT ��֤��
    - ����: �û��������б������

  - `/api/available-models`
    - ����: GET
    - ����: ��ȡ����ģ���б�
    - Ҫ��: �ޡ�
    - ����: ģ���б�

4. Admin Blueprint

- Blueprint: admin_blueprint

- ·��:
  - `/getusers`
    - ����: GET
    - ����: ��ȡ�����û���Ϣ��
    - Ҫ��: �ޡ�
    - ����: �û���Ϣ�б�

  - `/getdetections`
    - ����: GET
    - ����: ��ȡ���м����Ϣ��
    - Ҫ��: �ޡ�
    - ����: �����Ϣ�б�

  - `/gettasks`
    - ����: GET
    - ����: ��ȡ����������Ϣ��
    - Ҫ��: �ޡ�
    - ����: ������Ϣ�б�

  - `/proc/<task_id>`
    - ����: GET
    - ����: �����ض�����
    - Ҫ��: �ṩ����ID��
    - ����: �ޡ�
"""

# ������� app.py ����������
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