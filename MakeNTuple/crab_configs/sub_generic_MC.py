from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'WJ_Pt_250_Moriond_1'

config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ConfFile_cfg.py'
config.JobType.inputFiles = ['RPs_xi.txt','xi_as_a_function_of_x_graph_b1.root','xi_as_a_function_of_x_graph_b2.root','MyDataPileupHistogram.root','PileupMC.root']

config.Data.inputDataset = '/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'

config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic' #'FileBased'
#config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/user/mthiel' #%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

config.Data.outputDatasetTag = 'background'

config.JobType.outputFiles = ['out.root']

config.Site.storageSite = 'T2_CH_CERN'

