#include <iostream>
using namespace std;

int main(void) {

	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int a, b, v;
	cin >> a >> b >> v;
	//int res = 0;
	int day = 0;

	/*while (res < v) { // �ݺ������� ���� �� ������ ���� �Ұ���
		res += a;
		if (res < v) {
			res -= b;
			day++;
		}
	}*/
	
	// ���� �ľ� �� ����

	// v-b : �����ϴ� �� �̲������� �ʴ´�
	// a-b : �Ϸ翡 �� �� �ִ� ����

	if ((v - b) % (a - b) == 0) { // ���� ���� ���̿� �� ���� ���
		day = (v - b) / (a - b);
	}
	else { // ���� ���� ���̺��� ���� �ö� �� ���� ���
		day = (v - b) / (a - b) + 1;
	}

	cout << day;
}