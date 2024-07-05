

#include <iostream>
#include<vector>
using namespace std;


vector<vector<int>> quick_sort(vector<vector<int>> nums, int st, int ed) {
    if (ed-st < 1)
        return nums;

    int l = st, r = ed;
    vector<int>mid = nums[l];
    while (l < r) {

        while (r > l && nums[r][0] >= mid[0])
            r--;

        nums[l] = nums[r];

        while (l<r && nums[l][0] <= mid[0])
            l++;

        nums[r] = nums[l];
        
    }
    nums[l] = mid;

    nums = quick_sort(nums, st, l-1);
    nums = quick_sort(nums, l+1, ed);
    return nums;
}


int* merge_sort(int * nums, int st, int ed) {
    if (ed == st)
        return new int(nums[st]);


    int mid = (st + ed) / 2;
    int* part = merge_sort(nums, st, mid);
    int* part_ = merge_sort(nums, mid+1, ed);

    int* merged = new int[ed - st + 1] {0};
    int i, l=0, r=0;
    for (i = 0;i <= (ed - st);i++) {
        if (l > mid - st) {
            memcpy(merged + i, part_ + r, sizeof(int) * (ed - i + 1));
            break;
        }
        if (r > ed - (mid + 1)) {
            memcpy(merged + i, part + l, sizeof(int) * (ed - i + 1));
            break;
        }

        merged[i] = part[l] <  part_[r] ? part[l++] : part_[r++];
        
    }

    delete[] part;
    delete[] part_;

    return merged;

}

void _swap(int* a, int* b) {
    int c = *a;
    *a = *b;
    *b = c;
};

int * buble_sort(int * nums, int l) {
    for (int i = 0;i < l;i++) {
        for (int j = 0; j < l-i-1;j++) {
            if (nums[j] > nums[j+1])
                _swap(nums+j, nums+j+1);
            
        }
    
    }
    return nums;
}

int lengthOfLIS(vector<int> nums) {
    int dp[100];
    dp[0] = 1;
    int max = 1;
    for (int i = 1;i < nums.size();i++) {
        int tp = 1, t = nums[i];

        for (int j = 0;j < i;j++)
            if(t > nums[j])
                tp = tp > dp[j] ? tp: dp[j]+1;
        dp[i] = tp;
        max = max > dp[i] ? max : dp[i];
    }


    return max;
}
void pr(int* a, int l) {
    for (int i = 0;i < l;i++)
        cout <<*(a+i)<<" ";
    cout << endl;
}
/*
int main() {
    int* a = new int[10]{10, 2, 4, 21, 23, 2, 31, 12, 9, 8};
    pr(a, 10);
    int* p = buble_sort(a, 10);
    pr(p, 10);
    
    vector<int> a = {0,1,0,3,2,3};
    lengthOfLIS(a);

}
*/
