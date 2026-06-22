//Using recursion
class Solution {
public:
int binary(vector<int>&arr,int start,int end,int target){
    if (start>end){
        return -1;
    }
    int mid=start+(end-start)/2;
    if (arr[mid] == target){
        return mid;
    }
    else if (arr[mid]>target){
        return binary(arr,start,mid-1,target);
    }
    else{
        return binary(arr,mid+1,end,target);
    }
}
    int search(vector<int>& nums, int target) {
        int start=0,end=nums.size()-1;
        return binary(nums,start,end,target);
    }
};