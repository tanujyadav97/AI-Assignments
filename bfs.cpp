//----------------TANUJ YADAV---------------------------------------------------
//                                                                            --
//    BFS is a good approach for this application                             --
//                                                                            --
//------------------------------------------------------------------------------


#include<bits/stdc++.h>
using namespace std;

int a,b;

vector<pair<int,int> > findstates(pair<int,int> aa)                  // finds the possible states
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

void bfs(int t1,int t2)
{
	int w=0;
	queue<pair<int,int> > que;
	que.push(make_pair(0,0));
	
	while(que.size())
	{
		pair<int,int> p=que.front();
		que.pop();
		
		vector<pair<int,int> > states=findstates(make_pair(p.first,p.second));
		for(int i=0;i<states.size();i++)
		{
			w++;
			if((states[i].first==t1)&&(states[i].second==t2))
			{
				cout<<states[i].first<<" "<<states[i].second<<" found after checking "<<w<<" states.";
				return;
			}
			
			que.push(states[i]);
		}
	}
}

int main()
{
	int t1,t2;
	cout<<"Enter the capacity of the jugs: ";
	cin>>a>>b;
	cout<<"Enter the target volumes: ";
	cin>>t1>>t2;
	
	bfs(t1,t2);
}
