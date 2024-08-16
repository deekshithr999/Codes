class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> umap;

        for (auto st : arr){
            umap[st]++;
        }

        for(int i = 0; i< arr.size(); i++){
            if (umap[arr[i]] == 1) k--;
            if(!k) return arr[i];
        }
        return "";
    }
};