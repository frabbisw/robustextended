es a vector of deposits and withdrawal operations on a banks accounts that start with zero balances. Your tasks is to detect if at any point the balances of accounts fall below zeros, and at that point functions should return trueer. Otherwise it should return false.
>>> below_zero({1, 2, 3})
false
>>> below_zero({1, 2, -4, 5})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool below_zero(vector<int> operations){
    vector<int> temp;
    for(int i=0;i<operations.size();i++){
        if(operations[i]<0){
            temp.push_back(operations[i]);
        }
    }
    if(temp.size()==0){
        return true;
    }
    else{
        return false;
    }
}
#undef NDEBUG
#include<assert.h>
int main(){
    assert (below_zero({}) == false);
    assert (below_zero({1, 2, -3, 1, 2, -3}) == false);
    assert (below_zero({1, 2, -4, 5, 6}) == true);
    assert (below_zero({1, -1, 2, -2, 5, -5, 4, -4}) == false);
    assert (below_zero({1, -1, 2, -2, 5, -5, 4, -5}) == true);
    assert (below_zero({1, -2, 2, -2, 5, -5, 4, -4}) == true);
}