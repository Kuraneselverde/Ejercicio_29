#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;

int main()
{
  int nx=101;
  int nt=200;
  double dx=0.01;
  double dt=0.5;
  double ro=0.01;
  double cg=dx/dt;
  double ten=0.000003; 
  double c=sqrt(ten/ro);
  double dez[3][nx];
    
  ofstream outfile;
 
  ifstream infile; 
  string line;
  infile.open("dcero.txt");
    
  for (int i=0; i<nx;i++)
  {
    getline(infile,line);
    dez[0][i]=atof(line.c_str());
  }
  infile.close();  
  
  dez[0][0]=0.0;
  dez[0][nx-1]=0.0;
  dez[1][0]=0.0;
  dez[1][nx-1]=0.0;
    
  for(int x=1;x<(nx-1);x++)
  {
      dez[1][x]=dez[0][x]+((c*c)/(2*cg*cg))*(dez[0][x+1]+dez[0][x-1]-2*dez[0][x]);
  }   
    
  outfile.open("datos.dat");
    
  for(int x=0;x<nx;x++)
  {
      outfile << dez[0][x] << " ";
  }
  outfile << "\n";
  for(int t=2;t<nt;t++)
  {
      for(int x=1;x<(nx-1);x++)
      {
          dez[2][x]=2*dez[1][x]-dez[0][x]+((c*c)/(cg*cg))*(dez[1][x+1]+dez[1][x-1]-2*dez[1][x]);
      }
      for(int x=1;x<(nx-1);x++)
      {
          dez[0][x]=dez[1][x];
          dez[1][x]=dez[2][x];
      }
      for(int x=0;x<nx;x++)
      {
          outfile << dez[1][x] << " ";
      }
      outfile << "\n";
      
  }
  
  
    
  return 0;
}


