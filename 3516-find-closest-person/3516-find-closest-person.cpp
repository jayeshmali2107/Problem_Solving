class Solution {
public:
    int findClosest(int x, int y, int z) {
        int difference1 = abs(z-x);
        int difference2 = abs(z-y);
        if(difference1<difference2){
            return 1;
        }
        else if(difference1>difference2){
            return 2;
        }
        else{
            return 0;
        }
    }
};