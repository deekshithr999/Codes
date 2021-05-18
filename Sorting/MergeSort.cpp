#include<iostream>
#include<vector>

using namespace std;


void Merge(vector<int>&vect,int left,int mid,int right)
{
    int lp=left;
    int rp=mid;
    int pointer=lp;
    vector<int>tvect(right-left+1);
    while((lp<mid) & (rp<=right))
    {
     //   cout<<" lp , mid , rp : "<<lp<<" "<<mid<<" "<<rp<<endl;
        if(vect[lp]<vect[rp])
        {
           tvect[pointer]=vect[lp];
           lp++;
        }
        else if(vect[lp]>vect[rp])
        {
            tvect[pointer]=vect[rp];
            rp++;
        }
        pointer++;
        

    }
    while(lp<mid)
    {
        tvect[pointer]=vect[lp];
        pointer++;
        lp++;
    }
    while(rp<=right)
    {
        tvect[pointer]=vect[rp];
        pointer++;
        rp++;
    }

    for(int i=left;i<=right;i++)
    {
        vect[i]=tvect[i];

    }


}

void MergeSort(vector<int>&vect,int left,int right)
{
    int sze=(right-left+1);
    int midi=left+sze/2;
   // cout<<"size :"<<sze<<endl;  
    if(sze>1)
    {
        
        MergeSort(vect,left,midi-1); //NOTICE how the middle element is considered
        MergeSort(vect,midi,right);

    }
    Merge(vect,left,midi,right);
}



int main()
{
    int n;
    cin>>n;
    vector<int>vect;
    vect.reserve(n);
    int temp;
    for(int i=0;i<n;i++)
    {

        cin>>temp;
        vect.push_back(temp);
    }
  //  cout<<"vect size :"<<vect.size()<<endl;
   
    vector<int>res_vect(n);
     MergeSort(vect,0,n-1);

     cout<<"sorted :"<<endl;

     for(int i=0;i<n;i++)
     {
         cout<<vect[i]<<" ";
     }
     cout<<endl;
    

}