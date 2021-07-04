#include <iostream>
using namespace std;

int main(void) {

	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int a, b, v;
	cin >> a >> b >> v;
	//int res = 0;
	int day = 0;

	/*while (res < v) { // 반복문으로 했을 때 빠르게 진행 불가능
		res += a;
		if (res < v) {
			res -= b;
			day++;
		}
	}*/
	
	// 원리 파악 후 진행

	// v-b : 도착하는 날 미끄러지지 않는다
	// a-b : 하루에 갈 수 있는 높이

	if ((v - b) % (a - b) == 0) { // 나무 막대 높이에 딱 맞출 경우
		day = (v - b) / (a - b);
	}
	else { // 나무 막대 높이보다 높게 올라갈 수 있을 경우
		day = (v - b) / (a - b) + 1;
	}

	cout << day;
}