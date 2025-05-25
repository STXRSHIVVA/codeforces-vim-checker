  #include<bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i <n; i++) {
        cin >> a[i];
    }

    sort(a.begin(),a.end());

    int ct1 = 0,ct2 = 0,i=0,j=n-1;
    while( (a[i] + a[j]) % 2 != 0){
      j--;
      ct2++;
    }
    j = n-1;
    while( (a[i] + a[j]) % 2 != 0){
      i++;
      ct1++;
    }

    int ans = min(ct1,ct2);

    cout << ans + 1 << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
