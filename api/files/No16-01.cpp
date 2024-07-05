#include<iostream>
#include<cstring>
#include<cstdio>
#include <iomanip>
using namespace std;
int solution() {
	int n;
	cin >> n;

	int middle_l, middle_r;
	if (n & 1)
		middle_l = n / 2 + 1;
	else {
		middle_l = n / 2;
		middle_r = n / 2 + 1;

	}

	int min = 0x7fffffff, max = 0x80000000;
	int middle_val = 0;
	int a, b;



	for (int i = 1;i <= n;i++) {
		cin >> a;
		min = a < min ? a : min;
		max = a > max ? a : max;
		if (i == n / 2 + 1) {
			middle_val += a;
		}
		else if (i == n / 2 && !(n & 1)) {
			middle_val += a;
		}

	}


	cout << max << " ";
	if (!(n & 1) && (middle_val & 1)) {
		printf("%.1f", (double(middle_val) / 2));

	}
	else
		cout << middle_val / 2;
	cout << " " << min;
	return 1;
}