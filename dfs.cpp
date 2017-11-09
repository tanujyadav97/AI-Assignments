//----------------TANUJ YADAV---------------------------------------------------
//                                                                            --
//    DFS gives infinite loop in this application, so its better to use BFS   --
//                                                                            --
//------------------------------------------------------------------------------

#include<bits/stdc++.h>
using namespace std;

int a,b;

vector<pair<int,int> > findstates(pair<int,int> aa)                // finds the possible states
{
	vector<pair<int,int> > v;
	if(aa.first!=0)
	v.push_back(make_pair(0,aa.second));
	if(aa.second!=0)
	v.push_back(make_pair(aa.first,0));
	if(aa.first!=a)
	v.push_back(make_pair(a,aa.second));
	if(aa.second!=b)
	v.push_back(make_pair(aa.first,b));
	if(aa.first!=max(0,aa.first-(b-aa.second))&&aa.second!=min(b,aa.second+aa.first))
	v.push_back(make_pair(max(0,aa.first-(b-aa.second)),min(b,aa.second+aa.first)));
	if(aa.first!=min(a,aa.second+aa.first)&&aa.second!=max(0,aa.second-(a-aa.first)))
	v.push_back(make_pair(min(a,aa.second+aa.first),max(0,aa.second-(a-aa.first))));
	
	return v;
}

int w=0;
void dfs(int t1,int t2,pair<int,int> cs)
{
	w++;
			
	if((cs.first==t1)&&(cs.second==t2))
	{
		cout<<cs.first<<" "<<cs.second<<" found after checking "<<w<<" states.";
		return;
	}
	
	vector<pair<int,int> > states=findstates(make_pair(cs.first,cs.second));
	for(int i=0;i<states.size();i++)
	{
	  dfs(t1,t2,states[i]);  	
	}
	
}

int main()
{
	int t1,t2;
	cout<<"Enter the capacity of the jugs: ";
	cin>>a>>b;
	cout<<"Enter the target volumes: ";
	cin>>t1>>t2;
	
	dfs(t1,t2,make_pair(0,0));
}
