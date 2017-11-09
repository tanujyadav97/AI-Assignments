#include<bits/stdc++.h>
using namespace std;
int main()
{
	//freopen("1.txt","r",stdin);
	int i,j,f,v,k,p;
	cout<<"Enter the number of features and data values: ";
	cin>>f>>v;
	
	int d[v][f];
	
	cout<<"Enter the feature values in integer format:\n";
	
	for(i=0;i<v;i++)
	for(j=0;j<f;j++)
	cin>>d[i][j];
	
	int label[v];
	
	cout<<"Enter the labels(integer): \n";
	
	vector<int> pl;
	
	for(i=0;i<v;i++)
	{
		cin>>label[i];
		if(find(pl.begin(), pl.end(), label[i]) == pl.end())
		pl.push_back(label[i]);
	}
	bool test[v]={0};
	
	srand(time(NULL));
	
	int c=v/3;
	while(c)
	{
	  int f=rand()%v;
	  if(test[f]==0)
	   {
	  	test[f]=1;
	  	c--;
		}	
	}
	
	int freq[pl.size()]={0};
	
	for(i=0;i<v;i++)
	{
		if(test[i]==0)
		{
			vector<int>::iterator loc=find(pl.begin(),pl.end(),label[i]);
			if(loc!=pl.end())
			freq[*loc]++;
		}
	}
	
	for(i=0;i<v;i++)
	{
		if(test[i]==1)
		{
			cout<<"Prediction for [";
			for(j=0;j<f;j++)
			cout<<d[i][j]<<" ";
			cout<<"] :";
			
			float maxx=0;int maxi;
			
			for(p=0;p<pl.size();p++)
			{
				float pro=1;
				for(j=0;j<f;j++)
				{
					int cc=0;
					for(k=0;k<v;k++)
					{
						if(test[k]==0)
						{
							if((d[k][j]==d[i][j])&&(label[k]==pl[p]))
							cc++;
						}
					}
					
					pro*=float(cc)/freq[p];
				    	
				}
				if(pro>maxx)
				{
					maxx=pro;
					maxi=p;		
				}
			}
			
			cout<<pl[maxi]<<endl;
		}
	}
	
}
