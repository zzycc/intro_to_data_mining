#include <bits/stdc++.h>
using namespace std;
int main(){
	cin.sync_with_stdio(false);
	cin.tie(NULL);
	int min_sup;
	vector<string> dataset;
	string tmp;
	cin >> min_sup;
	while(getline(cin,tmp))
		dataset.push_back(tmp);

	map<string, int> F[dataset.size()];
	map<string, int>:: iterator it,it1,it2;
	map<string, int> answer;
	map<string, int> C[dataset.size()];
	for(int i=0;i<dataset.size();i++){
		stringstream line(dataset[i]);
		while(getline(line,tmp,' '))
			F[0][tmp]++;
	}
	for(it=F[0].begin();it!=F[0].end();it++){
		if(it->second < min_sup){
			F[0].erase(it->first);
			it=F[0].begin();
		}
	}
	int k = 0;
	while(F[k].size()!=0){
		for(it=F[0].begin();it!=F[0].end();it++){
			for(it1=it+1;it1!=F[0].end();it1++){
				stringstream line1(it->first),line2(it1->first);
				map<string, int> jointset;
				while(getline(line1,tmp,' '))
					jointset[tmp]++;
				while(getline(line2,tmp,' '))
					jointset[tmp]++;
				if(jointset.size()==k+2){
					tmp.assign("");
					for(it2=jointset.begin();it2!=jointset.end();it2++){
						tmp+=it2->first;
						tmp+=" ";
					}
					C[k+1][tmp.substr(0,tmp.size()-1)]++;
				}
			}
		}
		//F[k+1]
		k++;
	}
}