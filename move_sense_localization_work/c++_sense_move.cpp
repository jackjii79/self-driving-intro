#include <iostream>
#include <vector>
#include <string>

using namespace std;

float pHit = 0.6, pMiss = 0.2, pExact = 0.8, pOvershoot = 0.1, pUndershoot = 0.1;
vector<string> world = {"green", "red", "red", "green", "green"};

vector <float> sense(vector<float> p, string Z);
vector <float> move(vector<float> p, int step);

int main() {
 vector<float> P (5, 0.2), motions (2, 1);
 vector<string> measurements = {"red", "green"};
 for(int k=0;k < measurements.size();k++) {
  P = sense(P, measurements[k]);
  P = move(P, motions[k]);
 }
 for(int k=0;k < P.size();k++)
  cout << P[k] << " ";
 cout << endl;
 return 0;
}

vector <float> sense(vector<float> p, string Z) {
 vector<float> newvector (p.size(), 0);
 float sum = 0;
 for(int k=0;k < p.size();k++) {
  if (Z == world[k])
   newvector[k] = p[k] * pHit;
  else
   newvector[k] = p[k] * pMiss;
  sum += newvector[k];
 }
 for(int k=0;k < p.size();k++) 
  newvector[k] /= sum;
 return newvector;
}

vector <float> move(vector<float> p, int step) {
 vector<float> newvector (p.size(), 0);
 for (int k=0;k < p.size();k++) {
  int id1 = (k-step)%(int)p.size(), id2 = (k-step-1)%(int)p.size(), id3 = (k-step+1)%(int)p.size();
  newvector[k] += pExact * p[id1];
  newvector[k] += pOvershoot * p[id2];
  newvector[k] += pUndershoot * p[id3];
 }
 return newvector;
}
