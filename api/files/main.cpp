#include<iostream>

using namespace std;
int main() {

    int N = 2, M = 1, K = 2;
    cin >> N >> M >> K;
    int price[N][K];
    int t;
    for (int i = 0;i < N;i++) {
        for (int j = 0;j < K;j++) {
            cin >> t;
            price[i][j] = t;

        }
    }

    int total = 0;
    int a, b;
    for (int i = 0;i < M;i++) {
        int min = 1000000;
        cin >> a >> b;
        for (int j = 0;j < K;j++) {
            for (int p = 0;p < K;p++)
            {
                cin >> t;
                min = min < price[a][j] + price[b][p] + t ? min : price[a][j] + price[b][p] + t;
            }
        }
        total += min;
    }

    cout << total << endl;
    return 1;
}