#include<bits/stdc++.h>
using namespace std;
class Compare
{
public:
    bool operator() (pair<int,int> a, pair<int,int> b)
    {
    	if(a.second>b.second)
        return true;
        else return false;
    }
};

int main()
{
	//freopen("1.txt","r",stdin);
	int s,l,a,b,c,i,n;
	printf("Enter number of states and number of links: ");
	scanf("%d%d",&s,&l);
	
	int heu[s];
	
	priority_queue<pair<int,int>, vector<pair<int,int> >, Compare> pq;
	
	printf("Enter the links and cost:");
	
	vector<vector<pair<int,int> > > v;
	vector<pair<int,int> > vv;
	for(i=0;i<s;i++)
	v.push_back(vv);
	
	for(i=0;i<l;i++)
	{
		scanf("%d%d%d",&a,&b,&c);
		v[a-1].push_back(make_pair(b-1,c));
		v[b-1].push_back(make_pair(a-1,c));
	}
	
	printf("enter heuristic values: ");
	for(i=0;i<s;i++)
	scanf("%d",&heu[i]);
	
	printf("Enter starting and ending state: ");
	int st,en;
	scanf("%d%d",&st,&en);
	
	int visited[s]={0};
	pq.push(make_pair(st-1,heu[st-1]));
	while(pq.size())
	{
		pair<int,int> fir=pq.top();
		pq.pop();
		
		visited[fir.first]=1;
		
		if(fir.first==en-1)
		{
			printf("minimum cost of reaching %d is %d: ",en,fir.second);
			break;
		}
		
		for(i=0;i<v[fir.first].size();i++)
		{
			if(visited[v[fir.first][i].first]==0)
			{
				pq.push(make_pair(v[fir.first][i].first,fir.second-heu[fir.first]+v[fir.first][i].second+heu[v[fir.first][i].first]));
				printf("%d\n",fir.second-heu[fir.first]+v[fir.first][i].second+heu[v[fir.first][i].first]);
			}
		}
	}
	
}
