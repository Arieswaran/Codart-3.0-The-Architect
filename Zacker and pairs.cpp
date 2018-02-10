#include<iostream>
using namespace std;
int main()
{
    unsigned long int n,i,c,j,aj;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>c;
        aj=c;
        for(j=1;j<c;j++)
        aj+=j;
        cout<<aj<<endl;
    }
}
