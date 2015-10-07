



void eff_fitter_CMS(){

static const Int_t n = 14;
Double_t cms_pt_val[n] = {35, 45, 55, 65, 75, 90, 110, 140, 185, 235, 290, 360, 450, 585};
Double_t cms_effB[n] = {0.597767, 0.619989, 0.663316, 0.67937, 0.707839, 0.721407, 0.728765, 0.741069, 0.718627, 0.697444, 0.670068, 0.63153, 0.581825, 0.544507};
Double_t cms_effC[n] = {0.162417, 0.153629, 0.169673, 0.177044, 0.193108, 0.201717, 0.207834, 0.211455, 0.198939, 0.190156, 0.176425, 0.168895, 0.157638, 0.148846};
Double_t cms_effL[n] = {0.0162421, 0.0112699, 0.0117579, 0.0112546, 0.0119929, 0.0123575, 0.0130933, 0.014572, 0.0170408, 0.0190156, 0.0206191, 0.023339, 0.0280426, 0.032249};


TGraph* cms_effB_gr = new TGraph(n,cms_pt_val,cms_effB);
TGraph* cms_effC_gr = new TGraph(n,cms_pt_val,cms_effC);
TGraph* cms_effL_gr = new TGraph(n,cms_pt_val,cms_effL);


TCanvas *c1 = new TCanvas("c1","CMS efficiencies",200,10,700,500);

//cms_effB_gr->Draw("AP*");
cms_effB_gr->SetMinimum(0);
cms_effB_gr->SetMaximum(1);

cms_effB_gr->SetMarkerStyle(8);
cms_effC_gr->SetMarkerStyle(8);
cms_effL_gr->SetMarkerStyle(8);

cms_effB_gr->SetMarkerColor(8);
cms_effC_gr->SetMarkerColor(4);
cms_effL_gr->SetMarkerColor(2);

cms_effB_gr->Draw("AP");
cms_effC_gr->Draw("P");
cms_effL_gr->Draw("P");

cms_effL_gr->Fit("pol1");

TF1 *fB = new TF1("fB","0.85*TMath::TanH([0]*x)*(25/(1+[1]*x))",20,600);
cms_effB_gr->Fit(fB);

TF1 *fC = new TF1("fC","0.25*TMath::TanH([0]*x)*(1/(1+[1]*x))",20,600);
cms_effC_gr->Fit(fC);
}









