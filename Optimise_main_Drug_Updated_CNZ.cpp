#include <vector>
#include <zlib.h>
// #include <stdio.h>
// #include <stdlib.h>
#include <math.h>
#include <string.h>
#include <fstream>
#include <string>
#include <iomanip>      // std::setprecision


#include "SingleCellParameter.hpp"
#include "CRN_ODE.h"
#include "Updated_CNZ.h"
#include  <iomanip>
#include "EnumSimulationCtrl.hpp"
#include "APInof.hpp"
#include "stimulus.h"
// #define OUT_PHASE
// #define OUT_ICs
#define S1_Num 100
#define STATENUM 40
#define OUT_AP

int main(int argc, char const *argv[])
{
	double *state;

	APInfor AP("Drug_CNZ_APD_measure.dat", false);
	state =  new double [STATENUM] ; //(double *)malloc(STATENUM * sizeof(double));
	double stim;
	double v;
	double dv;
	double BCL = 1000.0;
	// crn_con_initial_conditions_Vent(state, 1 );
	BCL               = atof(argv[1]);
	int celltype      = atof(argv[2]);
	double S2         = atof(argv[3]);
	std::string Mut   = (argv[4]);
	std::string Mode  = (argv[5]);
	int count         = 0;
	double Total_time = 30000;
	double t          = 0.0;
	double outputTime = 0.0;
	std::ofstream output_file( "Drug_CNZ_out.dat");                      // output filename

	// TypeCell celltype    = LVEPI;
	// celltype = (TypeCell)in_celltype;                            // Type of cell  0 - 5
	double time_step     = 0.02;                                 // Time step



	int outfreq       = int(0.02 * 1 / time_step);
	// TNNP_MarkovIKr_Initialise(state, celltype);

	// CRN_1998_ODE_Initialise(state, 0);
	INa_IKur_Drug_Updated_CNZ_ODE_Initialise(state, 0);
	SingleCellPara cell_para;
	AtriaCellType type;
	type = GetCellTypeFromLabel(celltype);
	cell_para.SetCellTypePara(type);



	IKurMuationType mut = WT;

	if (Mut == "WT") {
		mut = WT;
	}
	else if (Mut == "D322H")
	{
		mut = D322H;
	} else if (Mut == "E48G")
	{
		mut = E48G;
	} else if (Mut == "A305T") {
		mut = A305T;
	} else if (Mut == "Y155C") {
		mut = Y155C;
	} else if (Mut == "D469E") {
		mut = D469E;
	} else if (Mut == "P488S")
	{
		mut = P488S;
	} else {
		std::cout << "wrong cell of mutation";
		std::exit(0);
	}


	cell_para.SetIKurMutationPara(mut);
	int AF = atoi(argv[7]);

	double IKur_Drug_con = atof(argv[6]);


	cell_para.drug_INa_concen = 0.0;
	cell_para.SetAcacetinEffectPara(IKur_Drug_con); // 3.2 um of acacetin


	double Ka = atof(argv[8]);
	double Ki = atof(argv[9]);
	double La = atof(argv[10]);
	double Li = atof(argv[11]);

	cell_para.SetINaBlockPara(0.0, Ka,  Ki,  La,  Li);

	if (AF == 1) {
		cell_para.SetAFTypePara(AF4);
	}
	// cell_para.SetAFTypePara(NONE);


	// sprintf(filename_out, "results/BCL_%d_Model_%s_Region_%d_FB_%d_%d_Mut_%s_AF_%d_AP.txt", Argin.BCL, Argin.Model_type_char, Argin.region_3D, Argin.FB_type, Argin.FB_number, Argin.mutation_char, Argin.AF_model);
	// std::cout << BCL << " " <<celltype << " " << Mut  << ICFilename << std::endl;

	// Total_time = 50 * BCL;
	// double S2 = 0.5 * BCL;
	Total_time = 1500000.0;//(S1_Num - 1) * BCL + 2 * BCL;

	double Time_Start = 0.0;
	if (Mode == "Restart")
	{
		std::ifstream infile("Restart_ICs/ICs.bin", std::ios::binary | std::ios::in);
		if (infile.is_open())
		{
			infile.read(reinterpret_cast<char*>(state), sizeof(double)*STATENUM);
			infile.close();
			Time_Start = Total_time - 3 * BCL - time_step;
		} else {
			std::cout << "ICs file not opened..." << std::endl;
		}
	}

	if (Mode == "SimDrug")   // read the ICs.bin, set the time to be 60 s before termination of simulation
	{
		std::ifstream infile("Restart_ICs/ICs.bin", std::ios::binary | std::ios::in);
		if (infile.is_open())
		{
			infile.read(reinterpret_cast<char*>(state), sizeof(double)*STATENUM);
			infile.close();
			Time_Start = Total_time - 62 * 1000.0 - time_step;
		} else {
			std::cout << "ICs file not opened..." << std::endl;
		}
	}
	// Total_time = 2000000.0;//(S1_Num - 1) * BCL + 2 * BCL;
	// Total_time = 400000.0;//(S1_Num - 1) * BCL + 2 * BCL;

	// std::cout << "Time_Start = " << Time_Start << std::endl;

	for (t = Time_Start; t < Total_time; t = t + time_step)
	{
		// if (outputTime >= 0.0 && outputTime <= 2.0) stim = -18; else stim = 0.0;
		// if (outputTime > BCL) outputTime = 0.0;

		if (Mode == "SimDrug")   // read the ICs.bin, set the time to be 60 s before termination of simulation
		{
			if (t > Total_time - 62 * 1000) {
				cell_para.drug_INa_concen = 60.0*1e-6; // apply 60 umol INa blocker.. or 60.0*1e-6 mol;
			}
		}

		stim = S1S2(0.0, -20, BCL, 10000/*S1_Num*/, S2, t, 2.0);

		outputTime = outputTime + time_step;
		// double dv = TNNP_MarkovIKr_ODE_RV_Gradient(time_step, stim, state, ABIndex, 1.0, celltype);
		// double dv = TNNP_MarkovIKr_ODE(time_step, stim, state, ABIndex, celltype);
		// double dv = CRN_1998_ODE_New_INa(time_step, stim, cell_para, state);
		double dv = INa_IKur_Drug_Updated_CNZ_ODE(time_step, stim, cell_para, state);
		// double dv = CRN_1998_ODE(time_step, stim, cell_para, state);
		state[0] += - dv * time_step;

		AP.MeasureAPD90_INa(t, stim, BCL, time_step, state[0], cell_para.INa);

		// only output once
		if (t > Total_time - 3 * BCL - 0.5 * time_step and t < Total_time - 3 * BCL + 0.5 * time_step) {
			if (Mode == "Normal")
			{
				std::ofstream out("Restart_ICs/ICs.bin", std::ios::binary | std::ios::out);
				if (out.is_open())
				{
					out.write(reinterpret_cast<char*>(state), sizeof(double)*STATENUM);
					out.close();
				}
			}
		}

#ifdef OUT_AP

		if (count % outfreq == 0 and t > Total_time-1100)
		{
			// output_file << t << ' ' << state[0] << ' ' <<  state[7]*state[21] << ' ' <<  state[8]*state[22] << ' ' << 4.0*7.8* state[9] * state[9] * state[9] * (0.8 * state[7] + (1.0 - 0.8) * state[8]) * (state[0] - 66.0)<< std::endl;
			output_file << std::setprecision(9)
			            << t << " "    // 1
			            << state[0] << " "		// Vm
			            << state[9]  << " "  // cai
			            << state[8]  << " "   // Nai
			            << state[9] << " "		// Cass
			            << state[10] << " "   // 6
			            << cell_para.INa << " "
			            << cell_para.IKur << " "
			            << state[32] << " " //INa_BA;
			            << state[33] << " " //INa_BI;
			            << state[34] << " " //IKur_BO;
			            << state[35] << " " //IKur_BC;
			            << std::endl;
			// << ' ' <<  state[8]*state[22] << ' ' << 4.0 * 7.8 * state[9] * state[9] * state[9] *  (0.8 * (state[21]*state[7]) + (1.0 - 0.8) * (state[22]*state[8]))* (state[0] - 66.0) << std::endl;
		}
#endif
		count ++;

#ifdef OUT_PHASE
		int AF_model = 4;
		int region_3D = celltype;

		if (t >= 15400  && t <= 15400 + 205 * 1.5 + 5)
			if (count % 150 == 0)
			{	FILE *phase_out;
				char filename_phase[100];

				sprintf(filename_phase, "ICs/phase_%03d_Region_%d_Mut_%s_AF_%d_ICs.dat", 205 - ((int) ((t  - 15400) / 1.5)), region_3D, Mut.c_str(), AF_model );
				phase_out = fopen(filename_phase, "wt");
				int i = 0;
				for (i = 0; i < 29; i++) {
					fprintf(phase_out, "%lf\n", state[i]);
				}
				fprintf(phase_out, "%f\n", state[34]);
				fprintf(phase_out, "%f\n", state[35]);
				fprintf(phase_out, "%f\n", 0.0);
				fprintf(phase_out, "%f\n", 0.0);
				// fprintf(phase_out, "%f\n", state[38]);
				fclose(phase_out);
			}
#endif

	}


	output_file.close();



#ifdef OUT_ICs
	char ICFilename[200];

	sprintf(ICFilename, "Drug_BCL_%.0f_Model_CRN_Region_%d_Mut_%s_AF_%d_ICs.txt", BCL, celltype, Mut.c_str(), 4);
	std::ofstream output_file2(ICFilename);                      // output filename

	for (int i = 0; i < STATENUM; ++i)
	{
		output_file2 << std::setprecision(10) << state[i] << std::endl;
	}
	output_file2.close();
#endif

	std::ofstream output_AMP_ratio( "ratio.log");                      // output filename

	output_AMP_ratio << AP.AMP_over_last << std::endl;
	output_AMP_ratio.close();

	// std::cout << S2 << " ";
	// AP.ReportLast();
	AP.ReportLastTwo(S2);

	delete [] state;
	return 0;
}
