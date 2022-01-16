#include<iostream>

using namespace std;

int main()
{
    int A1,A2,A3,B1,B2,B3,T1,T2,T3,m,b,Q;
    cout << "num :";
    cin >> b;
    cout << "GF :";
    cin >> m;

    A1=1,A2=0,A3=m;
    B1=0,B2=1,B3=b;
    
    cout << "\n\tQ\tA1\tA2\tA3\tB1\tB2\tB3" << endl << endl;
    cout << "\t-\t" << A1 << "\t" << A2 << "\t" << A3 << "\t" << B1 << "\t" << B2 << "\t" << B3 << endl;
    while (B3 != 0 && B3 != 1)
    {
    	Q = A3 / B3;
    	T1 = A1 - Q * B1; 
    	T2 = A2 - Q * B2; 
    	T3 = A3 - Q * B3;
    	A1 = B1, A2 = B2, A3 = B3;
    	B1 = T1, B2 = T2, B3 = T3;
        cout << "\t" << Q << "\t" << A1 << "\t" << A2 << "\t" << A3 << "\t" << B1 << "\t" << B2 << "\t" << B3 << endl;
	}
	if(B2<0)
	cout << "\n\tinverse :" << B2+m;
}
