#include<iostream>
#include<cstring>
#include<cstdio>
#include <iomanip>
#include <sstream>

using namespace std;

class stack {
	int top = -1;
	int max = 5;

	int* val;
public:
	stack(const int m) : max(m) {
		val = new int[max];

	}

	void push(const int a) { val[++top] = a; };
	int pop() { return val[top--]; }

	int empty() { return top == -1; }
	int get() { return val[top]; }
	string out() {
		stringstream ss;
		for (int i = 0;i <= top;i++)
			ss << (val[i]) << ' ';
		return ss.str();
	}
};

int Solution() {

	int n = 1;
	cin >> n;
	cin.ignore();
	string s;
	char buffer[8];
	for (int p = 0;p < n;p++)
	{
		cin.getline(buffer, 8);
		//9+3+4x3

		stack opStack(3);
		stack nStack(4);

		for (int i = 0;i < 7;i++) {
			//cout << "i"<<endl;
			if ('0' < buffer[i] && buffer[i] <= '9') {

				nStack.push(buffer[i] - '0');
				//cout << "num:" << nStack.out() << endl;
				//cout << "opStack:" << opStack.out() << endl;


			}
			else {

				if (buffer[i] == 'x' || buffer[i] == '/') {
					int t = nStack.pop();

					if (buffer[i] == 'x')
						nStack.push(t * (buffer[i + 1] - '0'));
					else
						nStack.push(t / (buffer[i + 1] - '0'));

					i++;
				}
				else {// + - ÔËËã
					if (opStack.get() == '+' || opStack.get() == '-') {
						int a = nStack.pop();
						int b = nStack.pop();

						if (opStack.get() == '+') {
							nStack.push(b + a);
						}
						else {
							nStack.push(b - a);
						}

						opStack.pop();
						opStack.push(buffer[i]);
					}
					else {
						opStack.push(buffer[i]);
					}
				}

				//cout << "num:" << nStack.out() << endl;
				//cout << "opStack:" << opStack.out() << endl;
			}
		}
		if (!opStack.empty()) {
			int a = nStack.pop();
			int b = nStack.pop();
			if (opStack.get() == '+') {
				nStack.push(b + a);
			}
			else {
				nStack.push(b - a);
			}
		}

		string s = (nStack.get() == 24) ? "Yes" : "No";
		cout << s << endl;
	}
	return 1;
}