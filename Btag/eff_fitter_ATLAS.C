



void eff_fitter_ATLAS(){

static const Int_t n = 29;
Double_t atlas_pt_val[n] = {30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510, 530, 550, 570, 590};

Double_t atlas_effB[n] = {0.599092,0.708571,0.734056,0.747139,0.753768,0.747139,0.747139,0.734056,0.7276,0.721201,0.708571,0.696163,0.696163,0.677957,0.666085,0.64296,0.637306,0.60977,0.593823,0.56317,0.553308,0.524746,0.511022,0.476156,0.459625,0.471969,0.455583,0.443669,0.432066};
Double_t atlas_effC[n] = {0.113832,0.12996,0.131113,0.12996,0.127684,0.127684,0.127684,0.128817,0.126562,0.123252,0.124345,0.121093,0.122168,0.116889,0.116889,0.104208,0.098829,0.096245,0.092903,0.085049,0.080658,0.07319,0.079949,0.057152,0.061337,0.062984,0.04308,0.043847,0.06525};
Double_t atlas_effL[n] = {0.0021,0.002195,0.002254,0.002294,0.002335,0.002462,0.002762,0.002861,0.003153,0.003414,0.0036,0.003829,0.004295,0.004904,0.005125,0.005263,0.00531,0.006062,0.0058,0.004529,0.005217,0.00461,0.00411,0.005171,0.005599,0.00422,0.006116,0.006009,0.006622};


TGraph* atlas_effB_gr = new TGraph(n,atlas_pt_val,atlas_effB);
TGraph* atlas_effC_gr = new TGraph(n,atlas_pt_val,atlas_effC);
TGraph* atlas_effL_gr = new TGraph(n,atlas_pt_val,atlas_effL);


TCanvas *c1 = new TCanvas("c1","ATLAS efficiencies",200,10,700,500);

//cms_effB_gr->Draw("AP*");
atlas_effB_gr->SetMinimum(0);
atlas_effB_gr->SetMaximum(1);


atlas_effB_gr->SetMarkerStyle(8);
atlas_effC_gr->SetMarkerStyle(8);
atlas_effL_gr->SetMarkerStyle(8);

atlas_effB_gr->SetMarkerColor(8);
atlas_effC_gr->SetMarkerColor(4);
atlas_effL_gr->SetMarkerColor(2);

atlas_effB_gr->Draw("AP");
atlas_effC_gr->Draw("P");
atlas_effL_gr->Draw("P");

atlas_effL_gr->Fit("pol1");

TF1 *fB = new TF1("fB","0.80*TMath::TanH([0]*x)*(30/(1+[1]*x))",20,600);
atlas_effB_gr->Fit(fB);

TF1 *fC = new TF1("fC","0.20*TMath::TanH([0]*x)*(1/(1+[1]*x))",20,600);
atlas_effC_gr->Fit(fC);
}









