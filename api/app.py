
from api import app

from detect import detect

if __name__ == '__main__':
    # rs = detect('G:\\My_Projects\\codeopt\\api\\files\\Tencent.txt', 'c',1)
    # print(rs)
    app.run("0.0.0.0", port=10262, debug=True)